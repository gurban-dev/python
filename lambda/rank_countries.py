class Country:
  def __init__(self, country_name, development_index):
    self.country_name = country_name
    self.development_index = development_index

  # Selector/getter
  def get_development_index(self):
    return self.development_index

switzerland = Country('Switzerland', 0.967)
norway = Country('Norway', 0.966)

south_sudan = Country('South Sudan', 0.381)
somalia = Country('Somalia', 0.380)

countries = [south_sudan, switzerland, norway, somalia]

# "countries" is a Python list.
# Python lists have a method called sort().

# Syntax:
# lamda argument(s): expression

# Sort the Country objects by their
# human development index.

'''
Assigning True to the "reverse" parameter
of the sort() method sorts the Country
objects in ascending order (smallest to
largest) based on their values for the
development_index instance variable.'''
countries.sort(
  key=lambda country: country.development_index, reverse=True)

'''
Without explicitly referencing the "key"
parameter, Python wouldn't know that the
lambda function is meant to be the extractor.

The "extractor" refers to a function that
takes an element from a collection and extracts
a specific value from it, which is then used for
comparison.'''

data_of_countries = list(
  map(lambda country:
      (country.country_name,
      country.development_index), countries)
)

print('data_of_countries:', data_of_countries)