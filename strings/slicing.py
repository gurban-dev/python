'''
In Python, slicing is used to extract parts
of a string using the below syntax:

string[start:stop:step]

The start value specifies the index where
slicing begins.

G   o   o   d       d   a   y   !
0   1   2   3   4   5   6   7   8

Notice how the whitespace character has its
own index/indice which is index 4 in this
case.

The stop value specifies the index where
slicing ends (exclusive).
'''

# Negative indices count backward from the end
# of the string.
salutation = 'Good day!'

# Output:
# salutation[-1]: !
print('salutation[-1]:', salutation[-1])

print('\nsalutation[-2]:', salutation[-2])

'''
G   o   o   d       d   a   y   !
0   1   2   3   4   5   6   7   8
'''

# With only start and stop:
# Output:
# salutation[3:6]: d d
print('\nsalutation[3:6]:', salutation[3:6])

# Output:
# salutation[:4]: Good
print('\nsalutation[:4]:', salutation[:4])

# Output:
# salutation[5:]: day!
print('\nsalutation[5:]:', salutation[5:])

'''
 G    o    o    d         d    a    y    !
-9   -8   -7   -6   -5   -4   -3   -2   -1
'''

# Output:
# salutation[-5]: Good
print('\nsalutation[-5]:', salutation[-5])

'''
Negative indexing:
salutation[:-5]

Start = 0
Stop = -5

The stop value is excluded, so the slicing
occurs up until, but not including the
whitespace character at salutation[-5].
'''

# Output:
# salutation[:-5]: Good
print('\nsalutation[:-5]:', salutation[:-5])