from pathlib import Path
# "Path" is a class.
# If the first letter of what you are importing is 
# capitalised, that indicates that you are importing a class.

# Absolute path (if you wanted to start from the root of a hard disk) 
# (Example of an absolute path for linux: /usr/local/bin)

# Relative path (if you wanted to reference the ecommerce 
# directory in a project, you would use a relative path)

path = Path("emails") # A "Path" object. If we don't pass an argument here, 
# it will reference the current directory.

print('path.exists():', path.exists()) 
# If the directory passed as an argument on line 12 exists, path.exists() will return True,
# otherwise, it will return False.

print('path.mkdir():', path.mkdir()) # Creates the directory specified.
print('path.rmdir():', path.rmdir()) # Removes a directory specified.