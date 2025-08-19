'''
Problem to solve:
Given two strings "s" and "t", return true if the
two strings are anagrams of each other, otherwise
return false.

An anagram is a string that contains the exact same
characters as another string, but the order of the
characters can be different.

E.g. dog & god

Inputs:
Two different strings called "s" and "t".

Output:
True if strings "s" and "t" are anagrams of each
other, otherwise false.

1. If strings "s" and "t" are not the same length,
   return false.
2. Declare a dictionary countS and countT where
   countS keeps track of the quantity of each character
   in string "s" and countT keeps track of the quantity
   of each character in string "t".
3. Loop through the indexes or indices of string "s".
   a. Increment the integer value in countS associated
      with the current character in string "s".
   b. Increment the integer value in countT associated
      with the current character in string "t".
4. Loop through dictionary countS.
   a. If the value associated with the current key in countS
      is not equal to the value associated with the current
      key in countT, return false because the occurence of
      each character in string "s" and "t" are not the same.
5. Return true since each character in strings "s" and "t"
   occur the same amount of times.
'''

# stringOne is an anagram of stringTwo if
# stringOne has the same number of each
# character as stringTwo.
def isAnagram(s: str, t: str) -> bool:
  # len(s) -> 6 len(t) -> 6
  # if 6 != 6:
  if len(s) != len(t):
    return False

  # Two hashmaps or dictionaries.
  countS, countT = {}, {}

  # for index in range(6):
  for index in range(len(s)):
    # get() ensures that if the key does not exist
    # in the hashmap, the default value will be zero.

    # First iteration:
    # countS[s[0]] = 1 + 0 or countS["a"] = 1 + 0
    # countS['a'] = 1 + countS.get('a', 0)
    # countS['a'] = 1 + 0
    # countS['a'] = 1
    '''
    countS = {
      'a': 1
    }
    '''
    countS[s[index]] = 1 + countS.get(s[index], 0)

    # countT[t[0]] = 1 + 0 or countT["n"] = 1 + 0
    # countT['a'] = 1 + countT.get('n', 0)
    # countT['t'] = 1 + 0
    # countT['t'] = 1
    '''
    countT = {
      't': 1
    }
    '''
    countT[t[index]] = 1 + countT.get(t[index], 0)

  for character in countS:
    # If countS has a character that does not exist
    # in countT, the get() function will return a
    # default value of zero.
    if countS[character] != countT.get(character, 0):
      return False

  return True

#    0123456
s = "anagram"
t = "nagaram"

# t[0] -> "n"

print('isAnagram(s, t):', isAnagram(s, t))

# Time complexity: O(s + t)
# Space complexity: O(s + t)

# The time and space complexity are both
# O(s + t) because we need to iterate through
# both strings and we will be building hashmaps
# that could be potentially the size of strings
# s and t.

# A solution with O(1) space complexity would
# be to sort the two strings, so that they are
# in the same alphabetical order.