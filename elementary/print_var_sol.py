# # Store the customer's given name.
# customer_name = "Alice"

# # Store the main course the customer wants to order.
# main_course = "Spanish seafood paella"

# # Store the quantity of the main course the customer wants
# # to order.
# quantity = 1

# # The main course costed $15.
# # 0.75 is for the 5% sales tax applied to the main course.
# total_cost = 15 + 0.75

# # Print the order message.
# print(f"{customer_name} placed {quantity} order of {main_course}.")

# print(f'\nThe total cost was ${total_cost}.')

#############################

# When prompting the user to input some data inside of an input()
# function, use either a colon (:) or a question mark.
customer_name = input("Please enter your name: ")

main_course = input("What did the customer order? ").lower()

# Add a whitespace (simply a space) character after the colon or
# question mark in an input() function.
amount = input("How much did they buy of it? ").lower()

# Spaces should be placed after commas when passing multiple
# arguments to functions.

# To remove an unnecessary whitespace character between the last
# letter and the period, pass sep="" as an argument.

# sep="" is a keyword argument because the name of the parameter
# 'sep' is included. All this means is pass an empty string ("")
# to this 'sep' parameter to remove the space after each comma
# in the output.
print("\n", customer_name, " placed ", amount, " order of ", main_course, ".", sep="")

# F-string
# print(f"\n{customer_name} placed {amount} order of {main_course}.")