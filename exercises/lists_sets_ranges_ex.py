'''
Python Fundamentals Exercise:
Lists, Sets, Ranges, and Operators

Objective:
This exercise is designed to reinforce your understanding of:
- Python lists and sets
- Equality (==) and not-equal (!=) operators
- The range() function (start, stop, step)
- The __name__ dunder variable
- Basic iteration and conditional logic

PART 1: Working with Lists

1. Create a list called numbers that contains the integers
   1 through 1 000.

2. Print the entire list.

3. Loop through the list and:
   - Print each number
   - If the number is NOT equal to 5, print: "<number> is not 5"
   - If the number IS equal to 5, print: "Found 5!"

4. Create a new list called 'even_numbers'.
   - Add only the even numbers from the numbers list to 'even_numbers'.
   - Print 'even_numbers' when finished.


PART 2: Using range()

5. Use the range() function to generate numbers from 0 to 20 (inclusive).
   - Print each number.

6. Use range() with start, stop, and step to:
   - Generate only odd numbers from 1 to 20.
   - Store them in a list called odd_numbers.
   - Print the list.

7. Use range() with a step to count backwards from 10 to 0.
   - Print each value.


PART 3: Working with Sets

8. Create a list called duplicate_nums with the following values:
   [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

9. Convert duplicate_nums into a set called unique_nums.
   - Print unique_nums.
   - Observe what happened to the duplicates.


PART 4: Equality vs. Not Equality

11. Ask the user to input a number (use input()).
    - Convert the input to an integer.

12. Compare the user's number to the number 10:
    - If it == 10, print: "You entered 10."
    - If it != 10, print: "This is not 10."

13. Add the user's number to a list called user_nums.
    - If the number already exists in the list, print: "Duplicate detected."
    - Otherwise, add it and print the updated list.
'''

# Python's built-in input() function temporarily pauses the
# execution of a Python program and waits for the user to
# click the 'Enter' button on their keyboard.

# Irregardless of the content inputted, the input() function
# always returns a string object.
num = int(float(input('Enter a number: ')))

print('type(num):', type(num), '\n')

print('num:', num, '\n')


'''
PART 5: The __name__ Dunder Variable

14. At the bottom of your script, add the following conditional:

    if __name__ == "__main__":

15. Inside this block:
    - Print: "This script is being run directly."
    - Call a function of your choice from earlier in the exercise.

16. Outside of the if __name__ == "__main__" block:
    - Print: "This code was imported as a module."

(Think about when each message would appear and why.)

- Refactor repeated logic into functions.
- Try converting a list to a set and back to a list.
- Experiment with different range() step values.
- Add comments explaining what each section does.
'''