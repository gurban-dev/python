class Circle:
  def __init__(self, radius):
    # Access modifiers do not exist in Python
    # because the "radius" instance variable
    # can still be accessed outside of its class.

    # However, an instance variables with a leading
    # underscore should be treated as private. Meaning
    # that they should not be accessed outside of the
    # class they belong to.
    self._radius = radius

  @property
  def radius(self):
    """Get the radius of the circle."""

    print('self._radius():', self._radius)

    return self._radius
  
  @property
  def diameter(self):
    """Get the diameter of the circle."""
    print('self.radius() * 2:', self._radius * 2)

    return self._radius * 2

  @radius.setter
  def radius(self, value):
    """Mutate the radius of the circle."""

    if value > 0:
      self._radius = value
      print('Radius was mutated.')
    else:
      raise ValueError("Radius must be positive.")

  @radius.deleter
  def radius(self):
    """
    Delete the self._radius instance variable
    of the circle.
    """

    print('self._radius instance variable was deleted.')    

    del self._radius

# Instantiate an object of the Circle class.
c = Circle(5)

# Select the radius.
c.radius

# Select the diameter.
c.diameter

# Mutate the radius.
c.radius = 10

c.radius

c.diameter

del c.radius

c.radius