# The module name is languages.py.

# To use the content defined inside languages.py, import the
# name of the module into this namespace.

# Template for importing specific objects from a module:
# from <module_name> import <object_one>, <object_two>
from languages import french, italian

# Imports the entire module so its members are accessed
# through the module namespace (for example, languages.french).

# A namespace is a container that stores names and the objects
# they refer to. It helps Python organize names and prevents
# conflicts between names in different places.

# Imagine your Python program is a house with many rooms.

# Each room has a name:
# languages room
# math room

# Inside each room are the things that belong there.

# The languages Room contains:
# french
# italian

# The math room contains:
# pi
# sqrt

# When you write:
# import languages

# it's as if you've told Python:
# There's a room in this house called languages.
# I may need to get things from that room.
import languages

print("languages.french:", languages.french, "\n")

# A module is a file containing source code that can be reused
# in other programs.

# Modules help organise code by grouping related variables,
# functions, classes and data into separate files.

# Say hello in French.
print(f"french['hello']: {french['hello']}\n")

# Say hello in Italian.
print(f"italian['hello']: {italian['hello']}")