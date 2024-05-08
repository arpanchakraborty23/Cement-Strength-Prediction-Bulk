from setuptools import setup,find_packages
from typing import List

Hypen_dot_e='-e .'

def get_requirements(file_path:str)->[List]:
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements=[req.replace('/n','') for req in requirements]

        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)

    return requirements

setup(
    name='Cement-Strength-Prediction',
    version='0.1',
    author='Arpan Chakraborty23',
    author_email='Arpanchakraborty500@gmail.com',
    url='https:\\github.com\{author}\{name}.git',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)