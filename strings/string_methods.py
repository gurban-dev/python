course = "Python programming"

# Strings have built-in methods that perform common tasks.
# A method is called using the dot notation.

# Example:
# course.upper()

# upper() returns a new uppercase string.
# The original string is not modified.
print("\ncourse.upper():", course.upper())

# lower() returns a new lowercase string.
print("\ncourse.lower():", course.lower())

# title() capitalizes the first letter of every word.
print("\ncourse.title():", course.title())

# capitalize() only capitalizes the first letter of the string.
print("\ncourse.capitalize():", course.capitalize())

# replace() replaces one substring with another.

# The search is case-sensitive, meaning that changing "Programming" to
# "programming" (or vice versa) will cause the replacement to not occur.
print("\ncourse.replace('p', 'j'):", course.replace("p", "j"))

print("\nOriginal string:", course)