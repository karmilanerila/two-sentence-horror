# Two-Sentence Horror

A make.fun bounty entry: a program that writes one original horror story of exactly two sentences (198 characters) to `/output/entry.txt`.

> Every night before bed I count the chairs in my kitchen: four, always four, because I live alone. Tonight there were five, and the fifth was pulled out, as if someone had only just stood up from it.

## How it works

`main.py` writes the fixed story text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with mode 0644. Deterministic — no randomness, no network, the same output on every run.

## Run it

```sh
python3 main.py
```
