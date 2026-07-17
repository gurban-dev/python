# The module name is languages.py.

# To use the content defined inside languages.py, import the
# name of the module into this namespace.

# Template for importing specific objects from a module:
# from <module_name> import <object_one>, <object_two>
from languages import english, french

# A module is a file containing source code that can be reused
# in other programs.

# Modules help organise code by grouping related variables,
# functions, classes and data into separate files.

# Say hello in English.
print(f"english['hello']: {english['hello']}\n")

# Say hello in French.
print(f"french['hello']: {french['hello']}")