"""
5 is implicitly or automatically casted as a float (5.0).
The "my_number" variable will be assigned 10.0 and will be
of the float data type because 5 is being multiplied by a
float.

Implicitly in this context means that the casting of 5 to
a float is occuring behind the scenes."""
my_number = 5 * 2.0

print(f'type(my_number): {type(my_number)}')

"""
The float to int and int to float conversions below are
occuring explicitly because the int() and float()
functions are being utilised.

"fvalue" is explicitly being cast as an integer because
"fvalue" is being passed as an argument to the int()
function.

This is explicit due to the conversion occuring in the open
with int() as opposed to behind the scenes.
"""
fvalue = 2.6
ivalue = int(fvalue)

ivalue = 2
fvalue = float(ivalue)

'''
Re-assigning a value of a different data type
to the same variable is legal in Python and
forces the data type of the variable to change.'''
age = '100'

age = 100