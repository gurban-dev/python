tax_rate = 0.08

def final_price(price):
    """
    Calculate the final price including tax.
    """
    return price * (1 + tax_rate)

# This block runs only if pricing.py is executed directly.
if __name__ == "__main__":
    print("__name__ is:", __name__)

    print("Running pricing.py directly")

    while True:
        try:
            price = float(input("Enter a price: "))

            result = final_price(price)

            print("Final price with tax:", result)

            break
        except ValueError:
            print("Please enter a valid number.")