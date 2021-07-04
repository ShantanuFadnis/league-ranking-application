from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup (
    name="league-ranking-application",
    version="1.0.0",
    description="A CLI application to calculate ranking table of a given league data",
    long_description=long_description,
    author="Shantanu Fadnis",
    package_dir={"": "src"},
    packages=find_packages("src", exclude="tests"),
)