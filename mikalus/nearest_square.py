limit = 40
num = 0

# while (6 + 1)**2 < 40:
while (num + 1)**2 < limit:
  # First iteration:
  # 0 = 0 + 1 -> num = 1
  num += 1

  # First iteration:
  # nearest_square = 1**2 -> 1
  nearest_square = num**2

print('Nearest Square:', nearest_square)