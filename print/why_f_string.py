# Variables
given_name = 'Alexander'
title = 'the Great'
origin = 'Pella, Greece'
year_of_birth = 356

# Using commas (less readable for complex text).
print("Historical figure:", given_name, title, 
      "was born in", origin + ", in", year_of_birth,
      "BC.")

# f-strings are preferable when combining text and variables,
# because they keep code concise and easier to read.
print(f"\nHistorical figure: {given_name} {title} "
      f"was born in {origin}, in {year_of_birth} BC.")