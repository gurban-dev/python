
# Define the Restaurant class.
class Restaurant:

    # Constructor method.
    def __init__(self, restaurant_name, cuisine_type):
        # Two instance variables.
        self.restaurant_name = restaurant_name

        self.cuisine_type = cuisine_type

    # Instance method to describe the restaurant.
    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    # Instance method to indicate the restaurant is open.
    def open_restaurant(self):
        print("\n" + self.restaurant_name + " is now open!")


# Create an instance of the Restaurant class.
restaurant = Restaurant("Cedars of Beirut", "Lebanese")

# Print the two attributes individually.

# Directly accessing instance variable outside of the class is
# discouraged because it can violate data integrity because
# there is no data validation.

# Classes are supposed to control how their data is accessed.
print("restaurant.restaurant_name:", restaurant.restaurant_name)
print("restaurant.cuisine_type:", restaurant.cuisine_type, '\n')

# Call the methods.
restaurant.describe_restaurant()

restaurant.open_restaurant()