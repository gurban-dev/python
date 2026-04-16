choice = 'cappuccino'

if choice == "fruits":
    print('The theatregoer chose fruits.')
elif choice == "popcorn":
    print('The theatregoer chose popcorn.')
else:
    print('The theatregoer chose neither fruits nor popcorn.')

"""
Control flow in an if-elif-else statement proceeds from top to
bottom, evaluating each condition in order. The program first
checks the condition in the if statement. If it evaluates to
True, the corresponding block of code is executed, and the rest
of the conditions are skipped.

If the if condition is False, the program moves to the next
condition in the elif statement and evaluates it. This process
continues sequentially until a True condition is found. Once a
True condition is encountered, its block executes and the
remaining conditions are not checked.

If none of the conditions in the if or any elif statements
evaluate to True, the else block is executed by default. The
else statement does not have a condition because it serves as
a fallback case when all prior conditions fail.
"""