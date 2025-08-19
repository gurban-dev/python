import re

def extract_phone_numbers(text):
  # Regular expression pattern.
  phone_pattern = r'(\+\d{1,3}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'

  '''
  | Part                    | Meaning                                                                |
  | ----------------------- | ------------------------------------------------|
  | `(\+\d{1,3}\s?)?`       | **Optional country code**: `+` followed by 1-3  |
  |                         |   digits, optional space                        |
  | `(\(?\d{3}\)?[\s.-]?)?` | **Optional area code**: 3 digits, possibly in   |
                                `()`, optional separator                      |
  | `\d{3}`                 | **First part** of local number: 3 digits                               |
  | `[\s.-]?`               | **Optional separator**: space, dot, or hyphen                          |
  | `\d{4}`                 | **Second part** of local number: 4 digits                              |

  First part:
  (\+\d{1,3}\s?)?

  (\+
  Matches a literal plus sign +, which usually begins a
  country code like +1 or +44.

  \d{1,3}
  Matches 1 to 3 digits representing the country code number.

  \s?
  Matches zero or one whitespace character after the
  country code (optional space).

  () and ? outside the parentheses
  The entire group is optional, meaning the phone number may
  or may not include a country code.

  Example matches: +1 , +44, or nothing (if no country code).


  Second part:
  (\(?\d{3}\)?[\s.-]?)?

  \(?
  Matches optional opening parenthesis (. The backslash escapes
  the parenthesis because parentheses are special in regex.

  \d{3}
  Matches exactly 3 digits, often the area code (e.g., 123).

  \)?
  Matches optional closing parenthesis ).

  [\s.-]?
  Matches optional separator after the area code:

  \s = whitespace (space or tab)

  . = dot

  - = hyphen

  () and ? outside the parentheses
  The whole group is optional because some numbers may
  omit the area code.

  Example matches: (123) , 123-, 123., 123 , or nothing.


  Third part:
  \d{3}[\s.-]?\d{4}

  \d{3}
  Matches exactly 3 digits, the first part of the local
  number (e.g., 456).

  [\s.-]?
  Matches optional separator (space, dot, or hyphen).

  \d{4}
  Matches exactly 4 digits, the last part of the local
  number (e.g., 7890).


  Putting it all together, this regex can match:

  Optional country code (e.g., +1 )

  Optional area code with or without parentheses (e.g.,
  (123) or 123)

  A 7-digit number split into 3 + 4 digits with optional
  separators (e.g., 456-7890)

  Examples matched:

  +1 (123) 456-7890

  (555) 123 4567

  123.456.7890

  555-1234 (area code omitted)
  '''

  matches = re.findall(phone_pattern, text)

  # re.findall() with groups returns tuples, so reconstruct full matches:
  full_matches = []
  for match in matches:
    full_match = ''.join(match)
    full_matches.append(full_match.strip())

  return full_matches

text = """
Call us at +1 (123) 456-7890 or (555) 123 4567.
Our office number is 123.456.7890 and the hotline is 555-1234.
"""

phones = extract_phone_numbers(text)
print("Found phone numbers:", phones)