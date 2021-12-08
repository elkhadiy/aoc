from setuptools import setup, find_packages
from aoc import __version__

install_requires = [
    "numpy",
    "scipy",
    "pandas",
    "llvmlite",
    "numba",
]

setup(
    name="aoc",
    version=__version__,
    description="AoC utils",
    author="elk",
    packages=find_packages(exclude=["2021"]),
    install_requires=install_requires
)