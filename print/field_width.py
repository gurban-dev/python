'''
The format specifier can also include a minimum field
width, which is the minimum number of spaces that should
be used to display the value. The following example prints
a number in a field that is 12 spaces wide because of 12
preceding the comma:
'''
print('The number is', format(12345.6789, '12,.2f'))

# Without the field width:
print('The number is', format(12345.6789, ',.2f'))

# Field width without the comma.
print('The number is', format(12345.6789, '12.2f'))

'''
If a value is too large to fit in the specified field
width, the field is automatically enlarged to
accommodate the value.

In the next example, two spaces were specified for
the field width, but the number 12,345.68 uses
nine spaces on the screen.
'''
print('The number is', format(12345.6789, '2,.2f'), '\n')

# Field widths can help when you need
# to print numbers aligned in columns.

# The objective is to display the following floating-point
# numbers in a column with their decimal points aligned.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Display each number in a field of 7 spaces with 2 decimal
# places.
print(format(num1, '7.2f'))

print(format(num2, '7.2f'))

print(format(num3, '7.2f'))

print(format(num4, '7.2f'))

print(format(num5, '7.2f'))

print(format(num6, '7.2f'))