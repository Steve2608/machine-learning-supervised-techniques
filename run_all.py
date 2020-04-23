from glob import iglob
from shutil import move
from subprocess import call


for file in sorted(iglob('*/*.ipynb')):
    call(f'jupyter-nbconvert {file} --execute --ExecutePreprocessor.timeout=-1 --to notebook'.split(' '))
    new_name = file[:-len('.ipynb')] + '.nbconvert.ipynb'
    move(new_name, file)
    call(f'jupyter-nbconvert {file} --to html'.split(' '))