# An f-string (short for formatted string literal) lets you
# insert variables or expressions directly into a string using
# {} (curly braces).

name = "Herodotus"
century = 5

# To create an f-string, place a lowercase f immediately before
# the opening quotation mark.
print(f"The father of history is {name}.\n"
      f"He lived during the {century}th century BC.\n")

# The f tells Python to evaluate any expressions inside {}
# and insert their values into the string before it is printed.
print(f"Next century: {century + 1}th century BC.")

# F-strings automatically convert values such as integers,
# floats, and booleans to strings. This means you do not need
# to call str() yourself.

# F-strings are usually the easiest way to combine text with
# variables. The code closely matches the output, making it
# easier to read and write.

# Without an f-string, the sentence is split into several
# separate pieces.
print("The father of history is " + name + ".\n"
      "He lived during the " + str(century) + "th century BC.\n")

# Another approach is to separate the values with commas.
print("The father of history is ", name, ".\n"
      "He lived during the ", century, "th century BC.\n", sep="")

# Commas separate the arguments passed to print().

# By default, print() places a space between each argument.

# The sep parameter controls the separator that print() places
# between its arguments.

# sep="" changes the separator to an empty string, so no spaces
# are inserted between the arguments.