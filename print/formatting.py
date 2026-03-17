'''
When a floating-point number is displayed by the
print() function, it can appear with up to twelve
significant digits.
'''
amount_due = 5000.0

# Using one forward slash for division
# is called float divsion while using
# two is called integer/floor division.

# Float division: The monthly payment is 416.6666666666667
# Integer/floor division: The monthly payment is 416.0
monthly_payment = amount_due / 12.0

print('The monthly payment is', monthly_payment)

'''
The built-in format() function, requires two arguments:
A numeric value and a format specifier.

The format specifier is a string that contains special
characters specifying how the numeric value should be
formatted.

The format specifier is '.2f' in this case.

The .2 specifies the precision. It indicates that we want
to round the number to two decimal places.

The f specifies that the data type of the number we are
formatting is a floating-point number.
'''
print('\nThe monthly payment is', format(monthly_payment, '.2f'))

# format(monthly_payment, '.2f') will return
# a formatted string as specified.
monthly_payment_formatted = format(monthly_payment, '.2f')

# Validate the data type of the
# "monthly_payment_formatted"
# variable.
print('\ntype(monthly_payment_formatted):', type(monthly_payment_formatted))

print(f'\nmonthly_payment_formatted: {monthly_payment_formatted}')

# Cast the "monthly_payment_formatted"
# variable as a float, so that arithmetic
# operations can be performed on it.
sum = float(monthly_payment_formatted) + 100

print(f'\nsum: {sum}')

# Round the floating-point number by specifying
# a precision of one decimal place.
print('\nThe monthly payment is', format(monthly_payment, '.1f'))

'''
If you prefer to display floating-point numbers in
scientific notation, you can use the letter e or
the letter E instead of f.
'''

# Output: 1.234568e+04
print('\nformat(12345.6789, \'e\'):', format(12345.6789, 'e'))

# Output: 1.23e+04 which means 1.23 x 10^4 -> 12345.
print(f"\nformat(12345.6789, \'.2e\'): {format(12345.6789, '.2e')}")

'''
The number is displayed with the letter e indicating the
exponent.

If you use uppercase E in the format specifier, the result
will contain a capital E indicating the exponent.

Double check:
A capital E simply makes the number more identifiable
inside of a passage.
'''
print('\nformat(12345.6789, \'.2E\'):', format(12345.6789, '.2E'))

'''
If you want the number to be formatted with comma
separators, you can insert a comma into the format
specifier.
'''
print(f"\nformat(12345.6789, ',.2f'): {format(12345.6789, ',.2f')}")

print('\nformat(123456789.456, \',.2f\'):', format(123456789.456, ',.2f'))

print(f"\nformat(12345.6789, ',f'): {format(12345.6789, ',f')}")

# At runtime, monthly_pay it should be
# determined that "monthly_pay" is of
# the float data type.
monthly_pay = 5000.0

# annual_pay = 5000.0 * 12 -> 60000.0
annual_pay = monthly_pay * 12

# sep='' will remove the default whitespace
# character that is inserted at the end of
# the string because of the comma.
print('\nYour annual pay is $',
      format(annual_pay, ',.2f'),
      sep='')

'''
Instead of using f as the type designator, you can
use the % symbol to format a floating-point number
as a percentage. The % symbol causes the number to
be multiplied by 100 and displayed with a % sign
following it.

The % symbol will take the floating-point number
passed as the first argument to the format()
function and will represent it as a percentage.'''
print('\nformat(0.5, \'%\'):', format(0.5, '%'))

# To truncate or to make the output shorter by cutting
# off the fractional or decimal part, set the precision
# to 0.
print(f"\nformat(0.5, '.0%'): {format(0.5, '.0%')}")

'''
The format() function can format integers. There are two
differences to keep in mind when writing a format
specifier that will be used to format an integer:

You use d as the type designator.
You cannot specify precision.
'''
print('\nformat(123456, \'d\'):', format(123456, 'd'))

# The number 123456 is printed with a comma separator.
print(f"\nformat(123456, ',d'): {format(123456, ',d')}")

# Learn how to format large numbers:
# 123 456

# An empty string literal:
# ''

# A whitespace character:
# ' '

# Output: 123 456
print(f"\nformat(123456, ',d').replace(',', ' '): \
       {format(123456, ',d').replace(',', ' ')}")