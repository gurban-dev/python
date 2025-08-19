from animals import *

'''
Create an instance/object of the Mammal class.
"mammal" refers to an object of the Mammal class.

Creating an instance of the Mammal class invokes
its __init__ method.

The argument 'regular mammal' will be assigned
to the "species" parameter visible in the method
signature.'''
animals = Mammal('regular mammal')

# An easy way to distinguish methods and
# functions is that methods must be invoked
# with the "." operator.
animals.show_species()

animals.make_sound()

# Object of the Dog class.
dog = Dog()

dog.show_species()

dog.make_sound()

# Object of the Cat class.
cat = Cat()

cat.show_species()

cat.make_sound()