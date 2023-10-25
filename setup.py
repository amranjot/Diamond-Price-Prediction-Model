from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path:str)->List[str]:
    
    requirements = [] 
    with open(file_path,"r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements
    
    

# Setup The Project
setup(
    
    name = "Diamond Price Prediction",
    version = 0.01,
    author = "Ranjot",
    author_email = "iamranjot0001@gmail.com",
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
      
)