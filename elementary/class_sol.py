class Country:
    def __init__(self, name, population):
        self.name = name

        # Note that the population is in millions.
        # E.g. 9.82 means 9.82 million
        self.population = population

    def increase_pop(self, change):
        self.population += change

    def decrease_pop(self, change):
        self.population -= change

    def get_name(self):
        return self.name

    def get_population(self):
        return self.population

greece = Country("Greece", 9.82)

print(f"greece.get_name(): {greece.get_name()}\n\n"
      f"greece.get_population(): {greece.get_population()}")