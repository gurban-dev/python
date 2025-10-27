def calculate_monthly_savings(
  income: float, expenditure: float) -> float | str:
  difference = income - expenditure

  # print('difference:', difference)

  if difference > 0:
    return difference
  else:
    return "You did not save anything for this month."

monthly_income = 2500.00
monthly_expenditure = 2000.00

result = calculate_monthly_savings(monthly_income, monthly_expenditure)

statement = ""

if isinstance(result, float):
  # statement = "Your monthly savings: " + str(result)

  statement = f"Your monthly savings: {result}"
else:
  statement = result

print(statement)