sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

unique_list = []

for num in sample_list:
  if num not in unique_list:
    unique_list.append(num)

# Expected outcome:
# unique_list: [1, 2, 3, 4, 5]

print(f'unique_list: {unique_list}')