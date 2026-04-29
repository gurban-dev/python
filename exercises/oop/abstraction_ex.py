"""
Abstraction with a Country Class

Concepts:
Abstraction
Inheritance
Polymorphism

Core Idea:
A base class is like a blueprint. It defines what every country
MUST be able to do, but does not say how to do it.

Your job is to complete the subclasses so they follow the blueprint.

--------------------------------------------------

What You Need to Do:

1. Read the Country class carefully.
2. Complete each subclass by implementing ALL required methods.
3. Run the program and fix any errors.
4. Answer the reflection questions at the bottom.

--------------------------------------------------
"""

from abc import ABC, abstractmethod


class Country(ABC):

    # Initialize name and population.
    def __init__(self, name, population):
        if population <= 0:
            raise ValueError("Population must be greater than zero.")
        self.name = name
        self.population = population

    # Must be implemented in subclasses.
    @abstractmethod
    def get_government_type(self):
        pass

    # Must be implemented in subclasses.
    @abstractmethod
    def calculate_gdp_per_capita(self, gdp):
        pass

    # Must be implemented in subclasses.
    @abstractmethod
    def get_currency(self):
        pass

    # Shared method that uses other methods.
    def describe(self):
        return (
            f"{self.name} has a {self.get_government_type()} "
            f"and uses the {self.get_currency()}."
        )


# -------------------------
# Begin Here
# -------------------------

# TODO:
# Complete this class.
class USA(Country):

    def get_government_type(self):
        # TODO: Return the correct government type.
        pass

    def calculate_gdp_per_capita(self, gdp):
        # TODO: Return GDP per capita.
        pass

    def get_currency(self):
        # TODO: Return the correct currency.
        pass


# TODO:
# Complete this class.
class Japan(Country):

    def get_government_type(self):
        pass

    def calculate_gdp_per_capita(self, gdp):
        pass

    def get_currency(self):
        pass


# TODO:
# Create a NEW country class of your choice.
# Example ideas: India, Brazil, Canada
class YourCountry(Country):

    def get_government_type(self):
        pass

    def calculate_gdp_per_capita(self, gdp):
        pass

    def get_currency(self):
        pass


# -------------------------
# Testing
# -------------------------

# Create objects.
usa = USA("United States", 331_000_000)
japan = Japan("Japan", 125_000_000)
your_country = YourCountry("Your Country", 50_000_000)

countries = [usa, japan, your_country]

gdp_values = {
    "United States": 25_000_000_000_000,
    "Japan": 5_000_000_000_000,
    "Your Country": 1_000_000_000_000
}

for country in countries:
    print(country.describe())

    gdp = gdp_values[country.name]
    print("GDP per person:", country.calculate_gdp_per_capita(gdp))
    print()


# -------------------------
# Try Breaking It
# -------------------------

# 1. Comment out ONE method in a subclass.
#    What error do you get?

# 2. Uncomment this line:
# test = Country("TestLand", 1000)


"""
Reflection Questions:

1. Why are you forced to implement all methods in each subclass?

2. What error happens if you forget one?

3. Why can't you create a Country directly?

4. How does the loop treat all countries the same,
   even though they are different?

5. In your own words, what is abstraction?
"""