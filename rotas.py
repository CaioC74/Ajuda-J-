# -*- coding: utf-8 -*-
"""Rotas (endereços) do app, sessões e ações que mudam o estado."""
import copy
import csv
import datetime
import os
import re
import threading
import uuid
from urllib.parse import quote

import dados
import telas
from telas import Redirecionar, um

PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_REG = os.path.join(PASTA, "registros")
TRAVA = threading.Lock()
SESSOES = {}


def nova_sessao():
    """Estado inicial do app para uma pessoa (cada navegador tem o seu)."""
    return {
        "letra": "normal", "contraste": False, "voz": False, "simples": False,
        "prefs": {"vagas": True, "beneficios": True, "servicos": True},
        "avisos": copy.deepcopy(dados.AVISOS),
        "areas": [], "dist": "2",
        "filtros": {"contrato": "todos", "verificadas": False, "ordem": "perto"},
        "salvas": [], "respostas": {}, "offline": False,
        "lista_url": "/empregos/vagas", "benef_volta": "/beneficios/todos",
    }


def obter_sessao(sid):
    with TRAVA:
        if sid and sid in SESSOES:
            return sid, SESSOES[sid], False
        sid = uuid.uuid4().hex
        SESSOES[sid] = nova_sessao()
        return sid, SESSOES[sid], True


def _gravar_csv(nome, cabecalho, linha):
    """Guarda uma linha em registros/<nome>. Nunca derruba o app se falhar."""
    try:
        os.makedirs(PASTA_REG, exist_ok=True)
        caminho = os.path.join(PASTA_REG, nome)
        novo = not os.path.exists(caminho)
        with TRAVA:
            with open(caminho, "a", newline="", encoding="utf-8-sig") as f:
                w = csv.writer(f, delimiter=";")
                if novo:
                    w.writerow(cabecalho)
                w.writerow(linha)
    except OSError:
        pass


def _agora():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _seguro(v):
    return bool(v) and v.startswith("/") and not v.startswith("//") and "\\" not in v and ":" not in v


def _prox(q, padrao):
    v = um(q, "next")
    return v if _seguro(v) else padrao


# ----------------------------------------------------------------------------
# Ações (mudam o estado e voltam para uma tela)
# ----------------------------------------------------------------------------
def a_letra(s, q, tam):
    s["letra"] = tam
    return Redirecionar(_prox(q, "/ajustes"))


def a_letra_ciclo(s, q):
    ordem = ["menor", "normal", "maior"]
    s["letra"] = "normal" if s["letra"] == "maior" else ordem[ordem.index(s["letra"]) + 1]
    return Redirecionar(_prox(q, "/inicio"))


def _alternar(chave):
    def f(s, q):
        s[chave] = not s[chave]
        return Redirecionar(_prox(q, "/ajustes"))
    return f


def a_pref(s, q, chave):
    s["prefs"][chave] = not s["prefs"][chave]
    return Redirecionar(_prox(q, "/avisos"))


def a_salvar(s, q, vid):
    vid = int(vid)
    if dados.vaga_por_id(vid) is None:
        return None
    if vid in s["salvas"]:
        s["salvas"].remove(vid)
    else:
        s["salvas"].append(vid)
    return Redirecionar("/empregos/vaga/" + str(vid))


def a_filtros(s, q):
    contrato = um(q, "contrato", "todos")
    s["filtros"]["contrato"] = contrato if contrato in ("todos", "CLT", "PJ", "Informal") else "todos"
    s["filtros"]["verificadas"] = um(q, "verif") == "1"
    ordem = um(q, "ordem", "perto")
    s["filtros"]["ordem"] = ordem if ordem in ("perto", "salario") else "perto"
    return Redirecionar("/empregos/vagas")


def a_limpar_filtros(s, q):
    s["filtros"] = {"contrato": "todos", "verificadas": False, "ordem": "perto"}
    return Redirecionar("/empregos/vagas")


def a_dist_any(s, q):
    s["dist"] = "any"
    return Redirecionar("/empregos/vagas")


def a_responder(s, q, n, valor):
    permitidas = [v for v, _ in dados.PERGUNTAS[int(n) - 1][2]]
    if valor not in permitidas:
        return Redirecionar("/beneficios/passo/" + n)
    s["respostas"][n] = valor
    if int(n) >= 4:
        return Redirecionar("/beneficios/resultado")
    return Redirecionar("/beneficios/passo/" + str(int(n) + 1))


def a_abrir_aviso(s, q, aid):
    for a in s["avisos"]:
        if a["id"] == int(aid):
            a["lido"] = True
            return Redirecionar(a["destino"])
    return Redirecionar("/avisos")


def a_avisos_lidos(s, q):
    for a in s["avisos"]:
        a["lido"] = True
    return Redirecionar("/avisos")


def a_offline(s, q, modo):
    s["offline"] = (modo == "on")
    return Redirecionar(_prox(q, "/inicio"))


def a_novo_aviso(s, q):
    novo_id = max([a["id"] for a in s["avisos"]] + [0]) + 1
    s["avisos"].insert(0, {"id": novo_id, "cat": "vagas", "titulo": "Nova vaga próxima!",
                           "texto": "Porteiro — 1,5 km de você", "quando": "Agora", "lido": False,
                           "destino": "/empregos/vaga/5"})
    return Redirecionar(_prox(q, "/teste"))


