weight = int(input("Enter your weight: "))

unit = input(
	'If you entered your weight in pounds, enter' \
	'"L", if entered your weight in kilos, enter "K": ')

if unit == "L":
  weight = weight*0.453592
  convertedTo = "kilos"
else:
  weight = weight*2.20462
  convertedTo = "pounds"

print(f'You weigh {round(weight)} {convertedTo}.')