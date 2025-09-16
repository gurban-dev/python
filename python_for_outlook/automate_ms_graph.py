import os
import msal
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

MS_GRAPH_BASE_URL = 'https://graph.microsoft.com/v1.0'

def get_access_token(application_id, client_secret, scopes):
	client = msal.ConfidentialClientApplication(
		client_id=application_id,
		client_credential=client_secret,
		authority='https://login.microsoftonline.com/consumers/'
	)

	refresh_token = None

	# Check if a file named refresh_token.txt exists in
	# the current working directory.
	if os.path.exists('refresh_token.txt'):
		# If the file exists, this line opens it in read
		# mode ('r').

		# open() returns a file object.
		with open('refresh_token.txt', 'r') as file:
			refresh_token = file.read().strip()

			# Output:
			# type(refresh_token): <class 'str'>
			# print(f'type(refresh_token): {type(refresh_token)}')

	# Evaluates to True so long as the "refresh_token"
	# variable is not an empty string.
	if refresh_token:
		# If a valid refresh token is available, attempt
		# to acquire a new access token using that refresh
		# token.
		token_response = client.acquire_token_by_refresh_token(
			refresh_token,
			scopes=scopes
		)
	else:
		'''
		No refresh token, proceed with the authorisation
		code flow.

		Generate a URL that the user must visit to
		authenticate and authorize the application.'''
		auth_request_url = client.get_authorization_request_url(scopes)

		# with sync_playwright() as p:
		# 	# Set headless=True for no UI
		# 	browser = p.chromium.launch(headless=False)
		# 	page = browser.new_page()

		# 	page.goto(auth_request_url)

		# 	# Simulate the email address login process.
		# 	page.fill('input[type="email"]', 'leilamehti@hotmail.com')
		# 	# page.wait_for_selector('button[type="submit"]', timeout=20000)
		# 	page.click('button[type="submit"]')

		# 	# Wait for password page and fill in the password.
		# 	page.fill('input[type="password"]', 'Tatiana1939!')
		# 	# page.wait_for_selector('button[type="submit"]', timeout=20000)
		# 	page.click('button[type="submit"]')

		# 	# Wait for the consent page (if applicable) and click accept.
		# 	page.wait_for_selector('button[type="submit"]', timeout=60000)
		# 	page.click('button[type="submit"]')

		# 	# After successful login, the page will be
		# 	# redirected to the redirect URI with an
		# 	# authorization code.
		# 	page.wait_for_url(f"https://localhost.com:8000/?code=")
		# 	url = page.url
		# 	browser.close()

		# 	# Extract the authorization code from the URL
		# 	code = url.split("code=")[1]

		# 	return code

		'''
		Check if the user entered an authorisation code. If
		the input is empty (e.g., the user just pressed the
		Enter key without pasting the code), raise a ValueError.'''
		if not authorization_code:
			raise ValueError('Authorisation code is empty')

		'''
		If a valid authorisation code is provided, use it
		to acquire an access token.

		The acquire_token_by_authorization_code() method
		exchanges the authorisation code for an access
		token and possibly a refresh token, depending on
		the flow and configuration.'''
		token_response = client.acquire_token_by_authorization_code(
			code=authorization_code,
			scopes=scopes
		)

	print('type(token_response):', type(token_response))

	'''
	Validate that the access token was generated.

	token_response is likely a dictionary data structure
	that consists of a key called 'access_token'.'''
	if 'access_token' in token_response:
		# Store the refresh token securely.
		if 'refresh_token' in token_response:
			'''
			The 'w' mode means the file will be opened for
      writing.

			If the file already exists, its contents will be
			overwritten; if not, a new file will be created.

			The variable file is a file object returned by the
			open() function.

			It represents the opened file (refresh_token.txt)
			in write mode ('w').

			The with statement ensures that the file object is
			automatically closed when the program exits the
			block of code inside it.'''
			with open('refresh_token.txt', 'w') as file:
				file.write(token_response['refresh_token'])

			return token_response['access_token']
	else:
		# The raise statement is used to explicitly
		# trigger an exception.
		raise Exception('Failed to acquire access token: ' +
                    str(token_response))

def main():
	'''
	Load the environment variables from the .env file
	into the Python environment.

	Environment variables hold a predetermined value
  used by applications. These variables provide a
  way to configure and share information between
  multiple programs without hardcoding values into
  the source code.'''

	load_dotenv()

	# Retrieve the value of the two environment variables.
	APPLICATION_ID = os.getenv('APPLICATION_ID')

	CLIENT_SECRET = os.getenv('CLIENT_SECRET')

	'''
	Define scopes related to Microsoft Graph API permissions:
	User.Read: Allows reading user profile information.

	Mail.ReadWrite: Enables reading and writing mail.

	Mail.Send: Allows sending mail.'''
	SCOPES = ['User.Read', 'Mail.ReadWrite', 'Mail.Send']

	try:
		# Source code put inside of the try section
		# is known as protected code.

		access_token = get_access_token(
			application_id=APPLICATION_ID,
			client_secret=CLIENT_SECRET,
			scopes=SCOPES
		)

		'''
		The headers dictionary is declared after the call
    to get_access_token(application_id=APPLICATION_ID)
    because the value of access_token is required to
    construct the Authorization header.
		
		If all goes well, the generated access token should
    appears in the "headers" variable.'''
		headers = {
			'Authorization': 'Bearer ' + access_token
		}
		print(f'\nheaders: {headers}')
	except Exception as err:
		print(f'Error: {err}')

main()