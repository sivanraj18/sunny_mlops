import os
directories = ['data','src',os.path.join('data','train'),os.path.join('data','test'),
               'notebooks','saved_models']


for dir_ in directories: 
    os.makedirs(dir_,exist_ok = True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass


files = ['dvc.yaml',
         'params.yaml',
         ".gitignore",
         os.path.join('src','__init__.py')
         ]

for files_ in files: 
    with open(files_,"w") as f:
        pass