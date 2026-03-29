"""
Simple Grocery Price Checker

CONCEPTS:
- Lists (creating and accessing elements)
- Index lookup (.index())
- The len() function
- User input with input()
- String methods (.lower(), .upper(), .capitalize())
- String indexing (accessing characters like choice[-1])
- Membership operator for strings and lists (in)
- Conditional statements (if / elif / else)
- Comparison operators (==, <, >=, <=)
- Boolean expressions
- Basic output formatting with print()

--------------------------------------------------

OBJECTIVE
Build a simple program that:
1. Stores a list of items and their corresponding prices.
2. Asks the user what they would like to buy.
3. Checks whether the item exists in the store.
4. If it exists:
   - Finds its price
   - Formats the item name nicely
   - Determines whether it is affordable, moderately priced, or expensive
5. If it does not exist:
   - Displays an appropriate message

STEP-BY-STEP INSTRUCTIONS

1. CREATE DATA STRUCTURES
- Create a list called 'items' containing strings:
  ['persimmon', 'mango', 'quince']
- Create a second list called 'prices' with corresponding float values:
  [0.95, 1.25, 2.99]

2. PRINT NUMBER OF ITEMS
- Use len(items) to display how many items are available.

3. GET USER INPUT
- Prompt the user with:
  "What would you like to buy?"
- Convert the input to lowercase using .lower()
  (This ensures case-insensitive comparison)

4. DEBUG / LEARNING OUTPUT
- Print:
  - The user's choice
  - The length of the input string
- Demonstrate case sensitivity:
  Compare "KEFIR" == "kefir"

5. CHECK IF ITEM EXISTS
- Use:
  choice in items
- This returns True or False

6. IF ITEM EXISTS
- Find its index using:
  items.index(choice)
- Use that index to get the corresponding price from 'prices'

7. FORMAT THE ITEM NAME
- Capitalize the first letter using .capitalize()

8. HANDLE GRAMMAR (IS vs ARE)
- Check the last character:
  choice[-1]
- If it ends with 's', use "are"
- Otherwise, use "is"

9. DETERMINE PRICE CATEGORY
- If price < 5 -> "affordable"
- If price between 5 and 10 -> "moderately priced"
- Otherwise -> "expensive"

10. IF ITEM DOES NOT EXIST
- Print:
  "Sorry, we don't sell that item."
"""

items = ['persimmon', 'mango', 'quince']

prices = [2.99, 2.5, 3.99]

for item in items:
    print(item)

'''
Step-by-Step Tasks
1. Review the Lists

Look at the items and prices lists.

Notice that both lists share matching indexes.


Example:
items[0] corresponds to prices[0].


2. Understand Program Output

The program prints the number of available items using len().

It then asks the user to input an item name.

The user input is converted to lowercase so comparisons work correctly.


3. Analyse User Input

Print the user's choice.

Print the number of characters in the user's input.

Observe how Python compares strings using the equality operator (==).


4. Membership Testing

The program checks whether the user's choice exists in the items list using:
choice in items


If the item exists:
Find its index.

Retrieve the corresponding price.

Format the item name for display.


5. String Handling

Capitalise the item name.

Determine whether the item name ends in "s":

If yes -> add " are"

If no -> add " is"


6. Price Classification

Use conditional logic to categorise the price:

Less than $5 -> affordable

Between $5 and $10 -> moderately priced

Greater than $10 -> expensive


7. Invalid Items

If the user enters an item not sold by the store, print:
Sorry, we don't sell that item.
'''