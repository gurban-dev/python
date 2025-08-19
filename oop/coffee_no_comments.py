class Coffee:
  def __init__(self, bean_type):
    self.bean_type = bean_type

    print('\nCoffee class\' __init__ method invoked.')

    print('\nself.bean_type:', self.bean_type, '\n')

  def get_bean_type(self):
    return self.bean_type
  
  def set_bean_type(self, bean_type):
    self.bean_type = bean_type

    print(f'\nself.bean_type updated to {bean_type}.\n')

bean_types = [
  'Arabica',
  'Robusta',
  'Liberica'
]

# bean_types = ['Arabica', 'Robusta', 'Liberica']

for bean_type in bean_types:
  print(bean_type)

# print(bean_types)

bean_type = input(
  '\nEnter the bean type of your preference\n' \
  'from the above menu: '
)

espresso = Coffee(bean_type)

# espresso = Coffee('arabica')

print('espresso.get_bean_type():', espresso.get_bean_type())

espresso.set_bean_type('robusta')

print('espresso.get_bean_type():', espresso.get_bean_type())