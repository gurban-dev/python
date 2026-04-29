
video_game = input('Do you prefer minecraft or age of empires? ').lower()

# If the "Enter" button is clicked on the keyboard
# without typing anything in, an empty string will
# be returned by the input() function on line 2.

# An empty string has a length of zero because it does
# not contain any characters.
print(f'\nlen(video_game): {len(video_game)}')

print('\nvideo_game:', video_game, '\n')

print(f'video_game == \'minecraft\': {video_game == 'minecraft'}')

print(f'video_game == \'age of empires\': {video_game == 'age of empires'}')

# If the condition (video_game == 'minecraft') on line number 25
# evaluates to True, the instruction on line 26 will be executed
# and no other conditions in the if-elif-else statement will be
# evaluated.

# Only one of the print statements in the if-elif-else statement
# below will be executed.
if video_game == 'minecraft':
	print('\nYou selected minecraft.')
elif video_game == 'age of empires':
	print('\nYou selected age of empires.')
else:
	print('\nYou selected neither minecraft nor age of empires.')