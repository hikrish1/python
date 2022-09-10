#This is example to how to copy os directory using python script
import os
import shutil
print('Current working directory is \t',os.getcwd())
print('Copying directory')
shutil.copytree("e:\python","d:\py",symlinks=True)
print('Copy done')











