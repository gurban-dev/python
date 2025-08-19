'''
Importing the defaultdict class from Python's built-in
collections module.

defaultdict automatically provides default values for
missing keys, so you don't get a KeyError when accessing
a key that doesn't have a corresponding value yet.
'''
from collections import defaultdict

def custom_groupby(data, key):
    '''
    Passing list as an argument means that if you access a key
    that doesn't exist yet, it will automatically create a new
    empty list for that key.

    This is necessary because the subsequent line looks up the
    list at grouped[row[key]] and appends "row" to that list:
    grouped[row[key]].append(row)
    
    If grouped were a normal dictionary and the key row[key]
    didn't exist yet, grouped[row[key]] would raise a KeyError
    because there's no list yet to append to.
    '''
    grouped = defaultdict(list)

    for row in data:
        print(f'row[{key}]: {row[key]}')
        print(f'type(row[{key}]): {type(row[key])}\n')

        print('row:', row)
        
        # grouped[row[key]] will always return a list, even if that
        # key was never added before.
        
        # grouped['alice'].append({'user': 'alice', 'amount': 50})
        grouped[row[key]].append(row)

    return dict(grouped)

# A list of dictionary items.
data = [
    {"user": "alice", "amount": 50},
    {"user": "bob", "amount": 30},
    {"user": "alice", "amount": 20}
]

result = custom_groupby(data, "user")

print('result:', result)

'''
The main takeaways from this example are:
 
1. How to group a list of dictionaries by a specific key
   without relying on external libraries like pandas.

 
2. defaultdict(list) automatically initializes empty lists
   for new keys, simplifying code by avoiding explicit key
   existence checks.
 
3. The for loop goes through each dictionary item list called
   "data". On each iteration, it looks up the value associated
   with the grouping key ('user'), then adds that entire
   dictionary item to the list of rows already grouped under
   that key.

   The "grouping key" is the specific dictionary key whose
   values you want to group by.

   All dictionaries that share the same "user" value, will
   be grouped together.
'''