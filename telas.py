# -*- coding: utf-8 -*-
"""Telas do app Ajuda Já. Cada função recebe (sessão, parâmetros, caminho)
e devolve uma página HTML (texto) ou um Redirecionar."""
import datetime
import html
from urllib.parse import quote

import assistente
import dados
from estilo import CSS, JS, ic


class Redirecionar(object):
    def __init__(self, url):
        self.url = url


def esc(t):
    return html.escape(str(t), quote=True)


def um(q, chave, padrao=""):
    v = q.get(chave)
    return v[0] if v else padrao


def km(v):
    return ("%.1f" % v).replace(".", ",")


def visiveis(s):
    return [a for a in s["avisos"] if s["prefs"].get(a["cat"], True)]


def nao_lidos(s):
    return len([a for a in visiveis(s) if not a["lido"]])


# ----------------------------------------------------------------------------
# Estrutura comum de todas as telas
# ----------------------------------------------------------------------------
NAV = [("inicio", "/inicio", "Início", "home"),
       ("avisos", "/avisos", "Avisos", "bell"),
       ("ajuda", "/ajuda", "Ajuda", "help"),
       ("ajustes", "/ajustes", "Ajustes", "sliders")]

TAMANHOS_PX = {"menor": 17, "normal": 19, "maior": 23}


def _topo(topo):
    if topo is None:
        return ""
    if topo[0] == "marca":
        titulo = ('<strong class="pg">' + esc(topo[1]) + '</strong>') if len(topo) > 1 and topo[1] else ""
        return ('<header class="topo"><span class="logo">A</span><span class="marca">Ajuda Já'
                '<small>Prefeitura</small></span>' + titulo + '</header>')
    return ('<header class="topo"><a class="voltar" href="' + esc(topo[1]) + '" aria-label="Voltar">'
            + ic("chevron-left") + '</a><span class="titulo">' + esc(topo[2]) + '</span></header>')


def _ferramentas(s, caminho):
    maior = s["letra"] == "maior"
    rotulo = "Letra menor" if maior else "Letra maior"
    sinal = "A−" if maior else "A+"
    return ('<div class="ferr"><a class="btn-mini" href="/acao/letra-ciclo?next=' + quote(caminho, safe="") + '">'
            '<b>' + sinal + '</b> ' + rotulo + '</a>'
            '<button type="button" class="btn-mini" data-ouvir="tela">' + ic("volume") + ' Ouvir tela</button></div>')


def pagina(s, titulo, corpo, caminho="/", topo=None, nav=None, ferramentas=True, progresso=None, extra_head=""):
    px = TAMANHOS_PX[s["letra"]] + (2 if s["simples"] else 0)
    classes = []
    if s["contraste"]:
        classes.append("contraste")
    if s["simples"]:
        classes.append("simples")
    barra = ""
    if progresso:
        passo, total, pct = progresso
        barra = ('<div class="prog"><div class="prog-t"><span>Passo ' + str(passo) + ' de ' + str(total)
                 + '</span><b>' + str(pct) + '%</b></div><div class="prog-b"><i style="width:' + str(pct) + '%"></i></div></div>')
    menu = ""
    if nav:
        itens = ""
        for chave, href, rotulo, icone in NAV:
            extra = ""
            if chave == "avisos" and nao_lidos(s):
                extra = '<span class="n">' + str(nao_lidos(s)) + '</span>'
            itens += ('<a href="' + href + '"' + (' class="ativo" aria-current="page"' if chave == nav else '') + '>'
                      + ic(icone) + extra + rotulo + '</a>')
        menu = '<nav class="nav" aria-label="Menu principal">' + itens + '</nav>'
    return "".join([
        '<!doctype html><html lang="pt-BR" style="font-size:', str(px), 'px"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<title>', esc(titulo), ' — Ajuda Já</title><style>', CSS, '</style>', extra_head, '</head>',
        '<body class="', " ".join(classes), '" data-autoler="', "1" if s["voz"] else "0", '">',
        '<div class="celular">', _topo(topo), barra,
        '<main class="tela">', _ferramentas(s, caminho) if ferramentas else "",
        '<div id="conteudo">', corpo, '</div></main>', menu,
        '<p id="aviso-js" class="aviso-js" role="status" aria-live="polite" hidden></p></div>',
        '<script>', JS, '</script></body></html>',
    ])


def _x():
    return ('<svg class="x" viewBox="0 0 100 60" preserveAspectRatio="none" aria-hidden="true">'
            '<line x1="0" y1="0" x2="100" y2="60"/><line x1="100" y1="0" x2="0" y2="60"/></svg>')


def _mapa(rotulo):
    return ('<div class="mapa" role="img" aria-label="Mapa aproximado: ' + esc(rotulo) + '">' + _x() + ic("pin")
            + '<span class="rotulo">' + esc(rotulo) + '</span></div>')


def _caixa(tipo, icone, conteudo):
    return '<div class="caixa ' + tipo + '">' + ic(icone) + '<div>' + conteudo + '</div></div>'


