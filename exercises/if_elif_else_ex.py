'''
Concept:
if-elif-else statement

Please complete the following tasks:
1. Fill in the missing source code below to have a proper
   if-elif-else statement.

2. How many of the conditional branches (if, elif, else) will execute?

3. If both conditions are true (num > 10 and num > 5), will both messages
   print? Why or why not?

4. Change the value of num and predict the output before running:

   Case A: num = 7
   Case B: num = 3
   Case C: num = 10

5. Why does Python stop checking conditions after the first True condition
   in an if-elif-else structure?

Note that the final block in an if-elif-else statement is the default case
and does not test a condition.
'''

# The variable name is 'num'.
# 'num' references the integer 15.
num = 15

# In this context, if two expressions evaluate to True, how many
# statements will be printed?

# > is the greater than operator.

# If num > 10 means if num is greater than 10.
if num > 10:
	print("num is greater than 10.")
elif num > 5:
    print("num is greater than 5.")
else:
    print("num is not greater than 5.")

print("After if-elif-else statement.")