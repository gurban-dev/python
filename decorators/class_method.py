class Person:
  species = 'Homo sapiens'

  @classmethod
  def get_species(cls):
    print('cls.species:', cls.species)
    return cls.species

person = Person

person.get_species()