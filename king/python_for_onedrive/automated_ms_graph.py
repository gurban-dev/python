import os
import msal
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import webbrowser
import time

MS_GRAPH_BASE_URL = 'https://graph.microsoft.com/v1.0'

def get_access_token(application_id, client_secret, scopes):
	print('python_for_onedrive/automated_ms_graph.py')

	# print('application_id:', application_id)
	# print('client_secret:', client_secret)
	# print('scopes:', scopes)

	client = msal.ConfidentialClientApplication(
		client_id=application_id,
		client_credential=client_secret,
		authority='https://login.microsoftonline.com/consumers/'
	)

	auth_request_url = client.get_authorization_request_url(scopes)

	with sync_playwright() as p:
		# Set headless=True for no UI.
		browser = p.chromium.launch(headless=False)

		context = browser.new_context()
		page = context.new_page()

		page = browser.new_page()

		page.goto(auth_request_url)

		EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')

		PASSWORD = os.getenv('PASSWORD')

		# Simulate the email address login process.
		page.fill('input[type="email"]', EMAIL_ADDRESS)
		page.click('button[type="submit"]')

		# Wait for the password page and fill in the password.
		page.fill('input[type="password"]', PASSWORD)
		page.click('button[type="submit"]')

		try:
			# Set a custom timeout of 3 seconds for
			# locating and clicking the element.
			page.locator('input[id="checkboxField"]').click(timeout=3000)
			print("Checkbox clicked successfully!")
		except Exception as e:
			print(f"Element not found within 3 seconds: {e}")

		time.sleep(2)

		page.click('#declineButton')

		# noBtn = page.get_by_text("No")

		# noBtn = page.locator('button:has-text("No")')

		# yesBtn = page.locator('button:has-text("Yes")')

		# print('yesBtn:\n', yesBtn)

		# yesBtn.click()

		# await page.keyboard.press('Enter')

		print('After button click')

		# After successful login, the page will be
		# redirected to the redirect URI with an
		# authorization code.
		page.wait_for_url(f"https://localhost.com:8000/?code=", timeout=0)

		url = page.url

		browser.close()

		# Extract the authorization code from the URL
		code = url.split("code=")[1]

		return code

	# webbrowser.open(auth_request_url)

	# authorization_code = input('\nEnter the authorization code:')

	token_response = client.acquire_token_by_authorization_code(
		code=authorization_code,
		scopes=scopes
	)

	if 'access_token' in token_response:
		return token_response['access_token']
	else:
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