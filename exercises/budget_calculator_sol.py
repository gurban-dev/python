# According to Python's PEP 8 style guide, two blank lines should
# appear before function and class definitions that are written
# directly in the file (not inside another function or class).

# This improves readability and helps developers quickly identify
# where functions and classes begin when visually scanning a file.


def compute_savings(income=None, expenses=None):
    if not income:
        income = int(input("Please input monthly income: "))

    if not expenses:
        expenses = int(input("\nPlease input expenses: "))

    savings = income - expenses
       
    if savings < 1:
        print("\nYou didn't save anything.")
    else:
        print(f"\nYou saved {savings} this month.")

    # Note how if a value is not explicitly returned by a
    # user-defined function, the default value returned is
    # None.

    # Use a return statement when the program must return
    # from a function while also sending a value back to
    # where the function was invoked.
    return savings

savings = compute_savings()

print("\nsavings:", savings)

compute_savings(income=100, expenses=50)