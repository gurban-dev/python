def find_pair_sum(numbers, target):
  '''
  This known as a nested for loop because
  a for loop is inside of another one.

  Both the outer for loop and the inner for
  loop will iterate five times because there
  are 5 elements in the "numbers" list.'''

  # Outer for loop's 1st iteration:
  # i = 1

  for i in numbers:
    print('i:', i)

    # Inner for loop's 1st iteration:
    # j = 1

    # Subsequent iterations:
    # j = 2
    # j = 3
    # j = 4
    for j in numbers:
      print('j:', j)

      # 1st iteration of outer for loop and
      # 1st iteration of inner for loop:
      # i = 1
      # j = 1

      # 1st iteration of outer for loop and
      # 4th iteration of inner for loop:
      # i = 1
      # j = 4

      # 1 + 4 == 5 and 1 != 4:
      if i + j == target and i != j:
        return (i, j)

# Why is the output of this program (1, 4)?
print(find_pair_sum([1, 2, 3, 4, 5], 5))