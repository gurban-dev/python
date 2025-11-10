string = input('Enter any string: ')

# Compute the number of vowels in the inputted string.
# a, e, i, o, u

# Initialise an accumulator.
vowel_count = 0

vowels = ['a', 'e', 'i', 'o', 'u']

# Iterate through every character of "string".
for ch in string:
  # Check if the current character is a vowel.

  # Method 1:
  # if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':

  # Method 2:
  if ch in vowels:

    # Augmented assignment operator (+=).
    vowel_count += 1

# E.g. aeiou, dry
print('\nvowel_count:', vowel_count)