def _menu_card(href, icone, cor, titulo, sub):
    return ('<a class="menu-card" href="' + esc(href) + '"><span class="caixa-ico ' + cor + '">' + ic(icone) + '</span>'
            '<span class="tx"><strong>' + esc(titulo) + '</strong><span class="s">' + esc(sub) + '</span></span>'
            + ic("right") + '</a>')


def _aviso_golpe():
    return _caixa("info", "alert", "O app Ajuda Já é gratuito. Desconfie de cobranças ou pedidos de senha.")


# ----------------------------------------------------------------------------
# Início
# ----------------------------------------------------------------------------
def boas_vindas(s, q, caminho):
    passos = ""
    for n, icone, rot in [(1, "user", "Conte sobre você"), (2, "search", "Veja o que está disponível"),
                          (3, "message", "Receba orientação")]:
        passos += ('<div><div class="ph">' + _x() + ic(icone) + '</div><span class="num">' + str(n) + '</span><div>'
                   + rot + '</div></div>')
    corpo = ('<div class="centro"><div class="logo-g">A</div><h1 class="t" style="font-size:2rem">Ajuda já</h1>'
             '<p class="sub">Serviços da Prefeitura</p>'
             '<p style="font-size:1.25rem;font-weight:600;margin:1.2rem 0">Encontre emprego, benefícios e serviços públicos perto de você</p></div>'
             '<div class="passos3">' + passos + '</div>'
             '<a class="btn pri" href="/inicio">Começar</a>'
             '<a class="btn" href="/ajuda">' + ic("help") + ' Preciso de ajuda</a>')
    return pagina(s, "Bem-vinda", corpo, caminho, ferramentas=False)


def home(s, q, caminho):
    hora = datetime.datetime.now().hour
    saud = "Bom dia" if hora < 12 else ("Boa tarde" if hora < 18 else "Boa noite")
    cartoes = "".join([
        _menu_card("/empregos", "briefcase", "azul", "Empregos", "Vagas próximas a você"),
        _menu_card("/beneficios", "gift", "verde", "Benefícios", "Bolsa Família e outros auxílios"),
        _menu_card("/ajuda", "message", "roxo", "Dúvidas", "Pergunte falando ou escrevendo"),
    ])
    rotulo_letra = "Diminuir letra" if s["letra"] == "maior" else "Aumentar letra"
    acess = ('<div class="card nao-simples"><div class="linha-btn" style="margin:0">'
             '<a class="btn" style="margin:0" href="/acao/letra-ciclo?next=/inicio">' + ic("type") + ' ' + rotulo_letra + '</a>'
             '<button type="button" class="btn" style="margin:0" data-ouvir="tela">' + ic("volume") + ' Ouvir tela</button></div></div>')
    corpo = ('<p class="sub" style="margin:0">' + saud + ' 👋</p><h1 class="t" style="font-size:1.8rem">'
             + esc(dados.PERFIL["nome"]) + '</h1>' + cartoes + acess + _aviso_golpe())
    return pagina(s, "Início", corpo, caminho, topo=("marca",), nav="inicio", ferramentas=False)


# ----------------------------------------------------------------------------
# Empregos
# ----------------------------------------------------------------------------
def emp_passo1(s, q, caminho):
    marcadas = set(s["areas"])
    opcoes = ""
    for chave, rotulo in dados.AREAS:
        opcoes += ('<label class="opt"><input type="checkbox" name="area" value="' + chave + '" data-chaves="'
                   + esc(dados.CHAVES_AREA[chave]) + '"' + (" checked" if chave in marcadas else "") + '><span>'
                   + esc(rotulo) + '</span></label>')
    corpo = ('<h1 class="t">Que trabalhos você já fez?</h1>'
             '<p class="sub">Selecione tudo que souber fazer. Pode marcar mais de um.</p>'
             '<button type="button" class="btn claro" style="border-color:var(--pri);color:var(--pri)" data-falar="vagas">'
             + ic("mic") + ' Falar em voz alta</button>'
             '<form method="get" action="/empregos/passo2"><input type="hidden" name="from" value="1">'
             '<div class="grid2">' + opcoes + '</div>'
             '<div class="linha-btn"><a class="btn" href="/empregos/passo2?pular=1">Pular</a>'
             '<button class="btn pri" type="submit">Continuar</button></div></form>')
    return pagina(s, "Buscar emprego", corpo, caminho, topo=("voltar", "/inicio", "Buscar emprego"),
                  progresso=(1, 2, 50))


