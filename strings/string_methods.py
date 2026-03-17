course = "  Python programming  "

'''
String functions can be seen by typing the name
of a string variable followed by a dot. These
functions are called methods because they are
specific to a particular object. In this case,
the object is a string.'''

# Type "course." on the next line, but remove it when
# finished explaining.

# Remember that everything in Python is an object.
# Objects have functions called methods that can be
# accessed with the dot notation.

# upper() returns a new string converted to uppercase
# letters, so the original is not affected.
print('\ncourse.upper():', course.upper())

# Similarly, the lower() returns a new string converted
# to lowercase letters, without affecting the original.
print('\ncourse.lower():', course.lower())

# title() returns a new string where the first letter of
# every word is capitalised.
print('\ncourse.title():', course.title())

# strip() removes any whitespace characters at the beginning
# and end of a string which is useful when receiving input
# from the end user.
print('\ncourse.strip():', course.strip())

# rstrip() will only remove the whitespace characters from
# the right side or the end of a string.
print('\ncourse.rstrip():', course.rstrip())

# On the flip side, lstrip() only removes whitespace characters
# from the left side or the beginning of a string.
print('\ncourse.lstrip():', course.lstrip())

# The find() method is constructive for identifying
# the index of the first occurence of a certain
# character or sequence of characters in a string.
print('\ncourse.find(\'o\'):', course.find('o'))

'''
E.g.

Declared string:
          0123456789012345678901
course = "  Python programming  "

Sequence of characters/substring to locate: og

course.find('og') returns 11 because the substring
'og' begins on the eleventh index whereas the first
occurence of 'o' can be found on the sixth index.
'''
print('\ncourse.find(\'og\'):', course.find('og'))

'''
Due to Python being a case-sensitive programming language,
passing 'Pro' as an argument to the find() method rather
than 'pro' will make the find() method return -1 because
it is unable to find the substring 'Pro' in the string
variable "course".'''
print('\ncourse.find(\'pro\'):', course.find('pro'))

print('\ncourse.find(\'Pro\'):', course.find('Pro'))

'''
Keep in mind that in Python, zero is the first index
in strings as well as data structures like lists and
tuples. A more concise way to say this is Python uses
zero-based indexing.

If a list data structure was storing 100 elements/items,
the index of the last element/item in the list would be 99.

If you encounter the term "indice" instead of "index",
remember that these terms refer to the same concept which
makes them interchangeable. The same applies to the terms
"indexes" and "indices".
'''

# replace() will replace a character or a sequence of
# characters with something else. This is also
# case-sensitive.
print('\ncourse.replace(\'p\', \'j\'):', course.replace('p', 'j'))

# Returns True if a specific sequence of characters
# is found in a string. Otherwise, returns False.
print(f'\n\'pro\' in course: {'pro' in course}')

# Since the substring 'swift' is not in the
# "course" string variable, True is returned.
print(f'\n\'swift\' not in course: {'swift' not in course}')

'''
Since the substring "ython" is inside the string
variable "course", the following assertion is
False because it states that "ython" is not in
the "course" variable.'''
print(f'\n\'ython\' not in course: {'ython' not in course}')