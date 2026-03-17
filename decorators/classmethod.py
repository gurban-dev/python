class HomoHeidelbergensis:
  # Class variable
  species_name = 'Homo Heidelbergensis'

  # Here there are actually three methods because
  # the Python interpreter will internally created
  # a constructor for a class if the programmer
  # doesn't write one out.

  @classmethod
  def get_species(cls):
    return cls.species_name

  def get_species_name(self):
    return self.species_name

# Why use @classmethod if the class variable can be accessed
# with an instance method?
# Answer:
# The @classmethod decorator makes it possible for the class
# variable to be accessed without instantiating the class.

class HomoSapiens(HomoHeidelbergensis):
  species_name = 'Homo Sapiens'

# Output: Homo Sapiens
print('HomoSapiens.get_species():', HomoSapiens.get_species())

homoSapiensObj = HomoSapiens()

print('\nhomoSapiensObj.get_species_name():', homoSapiensObj.get_species_name())

# With a class method, an instance of the child class doesn't
# need to be created to access the class variable just as with
# the parent class.
print('\nHomoSapiens.get_species():', HomoSapiens.get_species())