print("Welcome to the Cat Adoption Center!")
print("Here's one of our cutest cats:\n")

print(" /\_/\ ")
print("( o.o )")
print(" > ^ < ")

# The input() function returns a string.
# The assignment operator (=) assigns the value
# returned by input() to the variable "name".
name = input("What would you like to name this cat? ")

print("\nGreat!", name, "is a purr-fect name.")

# The if-statement checks if the length of name is
# more than 10 characters.

# If so, it prints a message telling the user that
# the name must be less than ten characters.

# Note: This does not prevent the end user (the person
# typing in the name) from inputting a name that is
# longer than ten characters.
if len(name) > 10:
  print('Name must be less than ten characters.')
else:
  print('Name is an appropriate size.')