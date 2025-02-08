from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = [r.strip() for r in file.readlines() if r.strip() and r.strip() != "-e ."]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Aman Kumar Gupta',
    author_email='amank8525@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)