video_game = input('Do you prefer roblox or age of empires? ').lower()

# If the "Enter" button is clicked on the keyboard
# without typing anything in, an empty string will
# be returned by the input() function on line 1.

# An empty string has a length of zero because it does
# not contain any characters.
print(f'\nlen("{video_game}"): {len(video_game)}')

print('\nvideo_game:', video_game)

print(f'video_game == \'roblox\': {video_game == 'roblox'}')

print(f'video_game == \'age of empires\': {video_game == 'age of empires'}')

# If the condition on line number 22 evaluates to
# True, then the condition on line number 24 will
# not be evaluated.

# Only one of the print statements will be executed.
if video_game == 'roblox':
  print('\nYou selected roblox.')
elif video_game == 'age of empires':
  print('\nYou selected age of empires.')
else:
  print('\nYou selected neither roblox nor age of empires.')