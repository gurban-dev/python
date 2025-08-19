birth_year = input('Birth year: ')

print(type(birth_year))

# In python a string cannot be subtracted from
# an integer because it will generate an error.
# age = 2020 - birth_year

# To avoid this error the string returned by the
# input() function must be converted to an integer.
age = 2021 - int(birth_year)

print('type(age):', type(age))

print('age:', age)