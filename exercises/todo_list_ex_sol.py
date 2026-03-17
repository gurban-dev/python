# Step 1: multi-line instruction message
instructions = """
Welcome to the To-Do List Creator!

You will enter 3 tasks.
• Extra spaces at the beginning or end will be removed automatically.
• Empty tasks are not allowed!
"""

print(instructions)

tasks = []

# Step 2-5: get three tasks, clean them, validate, store
for i in range(1, 4):
  # Clean with strip()
  user_input = input(f"Enter task #{i}: ").strip()

  # Detect empty input using not operator
  while not user_input:
    print("You entered an empty task. Please try again.")

    user_input = input(f"Re-enter task #{i}: ").strip()

  tasks.append(user_input)

# Step 6: join to produce final formatted list
result = "\n".join(tasks)

print("\nYour final to-do list:\n{result}")