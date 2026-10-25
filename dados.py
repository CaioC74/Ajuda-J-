# -*- coding: utf-8 -*-
"""Dados de exemplo do protótipo Ajuda Já.

Tudo aqui é fictício (empresas, endereços e telefones) e serve só para o
protótipo funcionar sem banco de dados e sem internet.
"""

PERFIL = {"nome": "Visitante", "bairro": "Vila Madalena, São Paulo"}

# (chave, rótulo mostrado no passo 1 de "Buscar emprego") - mesma ordem do Figma
AREAS = [
    ("cuidador", "Cuidador(a)"),
    ("diarista", "Diarista"),
    ("cozinheiro", "Cozinheiro(a)"),
    ("seguranca", "Segurança"),
    ("porteiro", "Porteiro(a)"),
    ("limpeza", "Auxiliar limpeza"),
    ("jardineiro", "Jardineiro(a)"),
    ("motorista", "Motorista"),
    ("costureira", "Costureira(o)"),
    ("pedreiro", "Pedreiro(a)"),
]
AREAS_CHAVES = [a[0] for a in AREAS]

# Palavras que o reconhecimento de voz usa para marcar cada trabalho
CHAVES_AREA = {
    "cuidador": "cuidador cuidadora idoso idosos cuidar",
    "diarista": "diarista faxina faxineira",
    "cozinheiro": "cozinheiro cozinheira cozinha cozinhar",
    "seguranca": "seguranca vigilante",
    "porteiro": "porteiro porteira portaria",
    "limpeza": "limpeza limpar",
    "jardineiro": "jardineiro jardineira jardim",
    "motorista": "motorista dirigir",
    "costureira": "costureira costureiro costura",
    "pedreiro": "pedreiro obra construcao",
}

CONTRATOS = {
    "CLT": "CLT — com carteira assinada",
    "PJ": "PJ — como empresa, sem carteira assinada",
    "Informal": "Informal — sem carteira assinada",
}

VAGAS = [
    {"id": 1, "cargo": "Auxiliar de limpeza", "empresa": "Condomínio Jardins", "area": "limpeza",
     "km": 0.8, "contrato": "CLT", "verificado": True, "endereco": "R. das Flores, 120",
     "horario": "Segunda a sábado, 7h às 15h", "salario": "R$ 1.412,00 + vale-transporte",
     "sal_curto": "R$ 1.412,00", "salario_num": 1412, "tel": "(11) 3333-4444"},
    {"id": 2, "cargo": "Cuidadora de idosos", "empresa": "Cuidar Bem LTDA", "area": "cuidador",
     "km": 1.2, "contrato": "PJ", "verificado": True, "endereco": "Av. Rio Branco, 450",
     "horario": "Segunda a sexta, 8h às 17h", "salario": "R$ 1.800,00 por mês",
     "sal_curto": "R$ 1.800,00", "salario_num": 1800, "tel": "(11) 3333-5521"},
    {"id": 3, "cargo": "Diarista", "empresa": "App Faxina Fácil", "area": "diarista",
     "km": 2.4, "contrato": "Informal", "verificado": False, "endereco": "Endereço não informado",
     "horario": "Dias combinados com o cliente", "salario": "R$ 150,00 por dia",
     "sal_curto": "R$ 150,00 por dia", "salario_num": 150, "tel": "(11) 3333-7788"},
    {"id": 4, "cargo": "Auxiliar de cozinha", "empresa": "Restaurante Sabor", "area": "cozinheiro",
     "km": 3.1, "contrato": "CLT", "verificado": True, "endereco": "Rua Girassol, 88",
     "horario": "Terça a domingo, 10h às 18h", "salario": "R$ 1.500,00 + refeição",
     "sal_curto": "R$ 1.500,00", "salario_num": 1500, "tel": "(11) 3333-9012"},
    {"id": 5, "cargo": "Porteiro", "empresa": "Edifício Aurora", "area": "porteiro",
     "km": 1.5, "contrato": "CLT", "verificado": True, "endereco": "R. Aspicuelta, 300",
     "horario": "Escala 12x36, período noturno", "salario": "R$ 1.650,00 + vale-transporte",
     "sal_curto": "R$ 1.650,00", "salario_num": 1650, "tel": "(11) 3333-2210"},
    {"id": 6, "cargo": "Segurança", "empresa": "Mercado Bom Preço", "area": "seguranca",
     "km": 2.0, "contrato": "CLT", "verificado": True, "endereco": "Av. Pompeia, 1200",
     "horario": "Escala 12x36", "salario": "R$ 1.800,00 + vale-alimentação",
     "sal_curto": "R$ 1.800,00", "salario_num": 1800, "tel": "(11) 3333-6644"},
    {"id": 7, "cargo": "Auxiliar de limpeza", "empresa": "Escola Municipal Sol Nascente", "area": "limpeza",
     "km": 2.2, "contrato": "CLT", "verificado": True, "endereco": "Rua Harmonia, 410",
     "horario": "Segunda a sexta, 6h às 14h", "salario": "R$ 1.412,00 + vale-transporte",
     "sal_curto": "R$ 1.412,00", "salario_num": 1412, "tel": "(11) 3333-1180"},
    {"id": 8, "cargo": "Cozinheira", "empresa": "Padaria Pão Quente", "area": "cozinheiro",
     "km": 1.9, "contrato": "CLT", "verificado": True, "endereco": "R. Fradique Coutinho, 77",
     "horario": "Segunda a sábado, 5h às 13h", "salario": "R$ 1.700,00 + café da manhã",
     "sal_curto": "R$ 1.700,00", "salario_num": 1700, "tel": "(11) 3333-3095"},
    {"id": 9, "cargo": "Jardineiro", "empresa": "Condomínio Bosque Verde", "area": "jardineiro",
     "km": 4.2, "contrato": "CLT", "verificado": True, "endereco": "Rua das Acácias, 900",
     "horario": "Segunda a sexta, 7h às 16h", "salario": "R$ 1.550,00 + vale-transporte",
     "sal_curto": "R$ 1.550,00", "salario_num": 1550, "tel": "(11) 3333-8120"},
    {"id": 10, "cargo": "Costureira", "empresa": "Ateliê Costura Viva", "area": "costureira",
     "km": 3.5, "contrato": "Informal", "verificado": False, "endereco": "Rua Mourato Coelho, 640",
     "horario": "Segunda a sexta, 9h às 17h", "salario": "R$ 100,00 por dia",
     "sal_curto": "R$ 100,00 por dia", "salario_num": 100, "tel": "(11) 3333-4719"},
    {"id": 11, "cargo": "Cuidador(a) de idosos", "empresa": "Casa de Repouso Vida Longa", "area": "cuidador",
     "km": 4.8, "contrato": "CLT", "verificado": True, "endereco": "Av. Brasil, 2050",
     "horario": "Escala 12x36", "salario": "R$ 1.900,00 + vale-transporte",
     "sal_curto": "R$ 1.900,00", "salario_num": 1900, "tel": "(11) 3333-5307"},
    {"id": 12, "cargo": "Pedreiro", "empresa": "Construtora Alicerce", "area": "pedreiro",
     "km": 5.5, "contrato": "PJ", "verificado": True, "endereco": "Rua da Obra, 15",
     "horario": "Segunda a sexta, 7h às 16h", "salario": "R$ 2.400,00 por mês",
     "sal_curto": "R$ 2.400,00", "salario_num": 2400, "tel": "(11) 3333-9966"},
    {"id": 13, "cargo": "Motorista", "empresa": "Transportes Lima", "area": "motorista",
     "km": 6.8, "contrato": "CLT", "verificado": True, "endereco": "Av. dos Estados, 3300",
     "horario": "Segunda a sábado, 6h às 15h", "salario": "R$ 2.600,00 + vale-alimentação",
     "sal_curto": "R$ 2.600,00", "salario_num": 2600, "tel": "(11) 3333-7041"},
]


