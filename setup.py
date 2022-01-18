import os
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name="fzf.py",
  version="0.0.1",
  author="Liam Scalzulli",
  author_email="liam@scalzulli.com",
  description=("Python bindings for fzf"),
  long_description_content_type="text/markdown",
  license="CC0",
  keywords="lib, bindings",
  url="http://packages.python.org/fzf",
  project_urls={"Source Code": "https://github.com/terror/fzf"},
  packages=find_packages(),
  long_description=read("README.md"),
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Topic :: Software Development :: Libraries",
    "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
  ],
  install_requires=[],
  python_requires=">= 3.9",
)
