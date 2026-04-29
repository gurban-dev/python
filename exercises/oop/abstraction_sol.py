# Import abstract base class tools from the standard library.
from abc import ABC, abstractmethod


# Define an abstract base class that represents a generic country.
class Country(ABC):

    # Initialize name and population.
    # Raise an error if population is not valid.
    def __init__(self, name, population):
        if population <= 0:
            raise ValueError("Population must be greater than zero.")
        self.name = name
        self.population = population

    # Require subclasses to define government type.
    @abstractmethod
    def get_government_type(self):
        pass

    # Require subclasses to calculate GDP per capita.
    @abstractmethod
    def calculate_gdp_per_capita(self, gdp):
        pass

    # Require subclasses to define currency.
    @abstractmethod
    def get_currency(self):
        pass

    # Provide a shared method that uses subclass implementations.
    def describe(self):
        return (
            f"{self.name} has a {self.get_government_type()} "
            f"and uses the {self.get_currency()}."
        )


# Define the United States class.
class USA(Country):

    # Return the government type of the USA.
    def get_government_type(self):
        return "Federal Republic"

    # Calculate GDP per capita using a simple formula.
    def calculate_gdp_per_capita(self, gdp):
        return gdp / self.population

    # Return the currency used in the USA.
    def get_currency(self):
        return "US Dollar"


# Define the Japan class.
class Japan(Country):

    # Return the government type of Japan.
    def get_government_type(self):
        return "Constitutional Monarchy"

    # Calculate GDP per capita.
    def calculate_gdp_per_capita(self, gdp):
        return gdp / self.population

    # Return the currency used in Japan.
    def get_currency(self):
        return "Japanese Yen"


# Define a custom country.
class YourCountry(Country):

    # Return the government type of the custom country.
    def get_government_type(self):
        return "Democracy"

    # Calculate GDP per capita.
    def calculate_gdp_per_capita(self, gdp):
        return gdp / self.population

    # Return the currency of the custom country.
    def get_currency(self):
        return "Custom Currency"


# Create instances of each country.
usa = USA("United States", 331_000_000)
japan = Japan("Japan", 125_000_000)
your_country = YourCountry("Your Country", 50_000_000)


# Store all country objects in a list.
countries = [usa, japan, your_country]


# Define GDP values for each country.
gdp_values = {
    "United States": 25_000_000_000_000,
    "Japan": 5_000_000_000_000,
    "Your Country": 1_000_000_000_000
}


# Loop through each country and display information.
for country in countries:

    # Print a description using shared method.
    print(country.describe())

    # Look up GDP and calculate per capita value.
    gdp = gdp_values[country.name]
    result = country.calculate_gdp_per_capita(gdp)

    # Print the result.
    print("GDP per person:", result)
    print()