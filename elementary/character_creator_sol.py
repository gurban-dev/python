# Character Creator Game!

print("🎮 Welcome to the Character Creator! 🎮\n")

# Get character information
name = input("What is your character's name? ")

# The age was converted to an integer because one lin
# 18, the age variable is being multiplied by 10.
age = int(input("What is your character's age? "))

power = input("What is their superpower? ")
can_fly = input("Can they fly? (yes or no) ")

# Convert the flying answer to a boolean.
can_fly_bool = (can_fly == "yes")

# Calculate the power level by multiplying age by 10.
power_level = age * 10

# Display the character card
print("\n" + "=" * 40)
print("⭐ YOUR CHARACTER CARD ⭐")
print("="*40)
print("Name:", name)
print("Age:", age, "years old")
print("Superpower:", power)
print("Can fly:", can_fly_bool)
print("Power Level:", power_level)

# In Python, it is possible to multiply strings by
# integers to have them repeat multiple times.
print("=" * 40)

# Look at line 19, if the calculation assigned to the
# variable power_level is greater than 500, then the
# program will execute line number 36.
if power_level > 500:
  print("\nYou are a super human being!")
else:
  print("\nYou are a regular human being.")