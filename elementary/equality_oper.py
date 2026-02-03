# Python’s equality operator (==) returns True if the two values
# being compared are considered equal; otherwise, it returns False.

# Python is case sensitive when it comes to comparing
# strings.

# "venice" and "VENICE" are not equal to each other
# because the case of the letter (upper case or lower
# case) matters.
venice_lower_case = "venice"
venice_upper_case = "VENICE"

print('venice_lower_case == venice_upper_case:',
      venice_lower_case == venice_upper_case)

# "1" == 1 evaluates to False because Python first compares
# the data types.

# "1" is a string (text type), while 1 is an integer (numeric type).
# Because strings and numbers belong to different type categories,
# Python does not compare their values and considers them not equal.

# A "\n" (newline escape sequence) forces the output to appear
# one line below.
print("\n\"1\" == 1:", "1" == 1)

# Although 1.0 (float) and 1 (int) are different data types, they both
# fall under Python’s numeric type category, so Python compares their
# values and considers them equal.
print("\n1.0 == 1:", 1.0 == 1)