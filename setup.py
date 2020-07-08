from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Cython temp proj app',
    ext_modules=cythonize(
        ["package_b/fib.pyx", "package_b/simple.pyx", "package_a/main.py"],
        annotate=True,
        compiler_directives={'language_level': "3"}
    ),
    zip_safe=True,
)
