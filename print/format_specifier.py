# Floating point number.
total = 100.12345

# A whitespace character is automatically
# appended to the string passed as the first
# argument to the print() function.
print('total:', total)

'''
The print() function automatically appends or
adds a newline escape sequence to the end of
the output.

To change this, add end='' as a second
argument to the print() function.

.2f is a modifier that determines how precise
the outputted value will be by dictating the
number of digits to round to after the decimal.

The modifier is included by adding a colon (:).

Explanation:
The expression {total:.2f} formats the output of
the "total variable.

The curly braces {} are called placeholders and
a variable is placed inside them.

"total" is the variable whose value will be formatted.

: indicates the start of format specification.

.2 specifies that the number should be rounded to
two decimal places.

f indicates that the value is a floating-point number.'''
print(f'total with string formatting: {total:.2f}', end='')