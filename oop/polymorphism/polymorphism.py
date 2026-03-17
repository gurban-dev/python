'''
Polymorphism is the ability of an instance of a class to
take more than one form.

A class is a blueprint that defines the data and behaviour
encapsulated or grouped together in a single unit.

An instance of a class is an actual object created from
that blueprint.
'''

# Sometimes a superclass is also called a parent
# class or a base class.

# Superclass class
class Transport:
  # Constructor method.
  def __init__(self, name):
    self.name = name

    # "\n" is a newline escape sequence.
    print(f'Transport constructor:\nself.name: {self.name}\n')

  def move(self):
    print(f"{self.name} is moving generically.")

# Sometimes a subclass is also referred to as a child
# class or a derived class.

# Subclass
class Car(Transport):
  # The move() method in the subclass overwrites the
  # move() method in the superclass.

  # What would happen if the following move() method
  # was commented out and the program was run again?
  def move(self):
    print(f"{self.name}: The car is driving along the road.")

# Subclass
class Bicycle(Transport):
  def move(self):
    print(f"{self.name}: The bicycle is being pedaled along the bike lane.")

# Subclass
class Boat(Transport):
  def move(self):
    print(f"{self.name}: The boat is sailing across the water.")

# Function demonstrating polymorphism.
def start_journey(transport):
  print(
    f"Starting journey with: {transport.__class__.__name__}"
  )

  # Think about which move() method will be invoked.
  transport.move()

  print("-" * 55)

def main():
  # List data structure.
  vehicles = [
    Car("Toyota Corolla"),
    Bicycle("Mountain Bike"),
    Boat("Sea Ray 320")
  ]

  # Keep in mind that when the Car, Bicycle, and Boat
  # objects are created, the Transport class' constructor
  # or __init__() method is being invoked.

  # Which move() method is being invoked for each of
  # these objects?

  for vehicle in vehicles:
    # Pass each object in 'vehicles' as an argument
    # to the start_journey() function.
    start_journey(vehicle)

main()