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
    Product.total_products += 1

  # Selector/Getter
  def get_total_products(self):
    return Product.total_products

  def get_name_and_price(self):
    return (f'\nself.name: {self.name}, '
            f'self.price: {self.price}\n')

# Create three different instances/objects
# of the Product class.
product1 = Product("Laptop", 999.99)
product2 = Product("Smartphone", 499.99)
product3 = Product("Headphones", 99.99)

# Output the class variable that
# is the same for each object.
print(f'product1.get_total_products(): '
      f'{product1.get_total_products()}')

print(f'\nproduct2.get_total_products(): '
      f'{product2.get_total_products()}')

print(f'\nproduct3.get_total_products(): '
      f'{product3.get_total_products()}')

# Output the instance variables
# that are unique to each object.
print(f'\nproduct1.get_name_and_price():'
      f'{product1.get_name_and_price()}'
      f'\nproduct2.get_name_and_price():'
      f'{product2.get_name_and_price()}'
      f'\nproduct3.get_name_and_price():'
      f'{product3.get_name_and_price()}')