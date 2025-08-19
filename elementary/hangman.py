import random

HANGMAN_PIC = '''
  +---+
      |
      |
      |
     ===''','''
     ===''','''
  +---+
  o   |
      |
      |
     ===''','''
  +---+
  o   |
  |   |
      |
     ===''','''
  +---+
  o   |
 /|   |
      |
     ===''','''
  +---+
  o   |
 /|\  |
      |
     ===''','''
  +---+
  o   |
 /|\  |
 /    |
     ===''','''
  +---+
  o   |
 /|\  |
 / \  |
     ===''','''
'''

# The split() method will return a list containing
# all of the words in the subsequent multi-line
# string.
words = '''ant baboon badger bat bear beaver camel cat clam
         cobra cougar coyote crow deer dog donkey duck eagle
         ferret fox frog goat goose hawk lion lizard llama
         mole monkey moose mouse mule newt otter owl panda
         parrot pigeon python rabbit ram rat raven rhino salmon
         seal shark sheep skunk sloth snake spider stork swan
         tiger toad trout turkey turtle weasel whale wolf wombat
         zebra'''.split()

print('words:', words)
    
def getRandomWord(wordlist):
    # This function returns a random string from the past string
    wordindex = random.randit(o, len(wordlist) - 1)
    return wordlist [wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('missed letters,:' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len (secretWord)

    for i in range (len(secretWord)): # Replace blanks with correctly
    guessed letters.
    if secretword[i] in correctLetters:
    blanks = blanks[:i] + secretWord[i] + blank[i+1:]

    for letter in blanks: # Show the secret word with spaces in bettween
    each letter.
        print(letters, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letters the player has already enterd. This function makes sure the player only entered a single letter and not something else.
    while true:
        print('guess a letter.')
        guess =  input()
        guess = guess.lower()
        if len (guess) != 1:
        print(please enter a single letter.')