def vaga_por_id(vid):
    for v in VAGAS:
        if v["id"] == vid:
            return v
    return None


CRAS = {
    "nome": "CRAS Vila Madalena",
    "endereco": "Rua Girassol, 215 — Vila Madalena, São Paulo",
    "horario": "Segunda a sexta, 8h às 17h",
    "tel": "(11) 3333-0150",
    "tipo": "Atendimento social, CadÚnico e orientação sobre benefícios. É grátis.",
}

# ordem de exibição
BENEFICIOS_ORDEM = ["bolsa-familia", "bpc", "tarifa-social"]

BENEFICIOS = {
    "bolsa-familia": {
        "nome": "Bolsa Família",
        "tag": "Renda",
        "resumo": "Transferência de renda para famílias de baixa renda",
        "programa": "Programa Federal — Transferência de Renda",
        "como_pedir": "Vá ao CRAS do seu bairro com seus documentos e peça a inscrição no CadÚnico. É grátis.",
        "oque": "O Bolsa Família é um programa do governo federal que repassa dinheiro todo mês para famílias em situação de pobreza.",
        "quem": "Famílias com renda baixa por pessoa (valor de referência: até R$ 218 por mês para cada pessoa da casa) que estejam inscritas no Cadastro Único (CadÚnico). Quem tem crianças e jovens na casa recebe um valor a mais.",
        "docs": [
            "CPF ou título de eleitor de quem vai fazer o cadastro",
            "Documento com foto (RG ou CNH)",
            "Comprovante de endereço",
            "CPF ou certidão de nascimento de cada pessoa da casa",
            "Comprovante de matrícula escolar das crianças (se tiver)",
        ],
        "onde": "No CRAS do seu bairro ou em outro posto de atendimento do CadÚnico. Leve os documentos. O atendimento é gratuito.",
        "prazo": "O cadastro novo pode ser feito o ano todo. Quem já recebe precisa atualizar os dados a cada 2 anos — neste ano, até 30/09.",
    },
    "bpc": {
        "nome": "BPC / LOAS",
        "tag": "Assistência",
        "resumo": "Benefício de Prestação Continuada para idosos e pessoas com deficiência",
        "programa": "Programa Federal — Assistência Social",
        "como_pedir": "Ligue para o 135 ou use o Meu INSS para marcar o pedido. O CRAS ajuda a fazer o cadastro. É grátis.",
        "oque": "O BPC paga 1 salário mínimo por mês a idosos e a pessoas com deficiência que têm renda muito baixa. Não é aposentadoria.",
        "quem": "Idosos com 65 anos ou mais, ou pessoas com deficiência de qualquer idade, cuja renda por pessoa da casa seja de até 1/4 do salário mínimo. É preciso estar no CadÚnico.",
        "docs": [
            "Documento com foto (RG ou CNH) e CPF",
            "Comprovante de endereço",
            "CadÚnico atualizado",
            "Laudo médico (no caso de pessoa com deficiência)",
        ],
        "onde": "Peça o atendimento pelo telefone 135 ou no aplicativo Meu INSS. O CRAS ajuda com o CadÚnico e com os papéis.",
        "prazo": "O pedido pode ser feito o ano todo. A resposta pode levar algumas semanas.",
    },
    "tarifa-social": {
        "nome": "Tarifa Social de Energia",
        "tag": "Utilidade",
        "resumo": "Desconto na conta de luz",
        "programa": "Programa Federal — Desconto na conta de luz",
        "como_pedir": "Ligue para a empresa de energia (o telefone está na sua conta de luz) ou peça no CRAS. É grátis.",
        "oque": "A Tarifa Social dá desconto na conta de luz para famílias de baixa renda.",
        "quem": "Famílias inscritas no CadÚnico com renda de até meio salário mínimo por pessoa, ou que recebem o BPC.",
        "docs": [
            "CPF de quem é o titular da conta de luz",
            "Número do CadÚnico (NIS)",
            "Uma conta de luz recente",
        ],
        "onde": "Na empresa de energia que atende a sua casa (o telefone fica na conta de luz) ou no CRAS.",
        "prazo": "O pedido pode ser feito o ano todo.",
    },
}

