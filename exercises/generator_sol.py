def fibonacci():
    current_num = 0

    next_num = 1

    while True:
        yield current_num

        current_num, next_num = next_num, current_num + next_num
        
quantity = int(input("How many numbers of the fibonacci sequence would you like to print?\n"))

print("\nThe first", quantity, "fibonacci numbers:")

fib = fibonacci()

for i in range(quantity):
    print(next(fib), end=" ")
print()