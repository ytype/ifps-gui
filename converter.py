import os
infile = 'window.ui'
outfile = 'main.py'
os.system(f'pyuic5 -x {infile} -o {outfile}')