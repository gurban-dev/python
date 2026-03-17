# In this example, f-string format specifiers are used to horizontally
# align columns in a table.

# General format syntax used in this example:
# {value:alignment width .precision type}
# Parts after the colon control how the value is displayed.

# E.g.
# {price:>12.2f}
# price  -> value being formatted
# :      -> begins the format specification
# >      -> right alignment
# 12     -> minimum field width (padding spaces are added if needed)
# .2     -> display two digits after the decimal
# f      -> format the value as a decimal (floating-point) number

# Alignment options
# <  -> left align
# >  -> right align
# ^  -> centre align

# width -> minimum number of characters used to display the value
# precision -> number of digits shown after the decimal point (for floats)

# Sales data (product, quantity sold, unit price)
sales = [
    ("Laptop Sleeve", 12, 18.5),
    ("Wireless Mouse", 7, 24.99),
    ("USB-C Cable", 25, 7.45),
]

# Table header
print(f"\n|{'Product':<20}|{'Qty':^8}|{'Unit Price':>12}|{'Total':>12}|")

# Separator line
print("-" * 56)

# Table rows
for product, qty, price in sales:
    total = qty * price

    # :>12.2f -> right-align within 12 characters and display
    # two digits after the decimal point
    print(f"|{product:<20}|{qty:^8}|{price:>12.2f}|{total:>12.2f}|")

# Calculate overall total
grand_total = sum(qty * price for _, qty, price in sales)

print("-" * 56)

# Summary row
print(f"|{'Grand Total':<20}|{'':^8}|{'':>12}|{grand_total:>12.2f}|")