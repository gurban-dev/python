
# Base/Parent class
class Employee:
	# Class variables/attributes because they are
	# declared outside of the constructor method.
	field = 'Technology'

	no_of_employees = 0

	def __init__(self, full_name, position_name):
		# Instance variables/attributes.
		self.full_name = full_name
		self.position_name = position_name

		# Employee.no_of_employees = Employee.no_of_employees + 1
		Employee.no_of_employees += 1

		print('Employee constructor method invoked.', end='\n\n')

	'''
	@classmethod is called a decorator because it contains
	the @ character.

	Class methods in Python serve the purpose of defining
	operations that are related to the class itself, rather
	than to a specific instance of the class. They are
	distinguished by the @classmethod decorator and take
	the class as their first argument, conventionally named
	cls.

	cls is the conventional name for the first parameter
	of a class method in Python.

	Python automatically passes the class itself (cls)
	as the first argument to class methods.

	It is necessary to pass cls to a class method because
	Python will raise a TypeError when you try to call it
	without cls as the first parameter.'''
	@classmethod
	def get_total_employees(cls):
		# This class method returns the number of Employee
		# instances/objects created.
		return f"cls.no_of_employees: {cls.no_of_employees}\n"

	'''
	The behaviour is tied to the class itself, not a specific instance.

	You don't need self.

	The method works even if no object/instance of this class exists yet.
	'''
	@classmethod
	def print_field_name(cls):
		print(f'cls.field: {cls.field}\n')

	# Remember that a method with the same name will overwrite
	# the previous one written with the same the same name before
	# it.

	# Use this when you need to access both instance and class variables.
	def print_field_name(self):
		print(f'{self.full_name} works in {Employee.field}.\n')

	@staticmethod
	def name_is_valid(employee_name):
		# This static method checks if the employee's
		# full name is valid (non-empty string).
		return f'name_is_valid({employee_name}): ' \
			f'{isinstance(employee_name, str) and len(employee_name.strip()) > 0}\n'


# Derived/child class.
class WebDeveloper(Employee):
	# Class variable/attribute
	field = 'Web Development Team'

# Creating Employee instances/objects.
employee1 = Employee("Al-Khwarizmi", "Algorithm Designer")
employee2 = Employee("Pythagoras", "Senior Software Engineer")

# Calling a class method.
print(Employee.get_total_employees())

# employee1.print_field_name()
employee1.print_field_name()

# Calling a static method.
print(Employee.name_is_valid("  René Descartes   "))

print(Employee.name_is_valid(2))

print(Employee.name_is_valid(""))

WebDeveloper.print_field_name()