def a_reiniciar(s, q):
    s.clear()
    s.update(nova_sessao())
    return Redirecionar("/")


def a_golpe_enviar(s, q, corpo):
    tipos = [k for k, _ in dados.TIPOS_GOLPE]
    tipo = um(corpo, "tipo")
    if tipo not in tipos:
        return Redirecionar("/golpe")
    relato = um(corpo, "relato")[:1000]
    contato = um(corpo, "contato")[:200]
    caminho = os.path.join(PASTA_REG, "denuncias.csv")
    try:
        with open(caminho, encoding="utf-8-sig") as f:
            numero = max(sum(1 for _ in f), 1)
    except OSError:
        numero = 1
    protocolo = "AJ-%06d" % numero
    _gravar_csv("denuncias.csv", ["data", "protocolo", "tipo", "relato", "contato"],
                [_agora(), protocolo, tipo, relato, contato])
    return Redirecionar("/golpe/ok?p=" + quote(protocolo))


# ----------------------------------------------------------------------------
# Tabelas de rotas
# ----------------------------------------------------------------------------
PAGINAS = [
    (r"^/$", telas.boas_vindas),
    (r"^/inicio$", telas.home),
    (r"^/empregos$", telas.emp_passo1),
    (r"^/empregos/passo2$", telas.emp_passo2),
    (r"^/empregos/buscando$", telas.emp_buscando),
    (r"^/empregos/vagas$", telas.emp_lista),
    (r"^/empregos/filtrar$", telas.emp_filtrar),
    (r"^/empregos/vaga/(\d+)$", telas.emp_detalhe),
    (r"^/empregos/salvas$", telas.emp_salvas),
    (r"^/beneficios$", lambda s, q, c: telas.ben_passo(s, q, c, "1")),
    (r"^/beneficios/passo/([1-4])$", telas.ben_passo),
    (r"^/beneficios/resultado$", telas.ben_resultado),
    (r"^/beneficios/todos$", telas.ben_todos),
    (r"^/beneficios/([a-z-]+)$", telas.ben_detalhe),
    (r"^/avisos$", telas.avisos),
    (r"^/ajuda$", telas.ajuda),
    (r"^/ajuda/escrever$", telas.ajuda_escrever),
    (r"^/ajuda/pergunta$", telas.ajuda_pergunta),
    (r"^/ajustes$", telas.ajustes),
    (r"^/golpe$", telas.golpe),
    (r"^/golpe/ok$", telas.golpe_ok),
    (r"^/cras$", telas.cras),
    (r"^/erro$", telas.erro),
    (r"^/teste$", telas.painel_teste),
]

ACOES = [
    (r"^/acao/letra/(menor|normal|maior)$", a_letra),
    (r"^/acao/letra-ciclo$", a_letra_ciclo),
    (r"^/acao/contraste$", _alternar("contraste")),
    (r"^/acao/voz$", _alternar("voz")),
    (r"^/acao/simples$", _alternar("simples")),
    (r"^/acao/pref/(vagas|beneficios|servicos)$", a_pref),
    (r"^/acao/salvar/(\d+)$", a_salvar),
    (r"^/acao/filtros$", a_filtros),
    (r"^/acao/limpar-filtros$", a_limpar_filtros),
    (r"^/acao/dist-any$", a_dist_any),
    (r"^/beneficios/responder/([1-4])/([a-z_]+)$", a_responder),
    (r"^/avisos/abrir/(\d+)$", a_abrir_aviso),
    (r"^/acao/avisos-lidos$", a_avisos_lidos),
    (r"^/acao/offline/(on|off)$", a_offline),
    (r"^/acao/novo-aviso$", a_novo_aviso),
    (r"^/reiniciar$", a_reiniciar),
]


def despachar(metodo, caminho, q, corpo, s, url_completa, sid):
    """Devolve (status, tipo, conteúdo). tipo: html | redir | vazio."""
    if caminho == "/favicon.ico":
        return 204, "vazio", ""

    if metodo == "POST":
        if caminho == "/golpe/enviar":
            return _resultado(a_golpe_enviar(s, q, corpo), s, caminho)
        return 405, "html", telas.nao_encontrada(s, caminho)

    for padrao, fn in ACOES:
        m = re.match(padrao, caminho)
        if m:
            return _resultado(fn(s, q, *m.groups()), s, caminho)

    for padrao, fn in PAGINAS:
        m = re.match(padrao, caminho)
        if m:
            _gravar_csv("navegacao.csv", ["data", "sessao", "endereco"], [_agora(), sid[:6], url_completa])
            return _resultado(fn(s, q, url_completa, *m.groups()), s, caminho)
    return 404, "html", telas.nao_encontrada(s, url_completa)


def _resultado(r, s, caminho):
    if r is None:
        return 404, "html", telas.nao_encontrada(s, caminho)
    if isinstance(r, Redirecionar):
        return 303, "redir", r.url
    return 200, "html", r
