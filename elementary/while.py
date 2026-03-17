no_of_candy = input('Enter the number of candy you want to eat: ')

print('no_of_candy:', no_of_candy)

wants_to_play_another_round = 'yes'

# == (equality operator). It checks if two values
# are equal to each other.
while wants_to_play_another_round == 'yes':
  print('\nwants_to_play_another_round == \'yes\':',
        wants_to_play_another_round == 'yes')

  print('\nNew round beginning!')

  # How do you know that the following line of
  # code belongs to the while loop?
  # Answer: The following line is indented. Indented,
  #         meaning that it is positioned two spaces
  #         after the while loop header.
  wants_to_play_another_round = input(
    '\nWould you like to play another round? '
  )

  wants_to_play_another_round = wants_to_play_another_round.lower()

print('\nGame ended.')