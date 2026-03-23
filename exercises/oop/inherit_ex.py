'''
class Animal:
	def speak(self):
		print("The animal makes a sound")


class Dog(Animal):
	def bark(self):
		print("The dog barks")

my_dog = Dog()

my_dog.speak()
my_dog.bark()


1. Which class is the parent class?

2. Which class is the child class?

3. Why is my_dog.speak() allowed even though Dog does
   not define speak()?


Add a new child class called Cat that:
Inherits from Animal.

Has a method called meow() that prints "The cat meows".


Then:
Create a Cat object

Call both speak() and meow()
'''