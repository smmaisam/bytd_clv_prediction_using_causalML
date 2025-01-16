from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    hyphen_e_dot = '-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements


setup (
    
    name = "bytd_clv_prediction_using_causalML",  # Project name
    version = "0.0.1", # Package version
    author = "smmaisam", # Author name
    author_email = "muhammad.maisam@hotmail.com", # Author email
    
    package_dir ={"": "src"}, # Base directory for the source code
    packages = find_packages(where="src"),  # Finds all subpackages under "src"
    
    install_requires = get_requirements('requirements.txt') # Required packages
)