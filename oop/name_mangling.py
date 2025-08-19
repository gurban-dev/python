class Foo:
  __a = 2

  def __init__(self):
    self.__b = 1

F = Foo()

# F.__a = 3

# print(F.__a)

print(F._Foo__b)
