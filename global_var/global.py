# A global variable is created outside all functions.

# It can be accessed by any function in the same program file.

# Create a global variable.
my_value = 10

def show_value():
    # Read the global variable.
    print('my_value:', my_value)

show_value()

print('\nNow let\'s modify a global variable.\n')

# Create another global variable.
number = 0

def main():
    # The global statement tells Python that assignments to 'number'
    # should modify the global variable instead of creating a local one.
    global number

    number = int(input('Enter a number: '))

    show_number()

def show_number():
    print(f'\nThe number you entered is {number}.')

main()