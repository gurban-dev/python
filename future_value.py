"""
Suppose you want to deposit a certain amount of money into a savings account
and leave it alone to draw interest for the next 10 years. At the end of 10
years, you would like to have $10,000 in the account. How much do you need
to deposit today to make that happen? You can use the following formula to
find out:

The terms in the formula are as follows:
P is the present value, or the amount that you need to deposit today.
F is the future value that you want in the account. (In this case, F is $10,000.)
r is the annual interest rate.
n is the number of years that you plan to let the money sit in the account.
"""

"""
Algorithm

Inputs:
A desired future numerical value that the customer would
like to have in their savings account.
An annual interest rate entered as a decimal.
The number of years the money will appreciate in the account.

Output:
The amount of money needed to deposit today for the sake
of accumulate the desired future numerical value in the
savings account after ten years.

1. Get the desired future value.
2. Get the annual interest rate in decimal format.
3. Get the number of years that the money will sit in the account.
4. Calculate the amount that will have to be deposited.
5. Display the result of the calculation in step 4.
"""

# Get the desired future value.
future_value = float(input('Enter the desired future value: '))

# Get the annual interest rate.
rate = float(
  input(
  '\nEnter the annual interest rate in decimal\n'
  'format (4 should be inputted as 0.04): ')
)

# Get the number of years that the money will appreciate.
years = int(input('\nEnter the number of years the money will grow: '))

# Calculate the amount needed to deposit.

# P = F / (1+r)^n
present_value = future_value / (1.0 + rate) ** years

# Display the amount needed to deposit.

"""
{:.2f} is a string called a format specifier that
specifies how the numeric value should be formatted.

The .2 specifies the precision. It indicates that
we want to round the number to two decimal places.

The f specifies that the data type of the number
we are formatting is a floating-point number.
"""
print(f'\nYou will need to deposit this amount: {present_value:.2f}')