from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list:
    """This function will return the list of requirements"""
    with open(file_path) as file:
        requirements = file.readlines()
    list_requirements = [req.strip() for req in requirements if req.strip()]

    if HYPHEN_E_DOT in list_requirements:
        list_requirements.remove(HYPHEN_E_DOT)
    
    return list_requirements

setup(
    name='ml-project',
    version='0.0.1',
    author='Anusha',
    author_email='anushavirri@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)