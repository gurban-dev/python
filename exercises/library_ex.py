"""
Exercise: Library Book Tracker

Learning Goals
--------------
Practice:
- Dictionaries
- while loops
- try / except EOFError
- if key in dictionary
- Counting occurrences
- sorted()
- .lower()
- .capitalize()
- .title()

Problem
-------
Write a program that tracks how many times books are borrowed.

The librarian enters one book title per line.

The program should continue accepting input until an EOFError occurs.

Requirements
------------
1. Ignore differences in capitalization.
2. Count how many times each book was borrowed.
3. Print the results in alphabetical order.
4. Store dictionary keys using ONE consistent capitalization style.
5. Display the titles using a reader-friendly capitalization style.

Example Input
-------------
harry potter
Harry Potter
HARRY POTTER
the hobbit
The Hobbit
clean code
clean code

Expected Output
---------------
3 Harry Potter
2 Clean Code
2 The Hobbit

Challenge Extensions
--------------------
1. Ignore leading and trailing spaces.
2. Allow the user to type:
       quit
       QUIT
       Quit
   to exit immediately.
3. Think carefully about where to use:
       .lower()
       .capitalize()
       .title()

Thinking Questions
------------------
1. Which method converts:
       hARRY pOtTer
   into:
       Harry Potter

2. Which method converts it into:
       harry potter

3. Which method converts it into:
       Harry potter

4. Why is storing everything in lowercase usually a good idea?

5. Why should the way data is stored be different from the
   way it is displayed?

Starter Code
------------
Complete the program below without looking up the syntax.
"""

books = {}

# TODO:
# 1. Repeatedly ask the user for a book title.
# 2. Stop when the user enters "quit" (any capitalization)
#    or sends EOF (Ctrl+D on macOS/Linux, Ctrl+Z then Enter on Windows).
# 3. Ignore extra spaces before and after the title.
# 4. Store the title using one consistent capitalization style.
# 5. Count how many times each title appears.
# 6. Print the books in alphabetical order.
# 7. Display each title in a reader-friendly format.

# Write your solution below.

