"""
EXERCISE: CHECK IF PALINDROME

A palindrome is a word, number, phrase, or other sequence of
symbols that reads the same backwards as forwards.

Here are some examples:

Amore, Roma
No 'x' in Nixon
A man, a plan, a canal, Panama!

You have to write a program that determines whether input
by a user is a palindrome or not.

As you see in the examples, the case of the letters, spacing
and punction is ignored.

The output of your program should be "True" if the word, number
or phrase is a palindrome and "False" if that is not the case.
"""


def isPalindrome(str):
	# Suppose the "str" parameter is assigned the 'Amore, Roma'
	# argument.

	# left starts at the first character (A).
	# right starts at the last character (a).
	left, right = 0, len(str) - 1

	# Continue iterating over the string until the pointers
	# meet or cross.
	while left < right:
		# Have both the left and right pointers skip over
		# non-alphanumeric characters.
		if not str[left].isalnum():
			left += 1
			continue
		if not str[right].isalnum():
			right -= 1
			continue

		# Upon a mismatch, immediately return False.
		if str[left].lower() != str[right].lower():
			return False

		# Move the pointers, so that the right one points to the next
		# character to the right, and so that the left one points to
		# the next one to the left.
		left += 1
		right -= 1

	# Given that there were not any mismatches, send a
	# boolean value of True back to where this function
	# was invoked.
	return True

useCases = ['Amore, Roma', 'No \'x\' in Nixon', 'A man, a plan, a canal, Panama!']

for useCase in useCases:
  print(f'isPalindrome({useCase}): {isPalindrome(useCase)}\n')

falseUseCase = 'La Dolce Vita'

print(f'isPalindrome({falseUseCase}): {isPalindrome(falseUseCase)}')