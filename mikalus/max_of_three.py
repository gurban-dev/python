def max_of_three(num1, num2, num3):
  # max() is a built-in function in Python
  # that'll return the largest of three
  # numbers.
  return max(num1, num2, num3)

def get_valid_number():
  while True:
    try:
      return float(input('Input a number: '))
    except ValueError:
      print('Invalid input. Please enter a number.')

# An efficacious way to prompt the end user
# three times for input.
numbers = []
for i in range(3):
  numbers.append(get_valid_number())

print(f'max_of_three({numbers[0]}, {numbers[1]}, {numbers[2]}):\n'
      f'{max_of_three(numbers[0], numbers[1], numbers[3])}')