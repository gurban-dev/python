# Task 1 solution
season = input("What is your favourite season? ")

print('\nseason:', season)

print('season.lower() == "summer":', season.lower() == "summer", '\n')

if season.lower() == "summer":
  print("Summer is great for swimming!")
elif season.lower() == "winter":
  print("Winter is perfect for hot chocolate.")
elif season.lower() == "spring":
  print("Spring is full of flowers!")
elif season.lower() == "autumn" or season.lower() == "fall":
  print("Autumn has the best colors!")
else:
  print("That's an interesting choice, but that is not a season.")


# Task 2 solution
age = int(input("\nHow old are you? "))

city = input("What city do you live in? ")

if age >= 13:
  print("\nYou are a teenager or older.")

if city.lower() == "Washington DC":
  print("You live in Washington DC.")
else:
  print("You don't live in Washington DC.")