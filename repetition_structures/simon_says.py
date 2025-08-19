'''
"Simon Says" is a memory game where "Simon" outputs
a sequence of 10 characters (R, G, B, Y) and the user
must repeat the sequence. Create a for loop that
compares each character of the two strings. For each
matching character, add one point to user_score. Upon
a mismatch, end the loop.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
'''

# The data type of variable "seq1" is determined
# at runtime due to Python being a dynamically
# typed programming language.
seq1 = 'RRGBRYYBGY'
seq2 = 'RRGBBRYBGY'

# Integer
user_score = 0

for i in range(len(seq1)):
  # 1st iteration:
  # i = 0
  seq1Char = seq1[i]

  seq2Char = seq2[i]

  print('seq1Char:', seq1Char,
        '\nseq2Char:', seq2Char)

  # If the character at the current index/indice
  # are equivalent, increment "user_score" by 1.
  # Otherwise, break out of the for loop.
  if seq1Char == seq2Char:
    user_score += 1
  else:
    break

print(f'User score: {user_score}')

simon_pattern = 'RRGBRYYBGY'
user_pattern = 'RRGBBRYBGY'

# The min() function returns the item with
# the lowest value, or the item with the
# lowest value in an iterable.

# min(len(simon_pattern) returns 0.
for i in range(min(len(simon_pattern), len(user_pattern))):
  '''
  If simon_pattern only has 9 characters, but
  user_pattern has 10, accessing simon_pattern[9]
  will generate an error because a string with
  9 character will not have an index beyond 8.'''
  if simon_pattern[i] == user_pattern[i]:
    user_score += 1
  else:
    # Stop the loop at the first mismatch
    break

print(f'User score: {user_score}')