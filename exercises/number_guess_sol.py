import random

# Step 1: Generate a secret number between 1 and 20.

# randint(low (inclusive), high (inclusive)) returns an integer
# between low and high, both inclusive.
secret = random.randint(1, 20)

# Step 2: Initialise variables
guesses = []
guess_count = 0
correct = False

# Step 3: Start the guessing loop
while not correct:
	try:
		# Ask for user input
		user_input = input("Enter your guess: ")

		guess = int(user_input)
	except ValueError:
		print("Please enter a valid integer.")
		continue

	# Count the guess and store it.
	guesses.append(guess)

	guess_count += 1

	# Step 4: Check the guess
	if guess < secret:
		print("Too low!")
	elif guess > secret:
		print("Too high!")
	else:
		print("Correct!")
		correct = True

# Step 5: Display all guesses
print("\nYour guesses:")
for index, guess in enumerate(guesses, start=1):
	print(f"Guess #{index}: {guess}")

# Step 6: Calculate and display average guess value
average = sum(guesses) / len(guesses)
print(f"\nAverage guess value: {average:.2f}")