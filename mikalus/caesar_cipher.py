# Assume all letters are capital/upper case.
def caesar_cipher(text, offset):
	encoded_text = ''

	# Find the current position of the current character.
	# Find the index of the first occurence of the substring 'A'.

	for char in text:
		# On each iteration, append the new character (english_alphabet[new_position]).

		# ord(char) returns the ASCII decimal of the current character.

		# Full list of ASCII Decimals/Codes:
		# https://www.ascii-code.com/

		# Ensure that the Caesar cipher operates exclusively on letters.
		if 65 <= ord(char) <= 90:
			'''
			E.g.
			Suppose char = 'X' and offset = 3.

			new_ascii = ord('A') + (ord('X') - ord('A') + 3) % 26

			new_ascii = 65 + (88 - 65 + 3) % 26

			new_ascii = 65 + (26) % 26

			new_ascii = 65 + 0

			new_ascii = 65

			The ASCII value of 'A' is 65, and 'Z' is 90. Subtracting ord('A')
			from any uppercase letter's ASCII value converts it into a range
			of 0 to 25, which corresponds to the positions of letters in the
			alphabet (e.g., 'A' becomes 0, 'B' becomes 1, ..., 'Z' becomes 25).
			
			This zero-based index allows straightforward operations like modular
			arithmetic (% 26) to ensure that shifts wrap around the alphabet
			correctly. For example, shifting 'Z' by 1 wraps back to 'A'.'''
			new_ascii = ord('A') + (ord(char) - ord('A') + offset) % 26

			print('new_ascii:', new_ascii, '\n')

			# Convert the ASCII decimal to a character and
			# append it to the "encoded_text" variable.
			encoded_text += chr(new_ascii)
		else:
			# Processes whitespace characters.
			encoded_text += char
	return encoded_text

# Use case
print(f'caesar_cipher("ATTACK AT DAWN", 3): {caesar_cipher("ATTACK AT DAWN", 3)}')