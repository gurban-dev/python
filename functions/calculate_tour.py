# Inputs:
# Season (high-season, low-season)
# Quantity of tourists
# Has a child

# Output:
# The total cost of the tour.


def calculate_price(
  # Remember that a parameter that has a default
  # argument must not precede a parameter that
  # doesn't have one.
  # season_type: str, no_of_tourists: int = 0, has_child: bool
  season_type: str, no_of_tourists: int, has_child: bool = False) -> float:
  tour_price = 0

  print('has_child:', has_child)

  if season_type == 'High Season':
    tour_price += no_of_tourists * 20
  elif season_type == 'Low Season':
    tour_price += no_of_tourists * 15

  # If has_child evaluates to True.
  if has_child and tour_price >= 30:
    tour_price -= 15
  
  return tour_price

cost_of_tour1 = calculate_price('High Season', 4)

cost_of_tour2 = calculate_price('High Season', 4, True)

print('\ncost_of_tour1:', cost_of_tour1, '\n')

print('cost_of_tour2:', cost_of_tour2)