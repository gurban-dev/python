'''
1. Create a superclass Transport with:
   A constructor that sets a name attribute.

   A generic move() method (default message
   like "Transport is moving").

2. Create at least 3 subclasses of Transport:

   Car: overrides move() with "Car is driving
   on the road."

   Bicycle: overrides move() with "Bicycle is
   pedaling on the bike lane."

   Boat: overrides move() with "Boat is sailing
   through the water."

3. Write a function start_journey(transport) that:

   Accepts any Transport object.

   Calls its move() method.

   Prints the type of transport.

4. In the main() function:

   Create a list of different transport objects.

   Use a loop to call start_journey() on each one.
'''

# Superclass class
class Transport:
  def __init__(self, name):
    self.name = name

  def move(self):
    print(f"{self.name} is moving generically.")

# Subclass
class Car(Transport):
  def move(self):
    print(f"{self.name}: Car is driving on the road.")

# Subclass
class Bicycle(Transport):
  def move(self):
    print(f"{self.name}: Bicycle is pedaling on the bike lane.")

# Subclass
class Boat(Transport):
  def move(self):
    print(f"{self.name}: Boat is sailing through the water.")

# Function demonstrating polymorphism
def start_journey(transport):
  print(
    f"Starting journey with: {transport.__class__.__name__}"
  )

  transport.move()
  print("-" * 40)

def main():
  transports = [
    Car("Toyota Corolla"),
    Bicycle("Mountain Bike"),
    Boat("Sea Ray 320")
  ]

  for vehicle in transports:
    start_journey(vehicle)

main()