def emp_passo2(s, q, caminho):
    if um(q, "pular") == "1":
        s["areas"] = []
    elif um(q, "from") == "1":
        s["areas"] = [a for a in q.get("area", []) if a in dados.AREAS_CHAVES]
    opcoes = ""
    for valor, titulo, sub in [("2", "Perto de casa", "Até 2 km"), ("5", "Um pouco longe", "Até 5 km"),
                               ("any", "Qualquer lugar", "Sem limite de distância")]:
        opcoes += ('<label class="opt grande"><input type="radio" name="dist" value="' + valor + '"'
                   + (" checked" if s["dist"] == valor else "") + '><span>' + titulo + '<small>' + sub + '</small></span></label>')
    corpo = ('<h1 class="t">Onde você prefere trabalhar?</h1>'
             '<p class="sub">Escolha a distância que funciona melhor para você.</p>'
             '<form method="get" action="/empregos/buscando">' + opcoes
             + '<h2 class="t" style="font-size:1rem">Sua localização aproximada</h2>' + _mapa(dados.PERFIL["bairro"])
             + '<button class="btn pri" type="submit">' + ic("search") + ' Buscar vagas</button></form>')
    return pagina(s, "Buscar emprego", corpo, caminho, topo=("voltar", "/empregos", "Buscar emprego"),
                  progresso=(2, 2, 100))


def emp_buscando(s, q, caminho):
    d = um(q, "dist")
    if d in ("2", "5", "any"):
        s["dist"] = d
    if s["offline"]:
        return Redirecionar("/erro?de=" + quote("/empregos/buscando", safe=""))
    corpo = ('<div class="centro" style="padding-top:5rem"><div class="spin" role="progressbar" aria-label="Carregando"></div>'
             '<h1 class="t">Procurando vagas…</h1><p class="sub">Aguarde um momento</p>'
             '<p><a class="link" href="/acao/offline/on?next=/empregos/buscando">Simular modo offline</a></p>'
             '<p><a class="link" href="/empregos/vagas">Ver as vagas agora</a></p></div>')
    return pagina(s, "Buscando vagas", corpo, caminho, topo=("voltar", "/empregos/passo2", "Buscando vagas"),
                  ferramentas=False, extra_head='<meta http-equiv="refresh" content="2;url=/empregos/vagas">')


def filtrar_vagas(s, termo=""):
    areas = set(s["areas"])
    f = s["filtros"]
    res = []
    for v in dados.VAGAS:
        if areas and v["area"] not in areas:
            continue
        if s["dist"] != "any" and v["km"] > float(s["dist"]):
            continue
        if f["contrato"] != "todos" and v["contrato"] != f["contrato"]:
            continue
        if f["verificadas"] and not v["verificado"]:
            continue
        if termo and assistente.normalizar(termo).strip() not in assistente.normalizar(v["cargo"] + " " + v["empresa"]):
            continue
        res.append(v)
    if f["ordem"] == "salario":
        res.sort(key=lambda v: -v["salario_num"])
    else:
        res.sort(key=lambda v: v["km"])
    return res


def _card_vaga(v):
    selo = ('<span class="chip ok">✓ Verificado</span>' if v["verificado"]
            else '<span class="chip aviso">Não verificado</span>')
    return ('<a class="card vaga" href="/empregos/vaga/' + str(v["id"]) + '"><div class="topo-v"><h3>' + esc(v["cargo"])
            + '</h3>' + selo + '</div><div class="emp">' + esc(v["empresa"]) + '</div><div class="linha">' + ic("pin")
            + '<span>' + km(v["km"]) + ' km</span><span class="chip">' + esc(v["contrato"]) + '</span><span>'
            + esc(v["sal_curto"]) + '</span></div></a>')


def emp_lista(s, q, caminho):
    termo = um(q, "q").strip()
    s["lista_url"] = caminho + ("?q=" + quote(termo) if termo else "")
    vagas = filtrar_vagas(s, termo)
    f = s["filtros"]
    ativos = (f["contrato"] != "todos") + bool(f["verificadas"]) + (f["ordem"] != "perto")
    rotulo_f = "Filtrar" + (" (" + str(ativos) + ")" if ativos else "")
    busca = ('<form class="busca" method="get" action="/empregos/vagas"><input type="search" name="q" value="' + esc(termo)
             + '" placeholder="Buscar por cargo..." aria-label="Buscar por cargo">'
             '<a class="btn-mini" style="margin:0" href="/empregos/filtrar">' + rotulo_f + '</a></form>')
    if vagas:
        n = len(vagas)
        corpo_v = '<p class="contagem">' + str(n) + (' vaga perto de você' if n == 1 else ' vagas perto de você') + '</p>'
        corpo_v += "".join(_card_vaga(v) for v in vagas)
    else:
        corpo_v = ('<div class="card centro"><h2 class="t" style="margin-top:0">Nenhuma vaga encontrada</h2>'
                   '<p class="sub">Não achamos vagas com essas escolhas. Veja vagas mais longe ou tire os filtros.</p>'
                   '<a class="btn pri" href="/acao/dist-any">Ver vagas mais longe</a>'
                   '<a class="btn" href="/acao/limpar-filtros">Tirar filtros</a></div>')
    salvas = ('<a class="btn claro" href="/empregos/salvas">' + ic("bookmark") + ' Vagas salvas (' + str(len(s["salvas"])) + ')</a>')
    nota = '<p class="rodape-nota">Vagas de exemplo, criadas para o protótipo.</p>'
    return pagina(s, "Vagas encontradas", busca + corpo_v + salvas + nota, caminho,
                  topo=("voltar", "/empregos/passo2", "Vagas encontradas"))


