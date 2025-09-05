"""
EXERCISE: BUY 3 GET 1 FREE

A pizzeria has a sales campaign on-going and gives
away 1 pizza for free if the customer purchases 3
pizza's.

In this exercise, you have to write a function named
"Price_of_Pizzas()" that has two parameters named
Number_of_pizzas and Price_per_pizza. 

Given this information, the function returns the total
cost of the order of the customer.

For example, buying 3 pizza’s for $10.50 each costs
$31.5 (or 3 × 10.5). But buying 4 pizza’s also costs
$31.5, since the first 3 makes the 4th pizza free.

Buying 5 pizza’s is calculated as follows: $ 31.5 for
the first 3 pizza’s, a free 4th pizza, and another
$10.50 for the 5th pizza for a total of $42.00.
"""

def Price_of_Pizzas(Number_of_pizzas, Price_per_pizza):
  # 28 // 4 -> 7

  # Divide by four because the fourth pizza is free.
  no_of_free_pizzas = Number_of_pizzas // 4

  no_of_paid_pizzas = Number_of_pizzas - no_of_free_pizzas

  return no_of_paid_pizzas * Price_per_pizza
    
print('Price_of_Pizzas(5, 10.5):', Price_of_Pizzas(5, 10.5))
print('Price_of_Pizzas(28, 14):', Price_of_Pizzas(28, 14))
print('Price_of_Pizzas(45, 18.2):', Price_of_Pizzas(45, 18.2))
