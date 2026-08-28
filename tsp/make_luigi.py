"""Gera assets/luigi.svg: o mascote (chef de pizzaria, personagem original,
sem relacao com nenhum personagem de terceiros) usado na folha e nos slides."""
import os

from make_worksheet import luigi_character

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "luigi.svg")

if __name__ == "__main__":
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 340" '
        'width="240" height="340">'
        + luigi_character(120, 155) +
        '</svg>'
    )
    out_path = os.path.abspath(OUT_PATH)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Escrito: {out_path}")
