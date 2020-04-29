import os
infile = 'design/ui/main.ui'
outfile = 'main.py'
os.system(f'pyuic5 -x {infile} -o {outfile}')