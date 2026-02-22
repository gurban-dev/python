'''
Concepts:
__main__ dunder variable.


Scenario
Imagine that you are working on a small application that calculates
final prices with tax.

This logic needs to be:
Reusable by other parts of the app

Testable by running the file directly

Your goal is to prevent user prompts from running when the file is imported.


Part 1: Create the Files

Create two Python files:

pricing.py - shared pricing logic

checkout.py - main application file


Part 2: Implement pricing.py

In pricing.py:

Define a constant tax rate (for example, 0.08).

Write a function final_price(price) that returns the price including tax.

Print the value of the __name__ variable.

Only if the file is run directly:

Print: "Running pricing.py directly"

Prompt the user for a price

Display the final price using final_price()

When this file is imported, no user input should occur.


Part 3: Implement checkout.py

In checkout.py:

Import pricing

Call final_price() with a hardcoded value (for example, 100)

Print the result


Part 4: Run and Observe

Run:
python pricing.py

Run:
python checkout.py


Reflection Questions

Answer in plain English:

1. Why does pricing.py behave differently when run directly vs imported?

2. What problem does if __name__ == "__main__": prevent?

3. Why is this useful in real applications?
'''