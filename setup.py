from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='aoc',
    version='0.1.0',
    description='My python solutions to AoC 2020',
    long_description=readme,
    author='Rui Marques',
    author_email='mail@ruimarques.xy',
    url='https://github.com/ruifm/aoc',
    license=license,
    packages=find_packages(exclude=('tests', 'inputs'))
)
