import sys

print('Before sys.path:', sys.path)

'''
In Python, sys.path is a list that contains the
directories where Python looks for modules when
you import them.

The sys.path.append() function is used to temporarily
add a new directory to this list, allowing Python to
search that directory when attempting to import a module.

Once this program terminates, the directory that was
added, will be removed from the sys.path list.

Python will look in /home/deniz/python/imports/folder1
for modules attempting to be imported, in addition to
the directories already in sys.path.'''
sys.path.append('/home/deniz/python/imports/folder1')

print('\nAfter sys.path:', sys.path)

'''
To remove the warning the following was added to
the settings.json file inside of the python/.vscode
directory:
{
  "python.analysis.extraPaths": [
    "./imports/folder1"
  ]
}
'''

from file1 import get_name

print('\nget_name():', get_name())