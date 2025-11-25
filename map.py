num1: int
num2: int

# Input only two numbers.
# The split() method will return a list of strings
# by using whitespaces as the delimiter.
num1, num2 = map(int, input('Input two numbers separated by spaces: ').split())

print('\nnum1:', num1, '\nnum2:', num2)

# Enter an infinite amount of numbers.
user_input: str = input(
  'Enter as many numbers as you like separated by spaces:\n'
)

# "1 2 3 four 5".split() -> ['1', '2', '3', 'four', '5']

user_input = user_input.split()

def safe_int_conversion(num_str: str) -> None:
  # Exceptions can rise gracefully.
  try:
    numbers_ints.append(int(num_str))
  except ValueError:
    print('Error: Please make sure that all the inputs are valid integers.')

numbers_ints: list[int] = list(map(safe_int_conversion, user_input))

print('\nnumbers_ints:', numbers_ints)