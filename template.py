import pathlib
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnCloud"

list_of_files = [".github/workflows/.gitkeep", 
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/componets/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/config/__init__.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 "config/config.yaml",
                 "dvc.ymal",
                 "params.ymal"
                 "requirements.txt",
                 "setup.py",
                 "research/trials.ipynb"
                 ]

for file_paths in list_of_files:
    file_paths = Path(file_paths)
    filedir, filename = os.path.split(file_paths)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file: {filename}")
        
    if (not os.path.exists(file_paths)) or (os.path.getsize(file_paths) == 0):
        with open(file_paths, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_paths}")
            
    else:
        logging.info(f"{filename} is  already Created;")            