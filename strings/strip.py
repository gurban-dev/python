# Validating user input.
email_address: str = input('Enter your email address: ').strip()

# The strip() method will remove leading and trailing whitespace
# characters from a string object.

# E.g.
#                                  alexanderhamilton@gmail.com                  

print('len(email_address):', len(email_address))

print('\nlen(\'alexanderhamilton@gmail.com\'):', len('alexanderhamilton@gmail.com'))

print(f'\nemail_address: {email_address}')