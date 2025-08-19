D = {1: [1, 2, 3], 2: (4, 6, 8)}

D[1].append(4)

print('D[1]:', D[1])

# Declare a list and assign it to "L".
# The first and so far only element of
# list "L" is a tuple data structure.
# [(4, 6, 8)]
L = [D[2]]

print('L:', L)

L.append(10)

# D[2] = ((4, 6, 8), 10)
D[2] = tuple(L)

print('D[2]:', D[2])