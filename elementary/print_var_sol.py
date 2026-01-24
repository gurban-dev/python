# Store the customer's given name.
customer_name = "Alice"

# Store the main course the customer wants to order.
main_course = "Spanish seafood paella"

# Store the quantity of the main course the customer wants
# to order.
quantity = 1

# The main course costed $15.
# 0.75 is for the 5% sales tax applied to the main course.
total_cost = 15 + 0.75

# Print the order message.
print(f"{customer_name} placed {quantity} order of {main_course}.")

print(f'\nThe total cost was ${total_cost}.')