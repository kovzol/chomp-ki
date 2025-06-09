# Dieser Code muss mit 'python3 setup.py build_ext --inplace' compiliert
# und dann mit 'python3 -c "import chomp"' gestartet werden.

from setuptools import setup
from Cython.Build import cythonize

setup (
    ext_modules = cythonize("chomp.py"),
)
