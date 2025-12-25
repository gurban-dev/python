# Python is case sensitive when it comes to comparing
# strings.

# "venice" and "VENICE" are not equal to each other
# because the case of the letter (upper case or lower
# case) matters.
venice_lower_case = "venice"
venice_upper_case = "VENICE"

print('venice_lower_case == venice_upper_case:',
      venice_lower_case == venice_upper_case)

# "1" == 1 evaluates to False because Python first
# compares the data types.

# It determines that "1" is a string (text), while 1 is
# an integer (number), and values of different types
# are not considered equal.
print("\n\"1\" == 1:", "1" == 1)

# Although 1.0 (flot) and 1 (int) are different data types,
# they are both numeric types, so Python compares their
# values and considers them to be equal.
print("\n1.0 == 1:", 1.0 == 1)