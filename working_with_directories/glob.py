# In this example we are iterating over all
# of the spreadsheets in a directory, opening
# them, and finally processing them.

from pathlib import Path

path = Path()

# The "glob" method searches for files
# and directories in the current path.
for file in path.glob('*.py'):
  print('file:', file)

for file in path.glob('*'):
  print('file:', file)

'''
(*) means all files and all directories.
(*.*) means all files only in the current directory.
(*.py) means all py files only in the current directory.
(*.xls) means all xls files only in the current directory.'''