from functools import wraps
from shutil import which
from subprocess import check_output
from typing import List, Any

class Fzf:
  PROG = 'fzf'

  def __init__(self) -> None:
    if (path := which(Fzf.PROG)) is None:
      raise SystemError(f'{Fzf.PROG} is not installed on $PATH.')
    self.path = path

  def prompt(self, input: List[Any], **opts) -> List[str]:
    return check_output([
      self.path,
      ' '.join(
        list(
          map(
            lambda key: f'--{key.replace("_", "-")}'
            if isinstance(opts[key], bool) else
            f'--{key.replace("_", "-")}={opts[key]}',
            opts.keys()
          )
        )
      )
    ], input=str.encode('\n'.join(list(map(str, input))))).decode('utf-8').strip().split('\n')

def fzf(**opts):
  def f(func):
    @wraps(func)
    def g(*args, **kwargs):
      return Fzf().prompt(func(*args, **kwargs), **opts)
    return g
  return f
