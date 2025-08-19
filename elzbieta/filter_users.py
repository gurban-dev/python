# The structure or format of the data in external_users
# is what would be expected in certain API responses.
external_users = [
  {"username": "jdoe", "active": True, "roles": ["user"]},
  {"username": "asmith", "active": False, "roles": ["user", "moderator"]},
  {"username": "bwhite", "active": True, "roles": ["admin", "user"]},
  {"username": "xguest", "active": False, "roles": ["guest"]},

  # 'support' is invalid
  {"username": "tlee", "active": True, "roles": ["moderator", "support"]},

  # User without any roles are also filtered out.
  {"username": "nmartinez", "active": True, "roles": []},

  # 'superadmin' is invalid
  {"username": "chill", "active": True, "roles": ["superadmin", "admin"]},

  {"username": "aparker", "active": True, "roles": ["guest", "user"]},
  {"username": "mnguyen", "active": False, "roles": ["admin"]},

  # 'intern' is invalid
  {"username": "rkumar", "active": True, "roles": ["intern"]}
]

valid_roles = ['admin', 'moderator', 'user', 'guest']

# List[Dict[str, int]]
# def get_valid_users():
  for external_user in external_users:
    print('external_user[]:', external_user[])

    # Output whether the condition satisfies.
    print('bool(external_user[] == ):', bool(external_user[] == ))

    print('external_user[] == :', external_user[] == )

    # Check if the external user is active.
    if external_user[] == :


    # 
    print('')

# get_valid_users()