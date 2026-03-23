"""
In Python, there are no access modifiers like in TypeScript
(public, protected, private). Instead, Python uses naming
conventions to signal direct access rules.

A public variable has no leading underscore.
It can be directly accessed from anywhere.

A protected variable (single leading underscore) can be directly
accessed by the class itself, its subclasses, and from outside
the class.

Keep in mind that although possible, attributes shouldn't be
directly accessed from outside a class.

A private variable (double leading underscore) can be directly
accessed only within the class that defines it. Python enforces
this through name mangling, not through a true restriction.
"""


class Parent:
	def __init__(self):
		self.public_var = "I am public."
		self._protected_var = "I am protected."
		self.__private_var = "I am private."
	
	# The object of the parent class has direct access to
	# all of its instance variables/attributes regardless
	# of the naming convention.
	def access_attributes(self):
		print('Parent sees:')
		print(self.public_var)
		print(self._protected_var)
		print(self.__private_var, '\n')
  

class Child(Parent):
	def access_parent_vars(self):
		print('Child sees:')
		print(self.public_var)
		print(self._protected_var)
		# print(self.__private_var)
		print()

parentObj = Parent()
childObj = Child()

parentObj.access_attributes()

childObj.access_parent_vars()

# The protected instance variable can be directly accessed
# outside of the Parent class without using name mangling.
print('parentObj._protected_var:', parentObj._protected_var)

# However, the same cannot be said of the parentObj's private
# instance variable.
# print('parentObj.__private_var:', parentObj.__private_var)

print('parentObj._Parent__private_var:', parentObj._Parent__private_var)