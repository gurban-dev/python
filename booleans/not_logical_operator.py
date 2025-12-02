'''
The not operator takes a Boolean expression as its operand
and reverses its logical value. It reverses the truth of its
operand.

If it is applied to an expression that is true, the operator
returns false. If it is applied to an expression that is false,
the operator returns true.
'''
temperature = 101

'''
First, the expression (temperature > 100) is tested and a value
of either true or false is the result.

Then the not operator is applied to that value. If the expression
(temperature > 100) is true, the not operator returns false.

If the expression (temperature > 100) is false, the not operator
returns true.

The below code is equivalent to asking:
"Is the temperature not greater than 100?"

The parentheses put around the expression temperature > 100 is to
make it clear that the not operator is applied not to the temperature
variable, but to the expression temperature > 100.
'''
if not(temperature > 100):
  print('This is below the maximum temperature.')