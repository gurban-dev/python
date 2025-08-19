import re

# A word character is: a–z, A–Z, 0–9, or underscore _

# A non-word character is anything else: whitespace,
# punctuation, etc.

text = "abc123def and 123 apples"

pattern = r'\b\d+\b'

matches = re.findall(pattern, text)

print('matches:', matches)