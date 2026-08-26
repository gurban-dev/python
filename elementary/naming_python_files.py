# Python File Rescue Mission.
# You are a detective trying to organize a messy Python folder.

print("🕵️ PYTHON FILE RESCUE MISSION 🕵️")

print("Uh oh!")
print("Someone left a folder full of Python programs...")
print("But the filenames are TERRIBLE! 😱")

print("\nYour mission:")
print("Figure out which filenames help you understand")
print("what each program does.")


input("\nPress Enter to begin the mission...")


print("\n========================================")
print("MISSION 1: FIND THE CALCULATOR")
print("========================================")


print("You need to find a program that calculates")
print("the total price of some items.")

print("\nWhich filename would you choose?")

print("A. stuff.py")
print("B. banana.py")
print("C. calculate_total.py")
print("D. x123.py")


answer = input("\nYour answer: ")

print()

if answer.lower() == "c":
    
    print("🎉 CORRECT!")
    print("calculate_total.py gives us a clue about what the program\n"
          "probably does.")
else:
    
    print("❌ Not quite!")
    print("\nThe best choice is calculate_total.py.")


input("\nPress Enter for the next mission...")


print("\n========================================")
print("MISSION 2: DEMON SLAYER FILE")
print("========================================")


print("You wrote a program that asks the user for their favorite\n"
      "Demon Slayer character.")

print("\nWhich filename would make the most sense?")

print("A. program.py")
print("B. demon_slayer_character.py")
print("C. stuff2.py")
print("D. aaa.py")


answer = input("\nYour answer: ")

print()

if answer.lower() == "b":
    
    print("⚔️ EXCELLENT!")
    print("demon_slayer_character.py tells us exactly what the program\n"
          "is about.")
else:
    
    print("❌ Try again!")
    print("\nThe best choice is demon_slayer_character.py.")


input("\nPress Enter for the FINAL MISSION...")


print("========================================")
print("🏆 FINAL MISSION 🏆")
print("========================================")


print("You find these four files:")

print("1. stuff.py")
print("2. pizza.py")
print("3. student_name.py")
print("4. thing.py")

print('\nWhich file asks the user for their name?')

answer = input("\nEnter the number: ")

print()

if answer == "3":
    
    print("🎉 MISSION COMPLETE!")
else:
    
    print("Almost!")
    print("The answer is 3: student_name.py")


print("\n========================================")
print("THE SECRET OF GOOD FILENAMES")
print("========================================")


print("A filename is like a label on a box.")

print("Imagine two boxes:")

print("📦 Box 1: 'stuff'")
print("📦 Box 2: 'board games'")

print("Which box would you open if you wanted")
print("to play some board games?")

print("A descriptive filename helps you and other programmers\n"
      "understand what a program is about without opening the file.")

print("\nThe key takeaway:\n"
      "Give your Python files names that tell people what the program does.")