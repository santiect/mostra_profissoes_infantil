# mostra_profissoes_infantil

Atividade de 5 minutos para apresentar a profissão de professor/cientista da
computação em uma mostra de profissões para crianças de 6 a 10 anos.

O tema é um desafio disfarçado: Luigi tem uma pizzaria e precisa entregar uma
pizza para cada um de seus 5 amigos, saindo da pizzaria, visitando cada casa
uma única vez e voltando — sem deixar as pizzas esfriarem. É o Problema do
Caixeiro Viajante (TSP), sem nomear como tal. Os tempos entre as casas foram
escolhidos de propósito para que a estratégia "vá sempre para o amigo mais
próximo" **não** seja a mais rápida, e para que a rota ótima não seja apenas
o contorno óbvio do desenho — evidenciando por que precisamos de matemática
e computadores para resolver problemas assim.

O personagem "Luigi" desta atividade é um mascote-chef **original**, criado
para este projeto — não tem relação com nenhum personagem de terceiros.

## Conteúdo

- `tsp/` — código Python com os dados do desafio e os geradores de imagem.
  - `data.py` — nós e tempos entre eles (fonte única de verdade).
  - `layout.py` — posições 2D da folha impressa (A4, retrato).
  - `make_slide_graph.py` — posições 2D do grafo usado na apresentação
    (paisagem, compacto) e gera `assets/challenge_graph.svg`.
  - `label_layout.py` — posiciona os rótulos de tempo sempre em cima da
    própria linha, longe de outros rótulos, de cruzamentos entre linhas e
    dos nomes/pizzaria (evita ambiguidade sobre a qual aresta um número
    pertence).
  - `solve_tsp.py` — compara o guloso (vizinho mais próximo) com o ótimo
    (busca exaustiva).
  - `make_worksheet.py` — gera `worksheet/pizza_challenge.svg` (folha para
    imprimir) e contém os desenhos (casinhas, pizzaria, mascote).
  - `make_solution_svg.py` — gera `assets/optimal_tour.svg` (rota ótima
    animável, usada no slide final).
  - `make_luigi.py` — gera `assets/luigi.svg` (mascote isolado, usado nos
    slides).
- `worksheet/` — a folha de atividade em A4, para imprimir e distribuir às
  crianças (fundo branco, pensada para gastar pouca tinta).
- `assets/` — imagens usadas na apresentação: SVGs gerados (`challenge_graph.svg`,
  `optimal_tour.svg`, `luigi.svg`), a foto/logo da ECT-UFRN (`predio_ect.jpeg`,
  `logo_ect.png`) e o KaTeX (`katex/`, vendorizado localmente).
- `index.html` — a apresentação (6 slides animados), pronta para o GitHub
  Pages. Usa o KaTeX local (`assets/katex/`) para renderizar a formulação
  matemática; nenhuma outra dependência externa é usada.

## Como usar

Rodar o solver (mostra o resultado do guloso vs. o ótimo no terminal):

```bash
cd tsp && python3 solve_tsp.py
```

Regerar as imagens (folha de atividade, grafo do slide e rota ótima), caso
os tempos do desafio sejam alterados em `tsp/data.py`:

```bash
cd tsp
python3 make_worksheet.py
python3 make_slide_graph.py
python3 make_solution_svg.py
python3 make_luigi.py
```

Gerar o PDF (A4) da folha de atividade a partir do SVG (requer `inkscape`):

```bash
worksheet/generate_pdf.sh
```

## Publicar no GitHub Pages

O `index.html` está na raiz do repositório. Basta habilitar o GitHub Pages
apontando para a branch `main` e a pasta raiz (`/`) em
`Settings → Pages` do repositório. A URL publicada abrirá direto na
apresentação.

Para testar localmente antes de publicar (necessário para os `fetch` dos
SVGs funcionarem, já que não funcionam em `file://`):

```bash
python3 -m http.server 8420
# depois abra http://localhost:8420/index.html
```
