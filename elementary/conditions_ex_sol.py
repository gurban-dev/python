# Task 1 solution
season = input("What is your favorite season? ")

if season.lower() == "summer":
  print("Summer is great for swimming!")
elif season.lower() == "winter":
  print("Winter is perfect for hot chocolate.")
elif season.lower() == "spring":
  print("Spring is full of flowers!")
elif season.lower() == "autumn" or season.lower() == "fall":
  print("Autumn has the best colors!")
else:
  print("That's a cool choice! Every season is unique.")


# Task 2 solution
age = int(input("How old are you? "))

city = input("What city do you live in? ")

if age >= 13:
  print("You are a teenager or older.")

if city.lower() == "new york":
  print("Cool! You live in New York.")