# The .strip() method removes leading and trailing
# whitespace characters from a string.
string = input('Enter any string: ').strip()

# Obtain the first character in the string with indexing.
abbreviation = string[0] + "."

for i in range(1, len(string), 1):
  # Check if the current character in "string" is a
  # whitespace character.
  if string[i] == " ":
    abbreviation += f"{string[i+1]}."

# E.g.
# United States
print('\nabbreviation:', abbreviation)