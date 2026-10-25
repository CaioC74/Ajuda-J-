# Ajuda Já — protótipo funcional (Python)

Protótipo funcional do aplicativo **Ajuda Já**, feito como evolução do protótipo de baixa fidelidade do Figma e ajustado com o que apareceu nos testes de usabilidade.

- Só **Python**
- Funciona **sem internet**: não baixa fontes, imagens nem bibliotecas.
- Roda em **Windows, Mac e Linux**.

## Como rodar (3 passos)

1. Baixe/clone esta pasta.
2. Abra o terminal dentro da pasta e rode:
   - Windows: `python app.py`
   - Mac/Linux: `python3 app.py`
3. O navegador abre sozinho. Se não abrir, entre em **http://localhost:8000** (o endereço certo aparece no terminal).

Para parar: `Ctrl + C` no terminal.

### Opções
| Comando    | O que faz |
|---   |---|
| `python app.py --rede` | Deixa abrir também no **celular**, no mesmo Wi-Fi (o endereço aparece no terminal). Pode pedir permissão do firewall. |
| `python app.py --porta 9000` | Usa outra porta (se a 8000 estiver ocupada, ele já tenta a próxima sozinho). |
| `python app.py --sem-navegador`    | Não abre o navegador automaticamente. |

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


## Limites do protótipo

- Vagas, benefícios, empresas e telefones são **dados fictícios**. Os valores dos benefícios são referências e devem ser confirmados no CRAS.
- **Voz**: usa o navegador. Reconhecimento de voz funciona no **Chrome/Edge**, em geral precisa de internet e só em `localhost` ou `https`; . Se a voz não funcionar, o app avisa na tela e continua usável.
- O assistente entende perguntas simples e leva a pessoa até a tela.

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
