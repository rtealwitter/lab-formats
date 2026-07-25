# lab-formats

Starter code for the **Rosetta Stone (JSON / YAML / TOML / CSV)** lab in *CSCI 40: Computing for the Web*.

![doctests](https://github.com/rtealwitter/lab-formats/actions/workflows/doctests.yaml/badge.svg)

Fork this repository, clone your fork, then fill in the function bodies in
`lab_formats.py` until the doctests pass:

```bash
python -m doctest -v lab_formats.py   # every test OK (silent without -v) means success
```

This lab uses PyYAML (installed by the workflow). `tomllib` is in the standard library on Python 3.11+; on 3.10 or older, also `pip install tomli`.

Push your fork and the **doctests** badge above turns green once every test
passes. Submit your fork's URL on Gradescope, resubmitting until it is 100%.
