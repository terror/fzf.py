default:
	just --list

fmt:
  yapf --in-place --recursive .

run *args:
  python3 fzf {{args}}

install *pkg:
  pipenv install {{pkg}} --skip-lock

build: clean
  python3 setup.py sdist && python3 setup.py build

clean:
  rm -rf dist build fzf.py.egg-info

publish:
  twine upload dist/*

lock:
  pipenv lock --pre

install-editable:
  pipenv install -e .

forbid:
	./bin/forbid
