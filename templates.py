from pathlib import Path
import os
import logging

list_of_files = [
    '.github/.gitkeeep',
    '.gitignore',
    'config/config.yaml',
    'NoteBook/Eda.ipynb',
    'src/components/__init__.py',
    'src/constant/__init__.py',
    'src/pipline/__init__.py',
    'src/logging/__init__.py',
    'src/utils/__init__.py',
    'src/exception/__init__.py',

    'setup.py',
    'templates/index.html',
    'app.py',
    'requirements.txt',
    'README.md'
]

for fileepath in list_of_files:
    fileepath=Path(fileepath)

    filedir, filename=os.path.split(fileepath)

    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'create dir {filedir} for filename {filename}')

    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(fileepath,'w') as f:
            pass
        
    else:
        logging.info(f' {filename} created')