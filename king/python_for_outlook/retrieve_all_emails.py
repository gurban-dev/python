import os
import httpx
from dotenv import load_dotenv
from textwrap import dedent

# Reference the name of a module without the py file extension.
# ms_graph.py is the entire file name.
from ms_graph import get_access_token, MS_GRAPH_BASE_URL

# If you wanted to import everything from ms_graph.py:
# from ms_graph import *

# This program is making use of the Microsoft Graph API
# to retrieve emails from a Microsoft Outlook account.

def main():
	# Load the environment variables into the Python environment.
	load_dotenv()

	# Obtain the environment variables.
	APPLICATION_ID = os.getenv('APPLICATION_ID')

	CLIENT_SECRET = os.getenv('CLIENT_SECRET')

	'''
	Define scopes related to Microsoft Graph API permissions:
	User.Read: Allows reading user profile information.

	Mail.ReadWrite: Enables reading and writing mail.
	'''
	SCOPES = ['User.Read', 'Mail.ReadWrite']

	'''
	Define the API endpoint for the email retrieval.'
	
	MS_GRAPH_BASE_URL refers to the base URL used for accessing
	the Microsoft Graph API. This API is a unified endpoint that
	allows developers to interact with various Microsoft 365 services,
	such as Outlook, OneDrive, Teams, etc.

	Actual URL: https://graph.microsoft.com/v1.0/me/messages

	The endpoint https://graph.microsoft.com/v1.0/me/messages is
	used to access and manage the messages (emails) of the currently
	signed-in user in Microsoft Graph.'''
	endpoint = f'{MS_GRAPH_BASE_URL}/me/messages'

	try:
		# The access_token in your code is obtained through the
		# function get_access_token, which likely interacts with
		# an authorisation server.
		access_token = get_access_token(
			application_id=APPLICATION_ID,
			client_secret=CLIENT_SECRET,
			scopes=SCOPES
		)

		'''
		The Authorization: Bearer {access_token} header validates the
		request by proving the app has permission to access emails in
		Outlook.'''
		headers = {
			'Authorization': 'Bearer ' + access_token
		}

		'''
		range(start, stop, step)

		Begin at 0, stop at 4 without including 4, and icnrement by 2.
		'''
		for i in range(0, 4, 2):
			# Define the parameters for the outlook API request.
			params = {
				# Limit the quantity of emails retrieved in each API call to 2.
				'$top': 2,

				# Specify the fields to be returned.
				# The asterisk returns all fields.
				'$select': '*',

				# Skip over the previously retrieved emails.
				'$skip': i,

				# Retrieve the most recent emails first.
				# desc stands for descending order.
				'$orderby': 'receivedDateTime desc'
			}

			# Send an HTTP GET request to the endpoint.
			response = httpx.get(endpoint, headers=headers, params=params)

			# A status of of 200 indicates that the HTTP request was
			# successfully processed.
			if response.status_code != 200:
				raise Exception(f'Failed to retrieve emails: {response.text}')

			# Take the httpx.Response object and parse it into a Python
			# dictionary data structure.
			json_response = response.json()

			# Properties:
			# https://learn.microsoft.com/en-us/graph/api/resources/message?view=graph-rest-1.0#properties

			for mail_message in json_response.get('value', []):
				# The 'isDraft' property can be seen in the above link
				# the references the documentation.
				if mail_message['isDraft']:
					print(dedent(
						f'''
							Subject: {mail_message['subject']}
							To: {mail_message['toRecipients']}
							Is Read: {mail_message['isRead']}
							Received Date Time: {mail_message['receivedDateTime']}

					'''))
				else:
					print(dedent(f'''
						Subject: {mail_message['subject']}
						To: {mail_message['toRecipients']}
						From: {mail_message['from']['emailAddress']['name']}
						Is Read: {mail_message['isRead']}
						Received Date Time: {mail_message['receivedDateTime']}						
					'''))
		print('-' * 140)

	# This exception is raised when an HTTP request returns
	# a status code that indicates an error (4xx or 5xx).
	except httpx.HTTPStatusError as err:
		print(f'HTTP Error: {err}')
	# General exception class in Python that
	# catches any other unexpected errors.
	except Exception as err:
		print(f'Error: {err}')

# Test the script by invoking the main() function.
main()

'''
4xx status codes: Client Errors

4xx errors occur due to issues on the client side.

The server is unable to process the request
because it is invalid or improperly formed.

5xx status codes: Server Errors

5xx errors occur when the server fails to fulfill a valid
request due to an internal issue or temporary unavailability.
'''