# Character Creator Game!

print("🎮 Welcome to the Character Creator! 🎮\n")

# Get character information
name = input("What is your character's name? ")
age = int(input("What is your character's age? "))
power = input("What is their superpower? ")
can_fly = input("Can they fly? (yes or no) ")

# Convert the flying answer to a boolean
can_fly_bool = (can_fly == "yes")

# Calculate a fun stat
power_level = age * 10

# Display the character card
print("\n" + "="*40)
print("⭐ YOUR CHARACTER CARD ⭐")
print("="*40)
print("Name:", name)
print("Age:", age, "years old")
print("Superpower:", power)
print("Can fly:", can_fly_bool)
print("Power Level:", power_level)
print("="*40)

# Fun message based on age
if power_level > 500:
  print("\nYou are a super human being!")
else:
  print("\nYou are !")