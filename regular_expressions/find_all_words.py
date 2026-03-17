import re

'''
Goal:
Write a function that finds all words in a sentence
that start with a capital letter (like names, places,
or the first word in a sentence).
'''

def extract_capital_words(text):
  pattern = r'\b[A-Z][a-z]*\b'

  return re.findall(pattern, text)

# Example input:
text = "Alice went to Paris to visit the Eiffel Tower with Bob."

words_beginning_with_capital = extract_capital_words(text)

print('words_beginning_with_capital:',
      words_beginning_with_capital)

# Expected output:
# ['Alice', 'Paris', 'Eiffel', 'Tower', 'Bob']

'''
| Part     | Meaning                                                       |
| -------- | ------------------------------------------------------------- |
| `\b`     | Word boundary: makes sure we're at the start or end of a word |
| `[A-Z]`  | One capital letter (A through Z)                              |
| `[a-z]*` | Zero or more lowercase letters after the capital letter       |
| `\b`     | Another word boundary at the end                              |
'''