# Perguntas do fluxo "Benefícios" (4 passos). (chave de resposta, texto, opções)
PERGUNTAS = [
    ("1", "Olá, Vou te ajudar a descobrir quais benefícios você pode ter direito. Você mora sozinho(a)?",
     [("sim", "Sim, moro sozinho(a)"), ("nao", "Não, moro com família")]),
    ("2", "Tem crianças ou adolescentes (até 17 anos) morando com você?",
     [("sim", "Sim, tenho"), ("nao", "Não tenho")]),
    ("3", "Alguém da sua casa tem 65 anos ou mais, ou tem alguma deficiência?",
     [("sim", "Sim, tem"), ("nao", "Não tem")]),
    ("4", "A renda da sua casa é baixa? Por exemplo: até meio salário mínimo para cada pessoa.",
     [("sim", "Sim, é baixa"), ("nao_sei", "Não sei"), ("nao", "Não, não é baixa")]),
]

# Avisos (notificações) de exemplo. cat: vagas | beneficios | servicos
AVISOS = [
    {"id": 1, "cat": "vagas", "titulo": "Nova vaga próxima!", "texto": "Auxiliar de limpeza — 0,8 km de você",
     "quando": "Hoje, 09:14", "lido": False, "destino": "/empregos/vaga/1"},
    {"id": 2, "cat": "beneficios", "titulo": "Bolsa Família: prazo se encerrando", "texto": "Atualize seu cadastro até dia 30/09",
     "quando": "Ontem, 15:30", "lido": False, "destino": "/beneficios/bolsa-familia"},
    {"id": 3, "cat": "servicos", "titulo": "CRAS abrirá amanhã às 8h", "texto": "Atendimento especial para CadÚnico",
     "quando": "18/09, 10:00", "lido": True, "destino": "/cras"},
    {"id": 4, "cat": "vagas", "titulo": "Sua vaga foi visualizada", "texto": "Cuidadora de idosos — Cuidar Bem",
     "quando": "17/09, 14:22", "lido": True, "destino": "/empregos/vaga/2"},
]

PREFERENCIAS = [
    ("vagas", "Vagas novas", "Avisar quando sair vaga perto de você"),
    ("beneficios", "Benefícios", "Prazos e novidades dos auxílios"),
    ("servicos", "CRAS e serviços", "Horários e atendimentos especiais"),
]

FAQ = [
    "Como faço para me cadastrar no Bolsa Família?",
    "Como busco emprego pelo app?",
    "Como denunciar um golpe?",
    "Como deixar a letra maior?",
]

TIPOS_GOLPE = [
    ("dinheiro", "Pediram dinheiro para conseguir uma vaga ou benefício"),
    ("whatsapp", "Recebi mensagem falsa (WhatsApp, SMS ou e-mail)"),
    ("senha", "Pediram minha senha ou um código"),
    ("ligacao", "Recebi uma ligação suspeita"),
    ("outro", "Outro problema"),
]
