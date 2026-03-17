import pwinput
from getpass import getpass

def get_credentials() -> tuple[str, str]:
	username: str = input('Please input your username: ')

	# Shows '*' by default.
	password = pwinput.pwinput("Please input your password: ")

	# password: str = getpass('Please input your password: ')

	return username, password

username, password = get_credentials()

print('username:', username)
print('password:', password)