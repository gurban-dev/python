def count_vowels() -> int:
  # vowels: list[str] = ['a', 'e', 'i', 'o', 'u']

  vowels: str = 'aeiou'

  word: str = input('Input a word: ')

  vowel_count: int = 0

  # word has a reference to an iterable (what the user types in which
  # becomes a string object in memory).
  # word_iter is the iterable that points to one before the first
  # character.
  word_iter = iter(word)

  print('\nnext(word_iter):', next(word_iter))

  for letter in word:
    if letter in vowels:
      vowel_count += 1

  return vowel_count

print('__name__:', __name__, '\n')

if __name__ == '__main__':

  while True:
    vowel_count = count_vowels()

    print('\nvowel_count:', vowel_count)

    enter_again: str = input(
      '\nInput \"yes\" if you would like to enter another word: '
    ).lower()

    if enter_again != "yes":
      break