def emp_filtrar(s, q, caminho):
    f = s["filtros"]

    def radio(nome, valor, rot, atual):
        return ('<label class="opt grande"><input type="radio" name="' + nome + '" value="' + valor + '"'
                + (" checked" if atual == valor else "") + '><span>' + rot + '</span></label>')
    corpo = ('<h1 class="t">Filtrar vagas</h1><form method="get" action="/acao/filtros">'
             '<label class="rot">Tipo de contrato</label>'
             + radio("contrato", "todos", "Todos", f["contrato"]) + radio("contrato", "CLT", "CLT (carteira assinada)", f["contrato"])
             + radio("contrato", "PJ", "PJ (como empresa)", f["contrato"]) + radio("contrato", "Informal", "Informal", f["contrato"])
             + '<label class="rot">Empresas</label><label class="opt grande"><input type="checkbox" name="verif" value="1"'
             + (" checked" if f["verificadas"] else "") + '><span>Mostrar só empresas verificadas ✓</span></label>'
             '<label class="rot">Ordenar por</label>'
             + radio("ordem", "perto", "Mais perto de casa", f["ordem"]) + radio("ordem", "salario", "Maior salário", f["ordem"])
             + '<button class="btn pri" type="submit">Ver vagas</button>'
             '<a class="btn" href="/acao/limpar-filtros">Tirar filtros</a></form>')
    return pagina(s, "Filtrar vagas", corpo, caminho, topo=("voltar", "/empregos/vagas", "Filtrar"), ferramentas=False)


def _info(icone, rotulo, valor):
    return '<div class="info-l">' + ic(icone) + '<div><small>' + esc(rotulo) + '</small><b>' + esc(valor) + '</b></div></div>'


def emp_detalhe(s, q, caminho, vid):
    v = dados.vaga_por_id(int(vid))
    if v is None:
        return None
    salva = v["id"] in s["salvas"]
    if v["verificado"]:
        selo = '<span class="chip ok">✓ Empresa verificada</span>'
        alerta_emp = ""
    else:
        selo = '<span class="chip aviso">Empresa não verificada</span>'
        alerta_emp = _caixa("atencao", "alert", "<strong>Empresa não verificada.</strong> Confira o nome da empresa e o endereço antes de ir ou de ligar.")
    tel_limpo = "".join(c for c in v["tel"] if c.isdigit())
    corpo = ('<div class="card"><h1 class="t" style="margin:0">' + esc(v["cargo"]) + '</h1><p class="sub" style="margin:.2rem 0 .5rem">'
             + esc(v["empresa"]) + '</p>' + selo
             + _info("pin", "Localização", v["endereco"] + " — " + km(v["km"]) + " km de você")
             + _info("clock", "Horário", v["horario"]) + _info("briefcase", "Contrato", dados.CONTRATOS[v["contrato"]])
             + _info("star", "Salário", v["salario"]) + '</div>' + alerta_emp
             + _caixa("ruim", "alert", 'Nunca pague para conseguir uma vaga. <a href="/golpe">Denuncie se pedirem dinheiro.</a>')
             + '<a class="btn pri" href="tel:' + tel_limpo + '">' + ic("phone") + ' Ligar agora: ' + esc(v["tel"]) + '</a>'
             + '<a class="btn" href="/acao/salvar/' + str(v["id"]) + '">' + ic("bookmark") + (' Vaga salva ✓ (tocar para tirar)' if salva else ' Salvar vaga') + '</a>')
    return pagina(s, "Detalhe da vaga", corpo, caminho, topo=("voltar", s["lista_url"], "Detalhe da vaga"))


def emp_salvas(s, q, caminho):
    vagas = [dados.vaga_por_id(i) for i in s["salvas"]]
    if vagas:
        corpo = '<h1 class="t">Vagas salvas</h1>' + "".join(_card_vaga(v) for v in vagas)
    else:
        corpo = ('<h1 class="t">Vagas salvas</h1><div class="card centro"><p class="sub">Você ainda não salvou nenhuma vaga. '
                 'Toque em "Salvar vaga" na página da vaga.</p><a class="btn pri" href="/empregos/vagas">Ver vagas</a></div>')
    return pagina(s, "Vagas salvas", corpo, caminho, topo=("voltar", s["lista_url"], "Vagas salvas"))


# ----------------------------------------------------------------------------
# Benefícios
# ----------------------------------------------------------------------------
def ben_passo(s, q, caminho, n="1"):
    n = int(n)
    if n < 1 or n > 4:
        return Redirecionar("/beneficios")
    chave, texto, opcoes = dados.PERGUNTAS[n - 1]
    texto = texto.format(nome=dados.PERFIL["nome"])
    volta = "/inicio" if n == 1 else ("/beneficios" if n == 2 else "/beneficios/passo/" + str(n - 1))
    botoes = "".join('<a class="resp" href="/beneficios/responder/' + str(n) + '/' + valor + '"><span>' + esc(rot) + '</span>'
                     + ic("right") + '</a>' for valor, rot in opcoes)
    corpo = ('<div class="chat"><span class="avatar">' + ic("message") + '</span><div class="balao">' + esc(texto) + '</div></div>'
             '<p><button type="button" class="btn-mini" data-ouvir="' + esc(texto) + '">' + ic("volume") + ' Ouvir pergunta</button></p>'
             + botoes + '<p class="centro"><a class="link" href="/beneficios/todos">Ver todos os benefícios, sem responder</a></p>')
    return pagina(s, "Benefícios", corpo, caminho, topo=("voltar", volta, "Benefícios"), progresso=(n, 4, n * 25))


