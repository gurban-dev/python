'''
Concepts:
for loops
while loops
Boolean expressions
The input() function
F-strings with format specifiers

Instructions:
1. Generate a secret random number.

Use the random module to generate a random number between 1 and 20.

import random

random.randint(start (inclusive), stop (inclusive))
secret_no = random.randint(1, 20)


2. Let the User Guess

Use a while loop to repeatedly ask the user to guess the number:
"Enter your guess: "

Count how many guesses the user has made.

Use boolean expressions to check:
If the guess is too high, print "Too high!"

If the guess is too low, print "Too low!"

If the guess is correct, print "Correct!" and exit the loop.


3. Store All Guesses

Keep track of each guess in a list.


4. Display All Guesses

After the user guesses correctly, use a for loop to display
all guesses in the format:

Guess #1: 12
Guess #2: 8
Guess #3: 14


5. Calculate and Display the Average

Compute the average of all guesses and print it using an
f-string with two decimal places:

average = sum(guesses) / len(guesses)
print(f"Average guess value: {average:.2f}")


Example Run:
Enter your guess: 10
Too low!
Enter your guess: 17
Too high!
Enter your guess: 14
Correct!

Your guesses:
Guess #1: 10
Guess #2: 17
Guess #3: 14

Average guess value: 13.67
'''