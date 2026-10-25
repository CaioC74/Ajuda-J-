# -*- coding: utf-8 -*-
"""Assistente virtual do Ajuda Já.

É só um "tira-dúvidas" simples: entende a pergunta por palavras-chave e leva a
pessoa até a tela certa. Não faz perguntas sobre a vida da pessoa e não usa IA.
"""
import re
import unicodedata


def normalizar(texto):
    """minúsculas, sem acentos e só letras/números."""
    texto = unicodedata.normalize("NFD", str(texto).lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", " ", texto)


# (nome, palavras-chave [início de palavra], resposta, destino, rótulo do botão)
# A ordem importa: em caso de empate, vale o primeiro.
TOPICOS = [
    ("golpe",
     ["golp", "fraud", "falso", "falsa", "engan", "pagar", "pagamento", "cobranca", "senha",
      "suspeit", "pediram dinheiro", "pedindo dinheiro", "mentira"],
     "Pedir vaga ou benefício é de graça. Se alguém pediu dinheiro, senha ou código, desconfie. Você pode denunciar aqui.",
     "/golpe", "Denunciar um golpe"),
    ("bolsa",
     ["bolsa", "cadunico", "cad unico", "cadastro unico", "cadastr"],
     "Para pedir o Bolsa Família, vá ao CRAS do seu bairro com seus documentos. Eu mostro o passo a passo.",
     "/beneficios/bolsa-familia", "Ver como pedir o Bolsa Família"),
    ("bpc",
     ["bpc", "loas", "idoso", "deficien", "aposenta"],
     "O BPC é para idosos com 65 anos ou mais e para pessoas com deficiência que têm renda baixa. Veja quem pode e como pedir.",
     "/beneficios/bpc", "Ver o BPC"),
    ("tarifa",
     ["luz", "energia", "tarifa", "eletric"],
     "A Tarifa Social dá desconto na conta de luz para famílias de baixa renda.",
     "/beneficios/tarifa-social", "Ver a Tarifa Social"),
    ("beneficio",
     ["benefici", "auxili", "governo", "programa", "direito"],
     "Para saber a quais benefícios você pode ter direito, toque em Benefícios e responda 4 perguntas rápidas. Ou veja a lista completa.",
     "/beneficios", "Ir para Benefícios"),
    ("emprego",
     ["empreg", "vaga", "trabalh", "contrat", "curricul", "servico", "bico"],
     "Para procurar emprego, toque em Empregos. Você escolhe os trabalhos que já fez e a distância, e o app mostra as vagas perto de você.",
     "/empregos", "Ir para Empregos"),
    ("avisos",
     ["avis", "notific", "novidade", "alerta"],
     "Seus avisos ficam na aba Avisos: vagas novas, prazos e novidades do CRAS.",
     "/avisos", "Ver meus avisos"),
    ("ajustes",
     ["letra", "aument", "tamanho", "contrast", "enxerg", "voz", "ouvir", "simples", "pequen", "grande", "leitura"],
     "Para deixar a letra maior, toque em Ajustes. Lá você também liga o alto contraste e a leitura em voz alta.",
     "/ajustes", "Ir para Ajustes"),
    ("cras",
     ["cras", "endereco", "onde fica", "prefeitura", "atendente", "telefone", "atendimento", "pessoa", "humano", "falar com"],
     "O CRAS é o posto da prefeitura que atende de graça. Veja o endereço, o horário e o telefone para falar com uma pessoa.",
     "/cras", "Ver o CRAS"),
    ("salvas",
     ["salv"],
     "As vagas que você salva ficam guardadas em \"Vagas salvas\", dentro de Empregos.",
     "/empregos/salvas", "Ver vagas salvas"),
    ("inicio",
     ["inicio", "comecar", "tela inicial", "voltar"],
     "Para voltar ao começo, toque em Início, no menu de baixo.",
     "/inicio", "Ir para o Início"),
]

NAO_ENTENDI = ("Não entendi muito bem. Tente falar de outro jeito, por exemplo: "
               "\"como peço o Bolsa Família\" ou \"quero achar emprego\". "
               "Se preferir, fale com uma pessoa no CRAS.")


def responder(pergunta):
    """Devolve dict(achou, resposta, destino, rotulo)."""
    texto = normalizar(pergunta).strip()
    palavras = texto.split()
    melhor = None
    melhor_pontos = 0
    for nome, chaves, resposta, destino, rotulo in TOPICOS:
        pontos = 0
        for ch in chaves:
            if " " in ch:
                if ch in texto:
                    pontos += 2
            elif any(p.startswith(ch) for p in palavras):
                pontos += 1
        if pontos > melhor_pontos:
            melhor_pontos = pontos
            melhor = (resposta, destino, rotulo)
    if melhor is None:
        return {"achou": False, "resposta": NAO_ENTENDI, "destino": "/cras", "rotulo": "Falar com uma pessoa (CRAS)"}
    return {"achou": True, "resposta": melhor[0], "destino": melhor[1], "rotulo": melhor[2]}
