def calculate_team_score(score):
  # Separate the characters in "score" by the
  # hyphen character and store them as items
  # in a list.
  scores = score.split('-')

  print('scores:', scores)

  if int(scores[0]) > int(scores[1]):
    scores[0] = '3'
  elif int(scores[0]) < int(scores[1]):
    scores[1] = '3'
  else:
    scores[0] = '1'
    scores[1] = '1'

  scores = (int(scores[0]), int(scores[1]))

  return scores

print('calculate_team_scores(\'2-0\'):', calculate_team_score('2-0'), '\n')
print('calculate_team_scores(\'2-2\'):', calculate_team_score('2-2'), '\n')
print('calculate_team_scores(\'1-2\'):', calculate_team_score('1-2'), '\n')