'''
Exercise:
Starts with 50 points and has 5 activities.

Fill in the blanks with either += or -=.

Practices positive and negative number changes
(adding points for good things, losing points for
challenges).

Has a built-in check at the end to see if 69 points
was the outcome.

Tips:
+= means "add to" (things that help the garden)
-= means "subtract from" (things that harm the garden)

🌸 MAGIC GARDEN POINTS GAME 🌸

You're taking care of a magical garden! 
Let's keep track of your magic points as you do
different activities.

Your job: Fill in the blanks with += or -= to make
the program work correctly!
'''

# Start with 50 magic points.
magic_points = 50

print("🌷 Welcome to your Magic Garden! 🌷")
print(f"Starting magic points: {magic_points}")
print()

# Activity 1: Plant some flowers (adds 10 points)
print("🌺 You planted beautiful flowers!")

# magic_points ___ 10  # FILL IN: Should this be += or -= ?
magic_points += 10

print(f"Magic points now: {magic_points}\n")

# Activity 2: Oh no! Weeds appeared (lose 15 points)
print("🥀 Oh no! Weeds appeared in the garden!")

# magic_points ___ 15  # FILL IN: Should this be += or -= ?
magic_points -= 15

print(f"Magic points now: {magic_points}\n")

# Activity 3: You watered the plants (adds 20 points)
print("💧 You watered all the plants!")

# magic_points ___ 20  # FILL IN: Should this be += or -= ?
magic_points += 20

print(f"Magic points now: {magic_points}\n")

# Activity 4: A bunny ate some carrots (lose 8 points)
print("🐰 A cute bunny ate some carrots from your garden!")

# magic_points ___ 8  # FILL IN: Should this be += or -= ?
magic_points -= 8

print(f"Magic points now: {magic_points}\n")

# Activity 5: Butterflies visited! (adds 12 points)
print("🦋 Beautiful butterflies visited your garden!")

# magic_points ___ 12  # FILL IN: Should this be += or -= ?
magic_points += 12

print(f"Magic points now: {magic_points}\n")

# Final score
print("=" * 40)
print(f"🌈 Final magic points: {magic_points} 🌈\n")

# Check if the correct number of magic points was calculated.
if magic_points == 69:
  print("✨ Perfect! You filled in all the operators correctly! ✨")
else:
  print("💭 Hmm, check your += and -= again!")
  print(f"(Hint: You should end with 69 points)")