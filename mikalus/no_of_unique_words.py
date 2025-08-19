# Different multi-line string than the
# one in the assignment.
sentence = """Lorem ipsum dolor sit amet,
       consectetur adipiscing elit,
       sed do eiusmod tempor incididunt
       ut labore et dolore magna aliqua."""

words = sentence.split()

# Use a set to extract unique words.
unique_words = set(words)

print('Number of unique words:', len(unique_words))