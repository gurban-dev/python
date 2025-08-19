import re

'''
A regular expression (regex) is a special
pattern of characters that helps you find
or match parts of text.

Python's built-in re module is a library
for working with regular expressions. It
allows you to search, match, and manipulate
text using patterns.

Use cases:
Find specific parts of text (like email
addresses, phone numbers, etc.)

Validate user inputs (like checking if a string
is a valid date).

Replace text based on patterns.

Split strings based complex rules.
'''

def extract_emails(text):
  '''
  The r before the string means it's a raw
  string in Python: r'...'

  First part: [a-zA-Z0-9._%+-]+

  The first part is a character class because
  it is enclosed by square brackets []. A character
  class defines a set of characters to match.

  This is for matching the "username" part of an
  email address (before the @).

  In this case, the character class a-zA-Z0-9._%+-
  matches one or more characters that can be:
  a-z: lowercase letters

  A-Z: uppercase letters

  0-9: digits

  ._%+-: common special characters allowed in
  email usernames.

  The + that follows the square brackets means "one
  or more of the previous characters", so it matches
  strings like john.doe, alice123, etc.

  Second part: @[a-zA-Z0-9.-]+
  @ is a literal character, matching the @
  symbol in email addresses.

  [a-zA-Z0-9.-]+
  This is a character class, matching:
  a-z: lowercase letters

  A-Z: uppercase letters

  0-9: digits

  .: a dot (used for subdomains like mail.example.com)

  -: hyphen (used in domain names like my-site.org)

  The + that comes after the square brackets means
  one or more of these characters.

  It matches domain parts like:
  example

  google.com

  my-domain.co
  '''

  # Third part: \.[a-zA-Z]{2,}

  # The third part is supposed to match the
  # top-level domain in an email address,
  # such as .com, .org, .edu

  # This matches a literal dot (.). The backslash
  # \ is used to escape the dot because, in regex,
  # a plain . means "any character."

  # [a-zA-Z]{2,}
  # This matches 2 or more letters, where:
  # [a-zA-Z] means any uppercase or lowercase English
  # letter.

  # {2,} is a quantifier that says "match at least
  # 2 of the preceding pattern," with no upper limit.

  email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

  # Use re.findall() to get all substrings
  # in the text that match the pattern.
  matches = re.findall(email_pattern, text)
  
  return matches

text = """
Hello Alice, please contact us at support@example.com for assistance.
You can also reach out to bob.smith@company.co.uk or marketing@web.biz.
Thank you!
"""

emails = extract_emails(text)

print("Found emails:", emails)

def extract_number(number):
  pattern = r'\b\d+\b'

  matches = re.findall(pattern, number)

  return matches

# Dennis10

# How would you extract 10?
print('extract_number(\'Dennis10\'):', extract_number('Dennis10'))