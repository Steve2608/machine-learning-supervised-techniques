"""
Executes all notebooks and stores them as html
"""
import glob
import shutil
import subprocess

from tqdm import tqdm


for path in tqdm(sorted(glob.iglob('*/*.ipynb')), desc='Source files', smoothing=0):
    # execute to temp notebook
    subprocess.run(['jupyter-nbconvert', path, '--execute', '--ExecutePreprocessor.timeout=-1', '--to', 'notebook'])
    # overwrite old notebook
    shutil.move(path[:-len('.ipynb')] + '.nbconvert.ipynb', path)
    # save html as well
    subprocess.run(['jupyter-nbconvert', path, '--to', 'html'])
