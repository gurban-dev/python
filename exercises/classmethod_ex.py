'''
Design a system that manages user access levels
for a web application.

Each end user can be an Admin, Editor, or Viewer.

Class and static methods will be utilised to manage
them.

Requirements

Create a class called User.

Each User has:

username

role (one of "admin", "editor", "viewer")

The class should keep track of how many users have been created.

Methods to Implement

@classmethod def from_string(cls, user_str)

Accepts a string like "alice:admin" and returns a new User instance.

@staticmethod def is_valid_role(role)

Returns True if the role is one of "admin", "editor", or "viewer".

Returns False otherwise.

@classmethod def total_users(cls)

Returns the total number of created users.

def has_access(self)

Returns True if the user is an admin or editor, and False otherwise.

In the main code:

Try creating users both directly and via from_string().

Print whether each has access (using truthy/falsy evaluation).

Print total users.

Example Output:
alice = User.from_string("alice:admin")
bob = User.from_string("bob:viewer")
carol = User("carol", "editor")

print(User.total_users())
print(User.is_valid_role("mod"))

for user in [alice, bob, carol]:
  if user:  # truthy/falsy check
    print(f"{user.username} has access.")
  else:
    print(f"{user.username} has no access.")


Expected Output:
3
False
alice has access.
bob has no access.
carol has access.
'''


class User:
  pass