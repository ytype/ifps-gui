import os
infile = 'design/ui/main-v0.1.ui'
outfile = 'main-v0.1.py'
os.system(f'pyuic5 -x {infile} -o {outfile}')