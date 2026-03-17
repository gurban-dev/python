# king_name = input('Type in your given name: ').lower()

king_name = 'Alexander'

# end='\n' is a keyword argument because the name of the
# parameter "end" is explicitly written out.
print('len(king_name):', len(king_name), end='\n')

# user_input += '!'

# A string variable.
# user_input.find()

king_name += '!!'

print('\nking_name:', king_name)

# Search for the ensuing substring: '!'
# string_variable_name.find(substring, start_index, end_index (exclusive))

# Exclusive means that the search will not include the end_index.
# This index is excluded from the search.
index_of_exclamation_mark = king_name.find('!', 0, len(king_name))

# If -1 is returned, that indicates that the substring was not found
# within the string being searched.
print(f'\nindex_of_exclamation_mark: {index_of_exclamation_mark}')

# If there are two exclamation marks, the index of only
# the first occurence is returned.

# Indices:     0123456789
# king_name = 'Alexander!'

# Size of "king_name" is 9.

# A string object that consists of ten thousand characters.
large_string = '*' * 10000

print('\nlen(large_string):', len(large_string))