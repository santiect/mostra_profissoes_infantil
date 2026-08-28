#!/usr/bin/env bash
# Gera o PDF (A4) da folha de atividade a partir do SVG.
set -euo pipefail
cd "$(dirname "$0")"
inkscape pizza_challenge.svg \
  --export-type=pdf \
  --export-filename=pizza_challenge.pdf \
  --export-area-page
echo "Gerado: worksheet/pizza_challenge.pdf"
