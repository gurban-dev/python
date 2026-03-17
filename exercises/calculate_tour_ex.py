'''
Exercise: Tour Price Calculator

Python Concepts Reinforced:
- Function parameters and default arguments
- Boolean values and conditional statements (if / elif)
- Arithmetic operations and logic flow
- Function return values
- How argument order affects function calls

Goal:
Understand how a Python function calculates a tour price using
parameters, default arguments, and conditional statements.

Function: calculate_price(season_type, no_of_tourists, has_child=False)

season_type: "High Season" or "Low Season"

no_of_tourists: number of tourists

has_child: True/False (default False), applies a child discount


Price Calculation Rules:

Base price per tourist:
High Season: 20 Euros
Low Season: 15 Euros

Total price = base price * number of tourists

If has_child=True and total >= 30 Euros, subtract 15 Euros.


Function Calls to Examine:
cost_of_tour1 = calculate_price('High Season', 4)      # No child
cost_of_tour2 = calculate_price('High Season', 4, True) # Child included


Compare the outputs to see how the has_child parameter affects the total.

Trace the logic step by step before running the program.
'''