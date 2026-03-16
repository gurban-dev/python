'''
Class variables serve as shared attributes
across all instances/objects of a class,
providing a centralised means for managing
data that is common to the entire class.

On the other hand, instance variables encapsulate
unique characteristics for each object, maintaining
individuality.'''
class Product:
	# A class variable to keep track of the number
	# of products.
	total_products = 0

	# What makes it clear that these are class variables
	# the fact that they are declared outside of the class'
	# constructor method.
	unique_products_count = 0

	product_names = set()

	# The parameterised constructor for this class
	# generates two instance variables upon object
	# creation.

	# The following constructor accepts two parameters:
	# name and price
	def __init__(self, name, price):
		self.name = name
		self.price = price

		# Increment the count of the class variable
		# "total_products" when a new instance is
		# created.
		# Product.total_products = Product.total_products + 1
		Product.total_products += 1

		if self.name not in Product.product_names:
			Product.unique_products_count += 1

			Product.product_names.add(self.name)

	# Selector/Getter
	# def get_total_products(self):
	# 	return Product.total_products

	@classmethod
	def get_total_products(cls):
		return cls.total_products

	def get_unique_products_count(self):
		return Product.unique_products_count
	
	def get_product_names(self):
		return Product.product_names

	def get_name_and_price(self):
		return (f'\nself.name: {self.name}, '
				f'self.price: {self.price}')

# Create three different instances/objects
# of the Product class.
laptop = Product("Laptop", 999.99)

print(f'laptop.get_total_products(): '
      f'{laptop.get_total_products()}')

smartphone = Product("Smartphone", 499.99)
headphones = Product("Headphones", 99.99)

print('\nAfter the Product class has be instantiated three times:')

# Output the class variable that is
# the same for each object.
print(f'laptop.get_total_products(): '
      f'{laptop.get_total_products()}')

print(f'\nsmartphone.get_total_products(): '
      f'{smartphone.get_total_products()}')

print(f'\nheadphones.get_total_products(): '
      f'{headphones.get_total_products()}')

# Output the instance variables
# that are unique to each object.
print(f'\nlaptop.get_name_and_price():'
      f'{laptop.get_name_and_price()}'
      f'\nsmartphone.get_name_and_price():'
      f'{smartphone.get_name_and_price()}'
      f'\nheadphones.get_name_and_price():'
      f'{headphones.get_name_and_price()}')

# Create a product with a duplicate name.
laptop2 = Product("Laptop", 1200.99)

print(f'\nlaptop2.get_name_and_price():'
      f'{laptop2.get_name_and_price()}')

print('\nlaptop.get_unique_products_count():',
			laptop.get_unique_products_count())

print('\nlaptop2.get_product_names():', laptop2.get_product_names())