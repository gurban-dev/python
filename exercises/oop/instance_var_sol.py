# Define the Restaurant class.
class Restaurant:
    
    # Constructor method.
    def __init__(self, restaurant_name, cuisine_type):
        # Instance variables.
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Instance method to describe the restaurant.
    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    # Instance method to indicate the restaurant is open.
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")


# Create an instance of the Restaurant class.
restaurant = Restaurant("Cedars of Beirut", "Lebanese")

# Print the two attributes individually.
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Outputs a blank line for readability
print()

# Call the methods.
restaurant.describe_restaurant()
restaurant.open_restaurant()