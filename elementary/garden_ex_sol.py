"""
🌸 MAGIC GARDEN POINTS GAME - SOLUTION 🌸

You're taking care of a magical garden! 
Let's keep track of your magic points as you do different activities.
"""

# Start with 50 magic points
magic_points = 50
print("🌷 Welcome to your Magic Garden! 🌷")
print(f"Starting magic points: {magic_points}")
print()

# Activity 1: Plant some flowers (adds 10 points)
print("🌺 You planted beautiful flowers!")
magic_points += 10  # Use += because we're ADDING points (good thing!)
print(f"Magic points now: {magic_points}")
print()

# Activity 2: Oh no! Weeds appeared (lose 15 points)
print("🥀 Oh no! Weeds appeared in the garden!")
magic_points -= 15  # Use -= because we're LOSING points (bad thing!)
print(f"Magic points now: {magic_points}")
print()

# Activity 3: You watered the plants (adds 20 points)
print("💧 You watered all the plants!")
magic_points += 20  # Use += because we're ADDING points (good thing!)
print(f"Magic points now: {magic_points}")
print()

# Activity 4: A bunny ate some carrots (lose 8 points)
print("🐰 A cute bunny ate some carrots from your garden!")
magic_points -= 8  # Use -= because we're LOSING points (bad thing!)
print(f"Magic points now: {magic_points}")
print()

# Activity 5: Butterflies visited! (adds 12 points)
print("🦋 Beautiful butterflies visited your garden!")
magic_points += 12  # Use += because we're ADDING points (good thing!)
print(f"Magic points now: {magic_points}")
print()

# Final score
print("=" * 40)
print(f"🌈 Final magic points: {magic_points} 🌈")
print()

# Check if they got it right
if magic_points == 69:
  print("✨ Perfect! You filled in all the operators correctly! ✨")
else:
  print("💭 Hmm, check your += and -= again!")
  print(f"(Hint: You should end with 69 points)")