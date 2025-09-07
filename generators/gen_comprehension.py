# Generator comprehension
generator_obj = (i for i in range(10))

print('generator_obj:', generator_obj, '\n')

for num in generator_obj:
  print('num:', num)