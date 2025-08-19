# Base/Parent class
class Employee:
  # Class variables/attributes because they
  # are declared outside of the constructor.
  field = 'Technology'

  no_of_employees = 0

  def __init__(self, full_name, position_name):
    # Instance variables/attributes
    self.full_name = full_name
    self.position_name = position_name

    Employee.no_of_employees += 1

  '''
  @classmethod is called a decorator because it
  contains the @ character.

  cls is the conventional name for the first parameter
  of a class method in Python.

  Python automatically passes the class itself (cls)
  as the first argument to class methods.

  It is necessary to pass cls to a class method
  because Python will raise a TypeError when you
  try to call it without cls as the first parameter.'''
  @classmethod
  def get_total_employees(cls):
    # This class method returns the number
    # of Employee instances created.
    return f"Total employees created: {cls.no_of_employees}"

  @classmethod
  def print_field_name(cls):
    print(f'\ncls.field: {cls.field}\n')

  # Remember that a method with the same name
  # will overwrite the previous one written with
  # the same name before it.
  # def print_field_name():
  #   print(f'\nEmployee.field: {Employee.field}\n')

  @staticmethod
  def name_is_valid(full_name):
    # This static method checks if the given
    # title is valid (non-empty string).
    return isinstance(full_name, str) and len(full_name.strip()) > 0

# Derived/child class
class Manager(Employee):
  # Class variable/attribute
  field = 'Web team'

# Creating Employee instances.
employee1 = Employee("Al-Khwarizmi", "Software Architect")
employee2 = Employee("Pythagoras", "Senior Software Engineer")

# Calling a class method.
print(Employee.get_total_employees())

# Calling a static method.
print(Employee.name_is_valid("René Descartes"))
print(Employee.name_is_valid(""))

Manager.print_field_name()