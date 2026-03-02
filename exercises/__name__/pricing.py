tax_rate = 0.08

def final_price(price):
    """
    Calculate the final price including tax.
    """
    return price * (1 + tax_rate)

print("In pricing.py:")

print("__name__:", __name__)

# This block runs only if pricing.py is executed directly.
if __name__ == "__main__":
    print("\nRunning pricing.py directly.\n")

    while True:
        try:
            price = float(input("Enter a price: "))

            final_price = final_price(price)

            print("\nFinal price with tax:", final_price)

            break
        except ValueError:
            print("Please enter a valid number.")
else:
    print("\npricing.py is being imported.")