def beneficios_elegiveis(r):
    baixa = r.get("4", "nao_sei") in ("sim", "nao_sei")
    lista = []
    if baixa:
        lista.append("bolsa-familia")
        if r.get("3") == "sim":
            lista.append("bpc")
        lista.append("tarifa-social")
    return lista


def _card_beneficio(slug):
    b = dados.BENEFICIOS[slug]
    return ('<a class="menu-card" href="/beneficios/' + slug + '"><span class="caixa-ico cinza">' + ic("gift") + '</span>'
            '<span class="tx"><strong style="font-size:1.1rem">' + esc(b["nome"]) + ' <span class="chip tag">' + esc(b["tag"])
            + '</span></strong><span class="s">' + esc(b["resumo"]) + '</span></span>' + ic("right") + '</a>')


def ben_resultado(s, q, caminho):
    s["benef_volta"] = "/beneficios/resultado"
    slugs = beneficios_elegiveis(s["respostas"])
    if slugs:
        n = len(slugs)
        topo_box = ('<div class="caixa ok" style="display:block"><h1 class="t" style="font-size:1.25rem;margin:0">🎉 Você pode ter direito a '
                    + str(n) + (' benefício!' if n == 1 else ' benefícios!') + '</h1><div>Toque em cada um para ver como conseguir.</div></div>')
        lista = "".join(_card_beneficio(x) for x in slugs)
    else:
        topo_box = _caixa("info", "alert", "<strong>Pelas suas respostas, não achamos benefícios agora.</strong> Isso não é uma decisão oficial. "
                          "Vá ao CRAS para conferir com uma pessoa.")
        lista = ('<a class="btn pri" href="/beneficios/todos">Ver todos os benefícios</a><a class="btn" href="/cras?v=/beneficios/resultado">Ver o CRAS</a>')
    nota = '<p class="rodape-nota">Resultado de exemplo. Quem decide é o CRAS, na hora do cadastro.</p>'
    return pagina(s, "Seus benefícios", topo_box + lista + '<a class="btn" href="/inicio">Voltar ao início</a>' + nota, caminho,
                  topo=("voltar", "/beneficios/passo/4", "Seus benefícios"))


def ben_todos(s, q, caminho):
    s["benef_volta"] = "/beneficios/todos"
    corpo = ('<h1 class="t">Todos os benefícios</h1><p class="sub">Toque em um para ver como conseguir.</p>'
             + "".join(_card_beneficio(x) for x in dados.BENEFICIOS_ORDEM)
             + '<a class="btn claro" href="/beneficios">Descobrir a quais eu tenho direito</a>')
    return pagina(s, "Todos os benefícios", corpo, caminho, topo=("voltar", "/beneficios", "Benefícios"))


def ben_detalhe(s, q, caminho, slug):
    b = dados.BENEFICIOS.get(slug)
    if b is None:
        return None
    docs = '<ul class="ok">' + "".join('<li>' + ic("check") + '<span>' + esc(d) + '</span></li>' for d in b["docs"]) + '</ul>'
    itens = [("O que é", '<p style="margin:0">' + esc(b["oque"]) + '</p>', True),
             ("Quem pode", '<p style="margin:0">' + esc(b["quem"]) + '</p>', False),
             ("Documentos necessários", docs, False),
             ("Onde ir", '<p style="margin:0">' + esc(b["onde"]) + '</p>', False),
             ("Prazo", '<p style="margin:0">' + esc(b["prazo"]) + '</p>', False)]
    acc = "".join('<details class="acc" name="beneficio"' + (" open" if aberto else "") + '><summary>' + t + ic("right")
                  + '</summary><div class="corpo">' + c + '</div></details>' for t, c, aberto in itens)
    c = dados.CRAS
    corpo = ('<div class="caixa info" style="align-items:center">' + ic("gift") + '<div><strong style="font-size:1.1rem">' + esc(b["nome"])
             + '</strong>' + esc(b["programa"]) + '</div></div>'
             + _caixa("ok", "check-circle", "<strong>Como pedir, em resumo:</strong> " + esc(b["como_pedir"]))
             + acc
             + '<div class="card"><strong>CRAS mais próximo</strong>' + _mapa(c["nome"])
             + '<div>' + esc(c["endereco"]) + '</div><div style="color:var(--mut)">' + esc(c["horario"]) + '</div>'
             '<a class="btn" style="margin-top:.7rem" href="/cras?v=/beneficios/' + slug + '">Ver endereço e telefone</a></div>'
             '<p class="rodape-nota">Informações de exemplo. Confirme no CRAS antes de ir.</p>')
    return pagina(s, b["nome"], corpo, caminho, topo=("voltar", s["benef_volta"], b["nome"]))


