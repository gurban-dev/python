"""
EXERCISE: THE LONGEST WORD

Write a function called "longest word" that takes a string
of text as argument.
The function should identify the longest word in the argument
and return that word, as well as the length of that word in a
string of text:
"The longest word is ... and it is ... characters long"
"""

def longest_word(str):
    list_of_words = str.split()

    longest_word = max(list_of_words, key=len)

    return f'{longest_word} is {len(longest_word)} characters long.'

'''
If there is more than one word that has the same number
of characters in a sentence, the program will simply
return the first one that has the same number of characters
as the others.'''
print(longest_word("The Englishman Who Went Up a Hill But Came Down a Mountain"))

print(longest_word("Alice in Wonderland"))   