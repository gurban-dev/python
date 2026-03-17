'''
A Roman soldier rides north on his mighty stallion.

After many days, he discovers a mysterious village
protected by a colossal fortress, complete with towers,
guards, and a door.

The villagers are cautious; outsiders are not always welcome.

To enter safely, one must speak their language and offer
a token of respect, such as a gift or gesture recognised
in their customs.
'''

speaks_the_local_tongue = True

# Could be a gift, salute, or friendly gesture.
offers_token_of_respect = True

if speaks_the_local_tongue and offers_token_of_respect:
  print(
    "The soldier enters the village. The villagers nod with cautious\n"
    "respect, allowing him to pass and interact safely."
  )
elif speaks_the_local_tongue or offers_token_of_respect:
  print(
    "The soldier manages to enter, but the villagers remain suspicious.\n"
    "They keep a close eye on him and restrict his movements until his\n"
    "intentions are clear."
    )
else:
  print(
    "The soldier cannot communicate and forgets to show a token of respect.\n"
    "The villagers bar the gates, and he must return to Rome."
  )