'''
Concepts:
Lists and list indexing

The len() function

User input with input()

String methods (.lower(), .capitalize())

Membership operator (in)

Equality operator (==)

Conditional statements (if, elif, else)

Nested conditionals

Accessing characters in a string using indexing

Basic program flow and decision making

Variables and reassignment

Exercise Instructions:
Create a simple shopping assistant program that asks the user what
item they want to buy and tells them whether the item is affordable,
moderately priced, or expensive.

Program Overview

The program uses two lists:
items - contains product names

prices - contains the price corresponding to each item


The user will input the item they want, and the program will:
Check if the item exists in the store.

Find the item's price.

Print a message describing its price category.
'''
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