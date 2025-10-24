# This line prints a welcome message when the game starts.
print("Welcome to the Watermelon Adventure! 🍉")

# This line asks the end user a question and waits for them
# to type "yes" or "no".
# The assignment operator (=) assigns whatever
# they type to the variable called "answer".
answer = input("\nDo you like watermelons? (yes or no): ").lower()

# \n: newline escape sequence
# \' single quote escape sequence
print('\nanswer == \'yes\':', answer == 'yes', '\n')

# The equality operator (==) checks if the person typed "yes".
# Use .lower() so the condition is satisfied even
# if they type "YES", "Yes", or "yEs".
if answer.lower() == "yes":
  # If the answer is yes, we print a happy watermelon message.
  print("Yay! Here's a big juicy watermelon just for you! 🍉😋")
# This checks if the person typed "no".
elif answer.lower() == "no":
  # If the answer is no, we print the following instead:
  # "Oh no! More watermelon for me then! 😎"
  print("Oh no! More watermelon for me then! 😎")
# If the person didn't type "yes" or "no", we get here.
else:
  # Inform the end user that their input wasn't understood
  # and remind them to type the right answer next time.
  print("Hmm, I didn't understand that. Try typing 'yes' or 'no' next time!")