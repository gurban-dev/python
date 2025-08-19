answer = 35

# Prompt the end user.
guess = int(input("Guess: "))

if guess < 35:
  result = "Oops! Your guess was too low."
elif guess > 35:
  result = "Oops! Your guess was too high."
elif guess == 35:
  result = "Your guess matched the answer!"

print(result)