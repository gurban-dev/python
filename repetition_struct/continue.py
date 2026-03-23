items = ['aardvark', 'badger', 'clementine']

'''
The continue keyword is a way to "jump" to the next item in a
loop so that the remaining code in the loop is not executed.
'''
for item in items:
    # If the item on the current iteration starts with the
    # letter 'b', the remaining code in this loop block will
    # not be executed.
    if item.startswith('b'):
        continue

    # Remaining code:
    print('item:', item)