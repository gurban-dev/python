discount = 10

# Identify the locally and globally defined 'discount' variables
# in this program.

def calculate_total(price):
    discount = 5

    tax_rate = 0.08

    tax = price * tax_rate

    # What is the value of 'discount' here?
    print("Inside calculate_total() discount:", discount)

    final_price = price + tax - discount

    print(f"Total: ${final_price}")

calculate_total(price=100)

# 'discount' is the globally defined variable in this program
# because it's not inside of a block.

# Can 'discount' be accessed here?
print("Outside calculate_total() discount:", discount)

# 'discount' can be accessed anywhere in the program
# after it is defined.