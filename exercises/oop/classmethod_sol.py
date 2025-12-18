class User:
  # Class variable to track total users
  user_count = 0

  def __init__(self, username, role):
    self.username = username

    self.role = role.lower()

    # validate role
    if not User.is_valid_role(self.role):
      raise ValueError(f"Invalid role: {self.role}")
    else:
      print('User objected/instance successfully created.')

    # increment count when a new valid user is created
    User.user_count += 1

  @staticmethod
  def is_valid_role(role):
    """Check if role is valid."""

    # The curly braces indicate that this is a set.
    # A set is a data structure and type that stores unique items.
    valid_roles = {"admin", "editor", "viewer"}

    if role in valid_roles:
      return True
    else:
      return False

    # return role.lower() in valid_roles
  
  def __str__(self):
    return f"self.username: {self.username}, " \
           f"self.role: {self.role}, User.user_count: {User.user_count}"