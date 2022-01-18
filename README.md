### fzf.py

Better Python bindings for the command-line fuzzy-finder
[`fzf`](https://github.com/junegunn/fzf).

### Installation

```bash
pip install fzf.py
```

### Usage

`fzf.py` can be used as a class instance or a function decorator.

```python
from fzf import Fzf, fzf
```

As a class instance:

```python
chooser = Fzf()
choices = chooser.prompt([1, 2, 3])
```

As a function decorator:

```python
@fzf()
def example():
  return [1, 2, 3]

choices = example()
```
