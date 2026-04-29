# Concept:
# if-elif-else statement

# This program shows how Python makes decisions step by step.
# It will check conditions and choose only one path to run.

# Question: How many blocks execute?
# Answer: Only one block executes.

# Question: If both conditions are True, will both messages print?
# Answer: No. Python checks from top to bottom and stops at the first
#         True condition.

# Case A
# This is the number we are testing in the program.
num = 7

# Case B
# Try changing the number to 3 to see a different result.
# num = 3

# Case C
# Try changing the number to 10 to see another result.
# num = 10

# Python starts by checking this first condition.
# It asks: Is num greater than 10?
if num > 10:
    # This line runs only if the condition above is True.
    print("num is greater than 10.")

# If the first condition is False, Python checks this next one.
# It asks: Is num greater than 5?
elif num > 5:
    # This runs only if the first condition was False and this is True.
    print("num is greater than 5.")

# If none of the above conditions are True, Python runs this block.
else:
    # This is the default case when all other checks fail.
    print("num is not greater than 5.")

# This prints a blank line for spacing in the output.
print()


# Question: Why does Python stop after the first True condition?
# Answer: Because an if-elif-else statement is designed to choose only
#         one path.

#         Once a True condition is found, the rest are skipped.

"""
How if-elif-else works

Python checks conditions from top to bottom, one at a time.

It starts with the if condition:
- If it is True, that block runs.
- All remaining conditions are skipped.

If the if condition is False, Python moves to the next elif:
- It checks each elif in order.
- As soon as one is True, that block runs.
- The rest are not checked.

If none of the conditions are True:
- The else block runs.
- else has no condition because it is the default case.
"""