# ----------------------------------------------------------------------------
# Avisos
# ----------------------------------------------------------------------------
ICONE_AVISO = {"vagas": "briefcase", "beneficios": "clipboard", "servicos": "landmark"}


def _linha_switch(icone, titulo, sub, ligado, href):
    return ('<a class="card linha-sw" href="' + esc(href) + '" role="switch" aria-checked="' + ("true" if ligado else "false") + '">'
            + (ic(icone) if icone else "") + '<span class="tx"><strong>' + esc(titulo) + '</strong><small>' + esc(sub) + '</small></span>'
            '<span class="est"><span class="sw' + (" on" if ligado else "") + '"></span>' + ("Ligado" if ligado else "Desligado") + '</span></a>')


def avisos(s, q, caminho):
    lista = visiveis(s)
    if lista:
        cartoes = ""
        for a in lista:
            cartoes += ('<a class="card aviso-card' + ("" if a["lido"] else " novo") + '" href="/avisos/abrir/' + str(a["id"]) + '">'
                        '<span class="aviso-ic">' + ic(ICONE_AVISO[a["cat"]]) + '</span><span class="tx"><strong>' + esc(a["titulo"])
                        + '</strong><span>' + esc(a["texto"]) + '</span><div class="q">' + esc(a["quando"]) + '</div></span>'
                        + ('' if a["lido"] else '<span class="ponto" aria-label="Aviso novo"></span>') + '</a>')
        marcar = ('<p style="text-align:right;margin:-.3rem 0 .6rem"><a class="link" href="/acao/avisos-lidos">Marcar todos como lidos</a></p>'
                  if nao_lidos(s) else "")
    else:
        cartoes = '<div class="card centro"><p class="sub" style="margin:0">Você não tem avisos agora.</p></div>'
        marcar = ""
    prefs = "".join(_linha_switch(None, tit, sub, s["prefs"][k], "/acao/pref/" + k) for k, tit, sub in dados.PREFERENCIAS)
    corpo = (marcar + cartoes + '<h2 class="t">Preferências de avisos</h2>' + prefs)
    return pagina(s, "Avisos", corpo, caminho, topo=("marca", "Avisos"), nav="avisos")


# ----------------------------------------------------------------------------
# Ajuda e assistente
# ----------------------------------------------------------------------------
def ajuda(s, q, caminho):
    cartoes = "".join('<a class="resp" href="' + h + '"><span>' + t + '</span>' + ic("right") + '</a>'
                      for h, t in [("/empregos", "Encontrar emprego"), ("/beneficios", "Pedir um benefício"),
                                   ("/golpe", "Denunciar um golpe")])
    faq = "".join('<a class="resp" style="font-size:.98rem" href="/ajuda/pergunta?q=' + quote(f) + '"><span>' + esc(f) + '</span>'
                  + ic("right") + '</a>' for f in dados.FAQ)
    corpo = ('<h1 class="t">O que você precisa?</h1>' + cartoes
             + '<p class="sub" style="margin:1rem 0 .5rem"><b>Ou pergunte ao assistente:</b></p>'
             '<div class="linha-btn"><button type="button" class="btn claro" data-falar="pergunta">' + ic("mic") + ' Falar</button>'
             '<a class="btn claro" href="/ajuda/escrever">' + ic("edit") + ' Escrever</a></div>'
             '<div class="nao-simples"><h2 class="t">Perguntas frequentes</h2>' + faq + '</div>'
             + _caixa("ruim", "alert", "<strong>Cuidado com golpes.</strong> Nunca pague para conseguir vaga ou benefício e nunca passe senhas ou códigos.")
             )
    return pagina(s, "Ajuda", corpo, caminho, topo=("marca", "Ajuda"), nav="ajuda")


def ajuda_escrever(s, q, caminho):
    exemplos = "".join('<a class="chip" style="text-decoration:none;font-size:.85rem;padding:.35rem .6rem;margin-bottom:.4rem" href="/ajuda/pergunta?q='
                       + quote(e) + '">' + esc(e) + '</a>' for e in ["Onde peço o Bolsa Família?", "Quero achar emprego", "Aumentar a letra"])
    corpo = ('<h1 class="t">Qual é a sua dúvida?</h1><p class="sub">Escreva com suas palavras. Eu levo você até o lugar certo.</p>'
             '<form method="get" action="/ajuda/pergunta"><label class="rot" for="pergunta">Sua pergunta</label>'
             '<input type="text" id="pergunta" name="q" placeholder="Digite aqui" autocomplete="off" autofocus>'
             '<div style="height:.8rem"></div><button class="btn pri" type="submit">' + ic("send") + ' Enviar pergunta</button></form>'
             '<button type="button" class="btn claro" data-falar="campo" data-campo="pergunta">' + ic("mic") + ' Falar em vez de escrever</button>'
             '<p class="sub" style="margin:1rem 0 .4rem">Exemplos:</p><div>' + exemplos + '</div>')
    return pagina(s, "Escrever pergunta", corpo, caminho, topo=("voltar", "/ajuda", "Escrever pergunta"))


