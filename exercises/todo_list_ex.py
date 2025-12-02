'''
Write a Python program that:
1. Displays a multi-line instruction message explaining
   what the user should do.

2. Asks the user to enter three tasks for a to-do list.

3. For each input, uses the .strip() method to remove leading and
   trailing whitespace characters.

4. If a user leaves a task blank (after stripping), use the not
   operator to detect this and warn them.

5. Stores the cleaned tasks in a list.

6. After all inputs are collected, uses the .join() method to print
   the final to-do list as a single formatted string.

Example Run
-----------

Welcome to the To-Do List Creator!

You will enter 3 tasks.
Extra spaces at the beginning or end will be removed automatically.
Empty tasks are not allowed!

Enter task #1:
Finish math homework

Enter task #2:

You entered an empty task. Please try again.
Re-enter task #2:
Study for science quiz

Enter task #3:
Clean my room

Your final to-do list:
Finish math homework
Study for science quiz
Clean my room
'''