video_game = input('Do you prefer fortnite or minecraft? ').lower()

# If I just click the "Enter" button on my keyboard
# without typing anything in, an empty string will
# be returned by the input() function on line 1.

# An empty string has a length of zero because it does
# not contain any characters.
print('\nlen(video_game):', len(video_game))

print(f'\n{video_game} == \'fornite\': {video_game == "fortnite"}')
print(f'{video_game} == \'minecraft\': {video_game == "minecraft"}')

# If the condition on line number 4 evaluates to
# True, then the condition on line number 8 will
# not be evaluated.

# Only one of the print statements will be executed.
if video_game == 'fortnite':
  print('\nYou selected fortnite.')
elif video_game == 'minecraft':
  print('\nYou selected minecraft.')
else:
  print('\nYou selected neither fortnite nor minecraft.')