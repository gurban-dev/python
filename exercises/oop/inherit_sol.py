class Animal:
	def speak(self):
		print("The animal makes a sound")


class Dog(Animal):
	def bark(self):
		print("The dog barks")


class Cat(Animal):
	def meow(self):
		print("The cat meows")


# Create objects.
my_dog = Dog()
my_cat = Cat()

# Call inherited method.
my_dog.speak()
my_cat.speak()

# Call child-specific methods.
my_dog.bark()
my_cat.meow()