def ajuda_pergunta(s, q, caminho):
    pergunta = um(q, "q").strip()[:300]
    if not pergunta:
        return Redirecionar("/ajuda/escrever")
    r = assistente.responder(pergunta)
    botoes = '<a class="btn pri" href="' + esc(r["destino"]) + '">' + ic("right") + ' ' + esc(r["rotulo"]) + '</a>'
    if r["destino"] != "/cras":
        botoes += '<a class="btn" href="/cras?v=/ajuda">' + ic("phone") + ' Falar com uma pessoa (CRAS)</a>'
    corpo = ('<div class="chat"><div class="balao eu">' + esc(pergunta) + '</div></div>'
             '<div class="chat"><span class="avatar">' + ic("message") + '</span><div class="balao">' + esc(r["resposta"]) + '</div></div>'
             '<p><button type="button" class="btn-mini" data-ouvir="' + esc(r["resposta"]) + '">' + ic("volume") + ' Ouvir resposta</button></p>'
             + botoes + '<a class="btn claro" href="/ajuda/escrever">Fazer outra pergunta</a>')
    return pagina(s, "Resposta", corpo, caminho, topo=("voltar", "/ajuda", "Resposta"), ferramentas=False)


# ----------------------------------------------------------------------------
# Ajustes (acessibilidade)
# ----------------------------------------------------------------------------
def ajustes(s, q, caminho):
    def tam(chave, rotulo, rem):
        sel = s["letra"] == chave
        return ('<a href="/acao/letra/' + chave + '"' + (' class="sel" aria-current="true"' if sel else '') + '><b style="font-size:'
                + rem + 'rem">A</b>' + rotulo + '</a>')
    letra = ('<div class="card"><strong style="font-size:1.15rem">' + ic("type") + ' Tamanho da letra</strong>'
             '<p class="sub" style="margin:.2rem 0 0">Ajuste para ver melhor o texto</p><div class="tamanhos">'
             + tam("menor", "Menor", "1") + tam("normal", "Padrão", "1.4") + tam("maior", "Maior", "1.9") + '</div>'
             '<div class="exemplo">Exemplo: assim fica o texto do aplicativo.</div></div>')
    corpo = (letra + '<h2 class="t">Cores e leitura</h2>'
             + _linha_switch("contrast", "Alto contraste", "Cores mais fortes para facilitar a leitura", s["contraste"], "/acao/contraste")
             + _linha_switch("volume", "Voz em voz alta", "O app lê o título de cada tela para você", s["voz"], "/acao/voz")
             + _linha_switch("layout", "Modo simples", "Menos opções, letras maiores, mais fácil", s["simples"], "/acao/simples")
             + '<a class="btn" href="/inicio">Voltar ao início</a>')
    return pagina(s, "Acessibilidade", corpo, caminho, topo=("voltar", "/inicio", "Acessibilidade"), nav="ajustes", ferramentas=False)


# ----------------------------------------------------------------------------
# Denunciar golpe, CRAS, erro
# ----------------------------------------------------------------------------
def golpe(s, q, caminho):
    tipos = "".join('<label class="opt grande"><input type="radio" name="tipo" value="' + k + '"' + (" required" if i == 0 else "")
                    + '><span>' + esc(t) + '</span></label>' for i, (k, t) in enumerate(dados.TIPOS_GOLPE))
    dicas = ('<ul class="pontos"><li>Vaga ou benefício de verdade <b>nunca</b> cobra dinheiro.</li>'
             '<li>Ninguém da prefeitura pede <b>senha</b> ou código recebido por mensagem.</li>'
             '<li>Confira o <b>nome da empresa e o endereço</b> antes de ligar ou ir.</li>'
             '<li>Na dúvida, fale com uma pessoa no CRAS.</li></ul>')
    corpo = ('<h1 class="t">Denunciar um golpe</h1>'
             + _caixa("ruim", "shield", "Se alguém pediu dinheiro, senha ou código, conte aqui. Sua denúncia ajuda outras pessoas.")
             + '<form method="post" action="/golpe/enviar"><label class="rot">O que aconteceu?</label>' + tipos
             + '<label class="rot" for="relato">Conte o que aconteceu (se quiser)</label><textarea id="relato" name="relato" maxlength="1000"></textarea>'
             '<button type="button" class="btn claro" style="margin-top:.5rem" data-falar="campo" data-campo="relato">' + ic("mic") + ' Falar em vez de escrever</button>'
             '<label class="rot" for="contato">Telefone, nome da empresa ou link suspeito (se tiver)</label>'
             '<input type="text" id="contato" name="contato" maxlength="200" autocomplete="off"><div style="height:1rem"></div>'
             '<button class="btn pri" type="submit">' + ic("send") + ' Enviar denúncia</button></form>'
             '<h2 class="t">Como saber se é golpe</h2><div class="card">' + dicas + '</div>')
    return pagina(s, "Denunciar um golpe", corpo, caminho, topo=("voltar", "/ajuda", "Denunciar um golpe"))


