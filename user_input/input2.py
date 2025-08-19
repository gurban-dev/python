# Get the end user's name, age, and income.
name = input('What is your name? ')

'''
"60" can be casted as an integer whereas "Dennis"
cannot be. This is why inputting a non-numeric
value and then attempting to to cast it as an
integer generates a ValueError.'''
age = int(input('What is your age? '))

# float() takes the string returned by input(),
# converts it to a floating-point number, and
# finally assigns it to the variable named
# "income".
income = float(input('What is your income? '))

# Display the data.
print('\nHere is the data you entered:',
      '\nName:', name,
      '\nAge:', age,
      '\nIncome:', income)