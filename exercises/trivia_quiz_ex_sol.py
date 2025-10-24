# 🎉 Welcome to the Mini Trivia Quiz! 🎉
# This game asks a few trivia questions and keeps score.
# You’ll learn about input, comparison, .lower(), .upper(), and if-else logic.

print("Welcome to the Mini Trivia Quiz!")
print("Answer the questions correctly to earn points!\n")

# Start with a score of 0
score = 0

# 🟣 Question 1
answer1 = input("What color do you get when you mix red and blue? ").lower()

# We use .lower() so the answer isn't case-sensitive
if answer1 == "purple":
  print("Correct! 🟣")
  score += 1
else:
  print("Oops! The correct answer was purple.")

print()  # blank line for readability

# 🗼 Question 2
answer2 = input("What is the capital city of France? ").upper()

# We use .upper() so 'paris', 'Paris', and 'PARIS' all count the same
if answer2 == "PARIS":
  print("Correct! 🗼")
  score += 1
elif answer2 == "LONDON":
  print("Close, but that's in the UK!")
else:
  print("Nope! The answer is PARIS.")

print()

# 🕷️ Question 3
answer3 = input("How many legs does a spider have? ")

# input() always returns a string, so we compare to a string ("8")
if answer3 == "8":
  print("Correct! 🕷️")
  score += 1
else:
  print("Nope! Spiders have 8 legs.")

print("\n🎯 Quiz Complete! 🎯")
print("You got", score, "out of 3 correct!")

# Final feedback
if score == 3:
  print("🏆 Perfect score! You’re a trivia master!")
elif score == 2:
  print("👏 Great job! Almost perfect!")
elif score == 1:
  print("🙂 Nice try! You got one right.")
else:
  print("😅 Better luck next time!")

print("\nThanks for playing the Mini Trivia Quiz! 🥳")