from dataclasses import dataclass

'''
@dataclass will scan the instance variables that have
explicit type annotations, and will automatically
populate the __init__(), __repr__(), and __eq__()
methods.
'''

@dataclass
class Product:
  name: str
  price: float
  quantity: int = 0

  def total_cost(self) -> float:
    return self.price * self.quantity

# Invokes the __init__() method.
p1 = Product(name='Laptop', price=1000.0, quantity=3)
p2 = Product(name='Laptop', price=1000.0, quantity=3)
p3 = Product(name='Smartphone', price=500.0, quantity=2)

# Invokes the __repr__() method.
print('p1:', p1)

print('p1.total_cost():', p1.total_cost())

# Invokes the __eq__() method.
print('p1 == p2:', p1 == p2)

print('p1 == p3:', p1 == p3)