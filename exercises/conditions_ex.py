'''
Task 1:
Have the user type in their favourite season (E.g. summer).

Write an if-elif-else statement that accurately prints what the user
chose.

Goal:
Learn the difference between if, elif, and else blocks.

Practice comparing strings and using .lower() for case-insensitive matching.

Case-insensitive means that the case of the letters doesn't matter.

Understand that only one block in an if / elif / else statement runs.

----------------------------------------------------------------------------

Task 2:
Ask the user their age and whether they live in a rural area.
Check each condition separately. No elif, no else.

If the user is older than 65, print that they are elderly.
Otherwise, print that they are an adult.

If the user lives in a rural areas, print that they will have an increased
pension.
Otherwise, print that they do not qualify for an increased pension.

Goal:
Show that multiple conditions can be checked separately, without
affecting each other.

Understand that both, one, or none of the messages can print depending
on the inputs.
'''

# 1. Have the user type in their favourite season.
# 2. Use an if-elif-else statement to display whether the user
#    chose "spring", "summer", "autumn" or "winter".

# The input() function:
# • Pauses the program temporarily
# • Waits until the user clicks the 'Enter' button on their keyboard
# • Returns what the user typed in.

# 'favourite_season' is the variable.

# The value being assigned to the variable is the string
# that is returned by the  function.
favourite_season = input("What is your favourite season? ")

print("\nfavourite_season:", favourite_season, '\n')

if favourite_season == 'spring':
    print("You inputted \"spring\".")

elif favourite_season == 'summer':
    print("You inputted \"summer\".")

elif favourite_season == 'autumn':
    print("You inputted \"autumn\".")

elif favourite_season == 'winter':
    print("You inputted \"winter\".")

else:
    print("Favourite season can only be \"winter\", \"spring\", "
          "\"summer\" and \"autumn\".")