# The Automobile class holds general data
# about an automobile in inventory.

class Automobile:
	# The __init__() method is explicitly passed arguments
	# for the make, model, mileage, and price. It initialises
	# the data attributes with the values from its parameters.

	def __init__(self, make, model, mileage, price):
		self.make = make
		self.model = model
		self.mileage = mileage
		self.price = price

	# The following methods are mutators for the
	# class's data attributes.

	def set_make(self, make):
		self.make = make

	def set_model(self, model):
		self.model = model

	def set_mileage(self, mileage):
		self.mileage = mileage

	def set_price(self, price):
		self.price = price

	# The following methods are the accessors
	# for the class's data attributes.

	def get_make(self):
		return self.make

	def get_model(self):
		return self.model

	def get_mileage(self):
		return self.mileage

	def get_price(self):
		return self.price


# The Car class represents a car. It is a subclass
# of the Automobile class.
class Car(Automobile):
	# The __init__() method accepts parameters for the
	# car's make, model, mileage, price, and doors.

	def __init__(self, make, model, mileage, price, no_of_doors):
		# Call the superclass' __init__() method and pass
		# the required arguments. Note that we also have
		# to pass "self" as the first argument.
		Automobile.__init__(self, make, model, mileage, price)

		# Initialise the "no_of_doors" attribute.
		self.no_of_doors = no_of_doors

	# The set_no_of_doors() method is the mutator for the
	# "no_of_doors" attribute.
	def set_no_of_doors(self, no_of_doors):
		self.no_of_doors = no_of_doors

	# The get_no_of_doors() method is the accessor for the
	# "no_of_doors" attribute.
	def get_no_of_doors(self):
		return self.no_of_doors

# Notice how only four arguments are explicitly being
# passed. "self" is not explicitly included.
dune_buggy = Automobile(
	make='Meyers',
	model='Manx Classic',
	mileage=8400,
	price=14995
)

'''
Are the following arguments being passed to the Car class'
constructor method positional or keyword arguments?

Answer:
They are keyword arguments because the parameters names are
explicitly being written out in the call to the constructor
method.

In the above constructor method call, for the Automobile class,
the parameter names are not included. That's why the arguments
being passed are positional arguments.
'''

toyota_camry_se_car = Car(
	make='Toyota',
	model='Camry SE',
	mileage=45200,
	price=18750,
	no_of_doors=4
)

# A method that's defined in the child class, but not in the
# parent class, cannot be called on an object of the parent class.
# print('toyota_camry_se_auto.get_no_of_doors():',
# 			toyota_camry_se_auto.get_no_of_doors())

print('toyota_camry_se_car.get_no_of_doors():',
			toyota_camry_se_car.get_no_of_doors())