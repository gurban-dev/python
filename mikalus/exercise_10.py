sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = []

for num in sample_list:
  if num % 2 == 0:
    even_numbers.append(num)

# Expected outcome:
# even_numbers: [2, 4, 6, 8]

print(f'even_numbers: {even_numbers}')