# Ask the user about the weather.
weather = input("What's the weather like today? (sunny, rainy, snowy, windy): ")

# Concept:
# if-elif-else statement

# What is the purpose of elif?
# Suppose you need to write a program that checks 3 or
# more conditions.
# To accomplish this, you would need to use an if-elif-else statement.

# Give clothing advice using if-elif-else statements.
if weather == "sunny":
  	print("It's a beautiful day! Don't forget your sunglasses.")
elif weather == "rainy":
  	print("You'll need an umbrella ☔ and waterproof shoes!")
elif weather == "snowy":
  	print("Bundle up — it's freezing!")
elif weather == "windy":
  	print("Hold onto your hat!")
else:
  	print("Hmm... I don't know that kind of weather, but dress comfortably!")