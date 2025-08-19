trow = [1]
y = [0]

# Since max(2, 0) is 2, the loop will run twice.
for x in range(max(2, 0)):
  '''
  [l + r for l, r in zip(trow + y, y + trow)]

  1st for loop iteration:
  zip(trow + y, y + trow) is evaluated first.

  zip(trow + y, y + trow) ->
  zip([1] + [0], [0] + [1]) ->
  zip([1, 0], [0, 1]) ->
  an iterator of tuples (1, 0) (0, 1)

    The comments below are indented to make it
    clear that the list comprehension iterations
    are happening within the for loop iteration.

    1st list comprehension iteration:
    l = 1 r = 0
    l + r -> 1 + 0 -> 1

    1 is added to the new list that will be
    returned by the list comprehension.

    2nd list comprehension iteration
    l = 0 r = 1
    l + r -> 0 + 1 -> 1

    1 is added to the new list that will be
    returned by the list comprehension.

  The next statement is de-indented to indicate
  that the flow of the program is no longer in
  the list comprehension loop.
  trow = [1, 1]

  2nd for loop iteration:
  zip(trow + y, y + trow) ->
  zip([1, 1] + [0], [0] + [1, 1]) ->
  zip([1, 1, 0], [0, 1, 1]) ->
  an iterator of tuples (1, 0) (1, 1) (0, 1)

    1st list comprehension iteration:
    l = 1 r = 0
    l + r -> 1 + 0 -> 1

    1 is added to the new list that will be
    returned by the list comprehension.

    2nd list comprehension iteration:
    l = 1 r = 1
    l + r -> 1 + 1 -> 2

    2 is added to the new list that will be
    returned by the list comprehension.

    3rd list comprehension iteration
    l = 0 r = 1
    l + r -> 0 + 1 -> 1

    1 is added to the new list that will be
    returned by the list comprehension.

  trow = [1, 2, 1]
  '''
  print(trow)

  trow = [l + r for l, r in zip(trow + y, y + trow)]