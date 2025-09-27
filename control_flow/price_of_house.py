# An integer variable.
house_price = 1000000

has_good_credit = True

print(has_good_credit[0])

print(bool(has_good_credit))

if has_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price

# A print statement with an f-string
# passed to it.
print(f"Down payment: ${down_payment}")