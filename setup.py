from setuptools import find_packages, setup
from typing import List

def get_requiremnts(file_path : str)-> List[str]:
    '''
    this function will give the requiremnts of txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n" ,"") for req in requirements]

setup(
    name="ml-projects",
    version="0.0.1",
    author="Lokesh",
    author_email="lokeshnagasaitungala79@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "seaborn"
    ]
)