def golpe_ok(s, q, caminho):
    protocolo = esc(um(q, "p", "—"))
    corpo = ('<div class="centro" style="padding-top:1rem"><span class="caixa-ico verde" style="margin:0 auto 1rem;width:4.5rem;height:4.5rem">'
             + ic("check-circle") + '</span><h1 class="t">Denúncia enviada</h1>'
             '<p class="sub">Obrigado por avisar. Seu número de protocolo é:</p>'
             '<p style="font-size:1.5rem;font-weight:800;letter-spacing:.05em;margin:0 0 1rem">' + protocolo + '</p></div>'
             '<div class="card"><strong>O que fazer agora</strong><ul class="pontos"><li>Não pague nada e não envie senha ou código.</li>'
             '<li>Se já pagou, guarde os comprovantes e procure uma delegacia ou o CRAS.</li>'
             '<li>Bloqueie o número que mandou a mensagem.</li></ul></div>'
             '<a class="btn pri" href="/cras?v=/inicio">' + ic("phone") + ' Falar com uma pessoa (CRAS)</a>'
             '<a class="btn" href="/inicio">Voltar ao início</a>'
             '<p class="rodape-nota">Protótipo: a denúncia fica salva só neste computador.</p>')
    return pagina(s, "Denúncia enviada", corpo, caminho, topo=("voltar", "/inicio", "Denúncia enviada"), ferramentas=False)


def _volta_segura(q, padrao):
    v = um(q, "v")
    return v if (v.startswith("/") and not v.startswith("//") and "\\" not in v and ":" not in v) else padrao


def cras(s, q, caminho):
    c = dados.CRAS
    tel = "".join(ch for ch in c["tel"] if ch.isdigit())
    corpo = ('<h1 class="t">' + esc(c["nome"]) + '</h1>' + _mapa(c["nome"])
             + '<div class="card">' + _info("pin", "Endereço", c["endereco"]) + _info("clock", "Horário", c["horario"])
             + _info("phone", "Telefone", c["tel"]) + _info("landmark", "O que fazem", c["tipo"]) + '</div>'
             '<a class="btn pri" href="tel:' + tel + '">' + ic("phone") + ' Ligar para o CRAS</a>'
             '<p class="rodape-nota">Dados de exemplo para o protótipo.</p>')
    return pagina(s, c["nome"], corpo, caminho, topo=("voltar", _volta_segura(q, "/inicio"), "CRAS mais próximo"))


def erro(s, q, caminho):
    de = _volta_segura({"v": q.get("de", [""])}, "/inicio")
    corpo = ('<div class="centro" style="padding-top:3rem"><span style="color:#9a9a9a">' + ic("x-circle").replace('class="ic ', 'style="width:4rem;height:4rem" class="ic ') + '</span>'
             '<h1 class="t" style="margin-top:1rem">Algo deu errado</h1>'
             '<p class="sub">Não conseguimos carregar o que você pediu. Verifique sua internet e tente novamente.</p></div>'
             '<a class="btn pri" href="/acao/offline/off?next=' + quote(de, safe="") + '">' + ic("refresh") + ' Tentar de novo</a>'
             '<a class="btn" href="/acao/offline/off?next=/inicio">Voltar ao início</a>'
             '<p class="centro"><span class="link" style="text-decoration:underline">Código de erro: ERR_CONNECTION_TIMEOUT</span></p>')
    return pagina(s, "Ops…", corpo, caminho, topo=("voltar", de, "Ops…"), ferramentas=False)


def nao_encontrada(s, caminho):
    corpo = ('<div class="centro" style="padding-top:3rem"><h1 class="t">Página não encontrada</h1>'
             '<p class="sub">Essa tela não existe. Volte ao início.</p><a class="btn pri" href="/inicio">Voltar ao início</a></div>')
    return pagina(s, "Não encontrada", corpo, caminho, ferramentas=False)


def painel_teste(s, q, caminho):
    corpo = ('<h1 class="t">Painel do facilitador</h1><p class="sub">Esta tela não aparece no app. Use entre uma pessoa e outra.</p>'
             '<a class="btn pri" href="/reiniciar">Começar teste com nova pessoa (reinicia tudo)</a>'
             '<a class="btn" href="/acao/novo-aviso">Simular um aviso novo</a>'
             '<a class="btn" href="/acao/offline/' + ("off" if s["offline"] else "on") + '?next=/teste">'
             + ("Voltar ao modo online (agora: offline)" if s["offline"] else "Simular modo offline (agora: online)") + '</a>'
             '<div class="card dash"><strong>Registros</strong><br>Cada tela aberta e cada denúncia ficam salvas na pasta <code>registros</code> '
             '(arquivos .csv), para ajudar a contar toques e tempo.</div>'
             '<a class="btn claro" href="/">Ir para a tela de boas-vindas</a>')
    return pagina(s, "Painel do facilitador", corpo, caminho, ferramentas=False)
