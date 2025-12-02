lines = []

print(
	'Enter your multi-line text (press Enter on\n'
	'an empty line to finish inputting):'
)

while True:
	line = input()

	# Output the current line that was inputted by
	# the user.
	# print('line:', line)

	# If the user just clicked the "Enter" key on their
	# keyboard without typing anything in.
	if not line:
		break
	else:
		lines.append(line)

full_text = '\n'.join(lines)

print(full_text)