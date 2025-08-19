# Indices:
#       0  1  2  3
seed = [1, 2, 3, 4]

lst_of_results = []

# # Extract a slice/subsection of the "seed" list
# from index 1 up to, but not including, index 3.
print('seed[1:3]:', seed[1:3])

lst_of_results.append(sum(seed[1:3]))

# seed*2 takes the current list and doubles
# its size through making a copy of its
# current elements.
print('\nseed*2:', seed*2)

lst_of_results.append((seed*2)[3])

print('\nlst_of_results:', lst_of_results)