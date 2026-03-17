'''
Problem: Extract All Overlapping SUbstrings Between Delimiters

You are given a string that may contain overlapping occurrences
of the substring "ab".

Task:
1. Count how many times "ab" appears (including overlapping).
2. Find all starting indices of "ab" using .find() correctly
   (avoid off-by-one bugs).
3. For each occurrence, extract a slice that includes the "ab"
   substring and the next two characters, but only if they exist
   (to practice bounds safety).

Example input:
s = "ababxababc"

Expected output:
Count: 4
Indices: 0, 2, 5, 7

Extracted substrings:
"ab" + next two characters -> "abab"
"ab" + next two characters -> "abxa"
"ab" + next two characters -> "abab"
"ab" only -> (because fewer than 2 characters remain)
'''

def analyze_ab(s: str) -> tuple[int, list[int], list[str]]:
  target: str = "ab"
  indices: list[int] = []
  extracted: list[str] = []

  starting_index: int = 0

  while True:
    # Find the next occurrence beginning at "starting_index".
    index = s.find(target, starting_index)

    # If the .find() method return -1.
    if index == -1:
      break

    indices.append(index)

    # Extract "ab" + the next two characters (if they exist)
    # Slicing does not generate errors in Python.

    # index + 4 would be excluded.
    extracted.append(s[index : index + 4])

    # Move the start forward by 1 to allow overlapping matches.
    starting_index = index + 1

  # Any function that uses a comma-separated return statement
  # automatically returns a tuple.
  return len(indices), indices, extracted

s: str = "ababxababc"

print(f'analyze_ab({s}): {analyze_ab(s)}')