# Ajuda Já — protótipo funcional (Python)

Protótipo funcional do aplicativo **Ajuda Já** (serviços da prefeitura para emprego, benefícios e dúvidas),
feito como evolução do protótipo de baixa fidelidade do Figma e ajustado com o que apareceu nos testes de usabilidade.

- Só **Python 3** (testado no 3.13; deve rodar do 3.8 em diante). **Não precisa instalar nada** (nenhum `pip install`).
- Funciona **sem internet**: não baixa fontes, imagens nem bibliotecas.
- Roda em **Windows, Mac e Linux**.

## Como rodar (3 passos)

1. Baixe/clone esta pasta (`git clone ...` ou "Download ZIP" no GitHub).
2. Abra o terminal dentro da pasta e rode:
   - Windows: `python app.py` (se não funcionar, `py app.py`)
   - Mac/Linux: `python3 app.py`
3. O navegador abre sozinho. Se não abrir, entre em **http://localhost:8000** (o endereço certo aparece no terminal).

Para parar: `Ctrl + C` no terminal.

### Opções
| Comando | O que faz |
|---|---|
| `python app.py --rede` | Deixa abrir também no **celular**, no mesmo Wi-Fi (o endereço aparece no terminal). Pode pedir permissão do firewall. |
| `python app.py --porta 9000` | Usa outra porta (se a 8000 estiver ocupada, ele já tenta a próxima sozinho). |
| `python app.py --sem-navegador` | Não abre o navegador automaticamente. |

> Dica: no computador, a tela aparece num "celular" no meio da janela. Para ver como no aparelho de verdade, use o celular com `--rede`
> ou aperte F12 e escolha o modo celular do navegador.

## Como usar nos testes de usabilidade

- Abra **http://localhost:8000/teste** (painel do facilitador, não aparece no app).
  - **Começar teste com nova pessoa**: zera letra, avisos, vagas salvas etc. Use entre uma pessoa e outra.
  - **Simular um aviso novo** e **Simular modo offline**.
- Cada navegador tem a sua própria sessão (guardada na memória). Fechou o programa, tudo zera.
- Na pasta `registros/` (criada sozinha) ficam dois arquivos que abrem no Excel:
  - `navegacao.csv`: cada tela aberta, com data e hora (ajuda a contar toques e tempo).
  - `denuncias.csv`: denúncias de golpe enviadas durante o teste.
  - Essas pastas **não vão para o GitHub** (estão no `.gitignore`), porque podem ter dados dos participantes.

## Mapa das telas (fluxos do Figma)

| Fluxo | Telas |
|---|---|
| A — Empregos | Boas-vindas → Início → Que trabalhos você já fez? → Onde prefere trabalhar? → Procurando vagas → Vagas encontradas → Detalhe da vaga |
| B — Benefícios | Início → Pergunta 1 a 4 → Seus benefícios → Detalhe (Bolsa Família, BPC/LOAS, Tarifa Social) |
| Outras | Avisos · Ajuda (assistente por voz/texto + perguntas frequentes) · Acessibilidade (Ajustes) · Algo deu errado (modo offline) |
| Novas | Filtrar vagas · Vagas salvas · Todos os benefícios · Denunciar um golpe · CRAS (endereço e telefone) |

## O que mudou desde o protótipo de baixa fidelidade (e por quê)

Resultado dos 5 testes: SUS médio **71,5** (A 82,5 · B 77,5 · C 65 · D 92,5 · E 40); **19 de 25** tarefas feitas sem ajuda (76%).
A tarefa pior foi a **T5 (aumentar a letra)**: só 2 de 5 conseguiram sozinhos.

| O que os testes mostraram | O que foi feito no protótipo |
|---|---|
| T5: 4 de 5 demoraram ou erraram para achar "aumentar a letra"; 3 confundiram com o botão de contraste. | Botão **"Letra maior"** em quase todas as telas (e na Início), que funciona na hora. A aba "Perfil" virou **"Ajustes"**. Na tela de acessibilidade, **tamanho da letra** fica separado de **"Cores e leitura"**, e o ícone de "Modo simples" deixou de ser um "T" (parecia letra). |
| C e E: letras pequenas nas vagas; pedem letra maior desde o começo. | Tamanho **padrão aumentado** (agora 19 px). Continua com Menor / Padrão / Maior. |
| E (baixa visão): quer botões maiores e voz que leia a tela. | Botão **"Ouvir tela"** em cada tela; opção **"Voz em voz alta"** (lê o título ao abrir); botões e áreas de toque maiores. |
| C e E: dúvida entre **Benefícios** e **Dúvidas** (T2); "Benefícios é só para quem já recebe?". | **Frase explicativa** em cada botão da Início ("Bolsa Família e outros auxílios"). Em Benefícios, atalho **"Ver todos os benefícios, sem responder"**. No detalhe, caixa verde **"Como pedir, em resumo"** logo no topo. |
| C, D, E: falaram de golpe e de confiar na vaga. | Selo **Verificado / Não verificado** nas vagas, aviso "Nunca pague para conseguir uma vaga", tela **Denunciar um golpe** (também pela Ajuda). |
| B e D: poucas vagas e sem filtros. | **13 vagas** de exemplo, **busca por cargo**, **filtros** (contrato, só verificadas, ordem por distância ou salário) e **vagas salvas**. |
| C, D, E: preferem **falar**; E digita pouco. | Voz no assistente e também no passo "Que trabalhos você já fez?" ("Falar em voz alta"). |
| Figma: modo offline / erro. | "Simular modo offline" mostra a tela **Algo deu errado**, com "Tentar de novo". |

**Ainda não resolvido** (para a próxima rodada): D pediu notificação no celular quando sair vaga nova (aqui os avisos só aparecem dentro do app).

## Limites do protótipo

- Vagas, benefícios, empresas e telefones são **dados de exemplo** (fictícios). Os valores dos benefícios são referências e devem ser confirmados no CRAS.
- **Voz**: usa o navegador. Falar (reconhecimento de voz) funciona no **Chrome/Edge**, em geral precisa de internet e só em `localhost` ou `https`; no celular via `--rede` (http) o microfone costuma ser bloqueado, então use "Escrever". Ouvir (leitura em voz alta) funciona na maioria dos navegadores. Se a voz não funcionar, o app avisa na tela e continua usável.
- O assistente é por **palavras-chave** (sem IA): entende perguntas simples e leva a pessoa até a tela.
- O fluxo de Benefícios segue o Figma (4 perguntas em formato de conversa); o resultado é só uma indicação de exemplo.

## Estrutura dos arquivos

```
app.py          servidor (biblioteca padrão do Python)
rotas.py        endereços, sessões e ações (letra, filtros, avisos, denúncia...)
telas.py        todas as telas
estilo.py       visual (CSS), ícones e o pouco de JavaScript que o navegador exige para voz
dados.py        vagas, benefícios, avisos, CRAS, perguntas (dados de exemplo)
assistente.py   assistente virtual (palavras-chave)
registros/      criada sozinha durante os testes (fora do GitHub)
```

Equipe: Caio Pugliese · Erik Dong · Guilherme Itihara — Universidade Presbiteriana Mackenzie.
