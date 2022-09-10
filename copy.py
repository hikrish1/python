import os
import shutil
print('Current working directory is \t',os.getcwd())
print('Copying directory')
shutil.copytree("e:\python","d:\py",symlinks=True)
print('Copy done')











