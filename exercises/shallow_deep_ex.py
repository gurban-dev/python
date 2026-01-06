import copy

num1 = 100

# num2 is assigned the same integer object as num1.
num2 = num1

# Integers are immutable.
# This creates a new integer object (150) and rebinds num2 to it.
num2 += 50

print('num1:', num1, ', num2:', num2)

# num1 does not change because integers are immutable.
# num2 += 50 does not modify the original object.
# Instead, num2 is rebound to a new integer object.


hello = "Hello"

# greeting references the same string object as hello.
greeting = hello

# Strings are immutable.
# This creates a new string object and rebinds greeting.
greeting += " world!"

print('hello:', hello, ', greeting:', greeting)

# 'hello' does not change because strings are immutable.
# greeting += " world!" creates a new string object.
# Only greeting is rebound to the new object.


# list1 is a list containing two inner lists.
list1 = [[1, 2], [3, 4]]

# list2 references the same outer list object as list1.
# A copy is not made.
list2 = list1

# list3 is a shallow copy of list1.
# A new outer list is created, but inner lists are shared.
list3 = list1[:]

# list4 is also a shallow copy.
# Behaviour is identical to slicing.
list4 = copy.copy(list1)

# This modifies the first inner list.
# Inner lists are shared by list1, list2, list3, and list4.
list2[0][0] = 99

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("list4:", list4)

# list1, list2, list3, and list4 are all affected.
# This is because all of them reference the same inner lists.
# Shallow copies duplicate only the outer list, not nested objects.

# This appends a new inner list to list3 only.
# list3 has its own outer list object.
list3.append([5, 6])

print("\nAfter appending to list3:")
print("list1:", list1)
print("list3:", list3)

# Only list3 is affected because append modifies the outer list.
# list1 and list3 do not share the same outer list object.
# They only shared inner lists prior to this operation.


# list5 is a deep copy of list1.
# Both the outer list and all inner lists are duplicated.
list5 = copy.deepcopy(list1)

# This modifies an inner list inside list5 only.
list5[0][1] = 777

print("list1:", list1)
print("list5:", list5)

# list1 does not change because deepcopy creates completely
# independent objects.

# No references are shared between list1 and list5.