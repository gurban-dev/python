import os
import base64
import mimetypes
import httpx
from manual_ms_graph import MS_GRAPH_BASE_URL

# The ID of the target folder in a person's email
# must be identified before emails can be retrieved
# from a specific folder.

'''
The default folder is "drafts" because of
its assignment as a default parameter.

Remember that in Python, default parameters must follow
non-default parameters in a function definition.'''
def search_folder(headers, folder_name='drafts'):
	# Full URL: 'https://graph.microsoft.com/v1.0/me/mailFolders'
	endpoint = f'{MS_GRAPH_BASE_URL}/me/mailFolders'

	response = httpx.get(endpoint, headers=headers)

	'''
	The next line automatically raises an exception if
	the HTTP response status code indicates an error
	(i.e., a status code of 4xx or 5xx).

	This prevents silent failures by ensuring that errors
	like "404 Not Found" or "500 Internal Server Error"
	are not ignored.

	Including this line would be necessary to catch the
	errors in a try except block.'''
	response.raise_for_status()

	'''
	Microsoft Graph API is returning all of the folders.

	The response.json() method parses the JSON response
	from the Microsoft Graph API into a Python dictionary.

	The data type of "response" is an httpx.Response object.

	The value key in the JSON response contains a list of
	mail folder objects. This is standard in Microsoft
	Graph API responses:
	https://learn.microsoft.com/en-us/graph/traverse-the-graph?tabs=http

	If the "value" key is not present, the default return
	is an empty list.

	The value that corresponds with "value" is a Python list.
	In that Python list, there is another dictionary with a
	key called "displayName".'''
	folders = response.json().get('value', [])

	# Iterate through all of the folders in a person's email.
	for folder in folders:
		'''
		.lower() is invoked to ensures that the comparison
		between folder['displayName'] and folder_name is
		case-insensitive.

		Meaning that the program ignores case and matches
		values regardless of their lower or upper case
		letters.'''
		if folder['displayName'].lower() == folder_name.lower():
			return folder

	# None is the return value if the folder being
	# sought is not found in the person's email.
	return None

# Exempt the file provided and return the file mime
# type that needs to be included when attaching a
# file in an email message.
def get_mime_type(file_path):
	mime_type, _ = mimetypes.guess_type(file_path)

	return mime_type

# In order to create an attachment,
# the file_path must be identified.
def create_attachment(file_path):
	# Open the file for reading in binary mode ('rb') to
	# handle all file types (text, images, PDFs, etc.).
	with open(file_path, 'rb') as file:
		content = file.read()
		encoded_content = base64.b64encode(content).decode('utf-8')

	# Returns a dictionary consisting of the required
	# properties to attach a file to an email.
	return {
		# Do not write multi-line comments (''' ''')
		# within these curly braces as they will
		# generate an error.

		# @odata.type: Specifies the attachment type (fileAttachment
		# vs. itemAttachment for calendar items).

		# #microsoft.graph.fileAttachment is a resource type that
		# represents the attached file. It has its own properties
		# as well.
    '@odata.type': '#microsoft.graph.fileAttachment',

		# Extract the file name from the given file_path and
		# assign it to the 'name' key in a dictionary.
		# File path for one particular attachment.
		'name': os.path.basename(file_path),

		# Determines the MIME type (e.g., application/pdf,
		# image/jpeg) via the get_mime_type() function.
		'contentType': get_mime_type(file_path),

		# Take the binary content (likely read from a file)
		# and encodes it into Base64 format.

		# Make sure to encode the file content in base64
		# before assigning it to contentBytes.
		'contentBytes': encoded_content
	}

def get_messages(headers, folder_id=None, fields='*', top=5,
				    		 order_by='receivedDateTime', order_by_desc=True,
			  				 max_results=20):
	'''
	If the folder ID is not provided, it can be assumed that emails
	from the entire Outlook account must be retrieved.

	Otherwise, emails from the target folder will be retrieved by
	including it in the endpoint URL.
	'''
	if folder_id is None:
		endpoint = f'{MS_GRAPH_BASE_URL}/me/messages'
	else:
		endpoint = f'{MS_GRAPH_BASE_URL}/me/mailFolders/{folder_id}/messages'

	'''
	Set the API call parameters.

	$select: Filters properties (columns) returned in the response.
	* causes all columns to be returned.

	$top: Limits the number of results returned.
	top is equal to 5 and max_results is equal to 20,
	so min(top, max_results) returns 5.

	$orderby: Sorts results by a specified field.
	If order_by_desc evaluates to True, the emails will be
	ordered by 'desc' (descending order). Otherwise, by 'asc'
	(ascending order).
	
	In this context, descending order sorts emails from the
	most recent to the oldest date and time.'''
	params = {
		'$select': fields,
		'$top': min(top, max_results),
		'$orderby': f'{order_by} {'desc' if order_by_desc else 'asc'}'
	}

	# A list storing accumulated email messages across all
	# paginated requests.
	messages = []

	# Stores the URL for the next batch of data.
	# Initialised with the initial endpoint.
	next_link = endpoint

	# If there are additional emails, use the next link.
	# "next_link" evaluates to True as long as it is not
	# an empty string ('').
	while next_link and len(messages) < max_results:
		'''
		For each GET request $top specifies that only 5 emails
		should be acquired. However, the program will keep retrieving
		emails so long as the number of elements inside the 'messages"
		list is less than "max_results".'''
		response = httpx.get(next_link, headers=headers, params=params)

		if response.status_code != 200:
			raise Exception(f'Failed to retrieve emails: {response.json()}')
		
		# Extract the current batch of email messages from value and
		# add them to messages.
		json_response = response.json()
		messages.extend(json_response.get('value', []))

		# Use the @odata.nextLink property (provided by Microsoft Graph)
		# to fetch the next page.
		next_link = json_response.get('@odata.nextLink', None)

		# Clear params for subsequent requests since these parameters
		# are automatically included in the next_link URL returned by
		# the API.
		params = None

		# If the next batch would exceed max_results, adjust $top to
		# fetch only the remaining items.
		if next_link and len(messages) + top > max_results:
			# Modify only the $top parameter in the subsequent request.
			params = {
				'$top': max_results - len(messages)
			}

	'''
	Limits the returned list of messages to the first max_results
	items, so that the final result never exceeds max_results.

	This concept is known as list slicing.'''
	return messages[:max_results]

def get_sub_folders(headers, folder_id):
	# Notice how the endpoint in this function requires the folder ID
	# of the parent folder, so that its subfolders can be obtained.
	endpoint = f'{MS_GRAPH_BASE_URL}/me/mailFolders/{folder_id}/childFolders'

	# Send a GET request to the endpoint.
	response = httpx.get(endpoint, headers=headers)

	# Raise an exception if the HTTP response status code is 4xx or 5xx.
	response.raise_for_status()

	'''
	Include the 'value' key, so that the folder object is returned.
	An empty list is returned if the folder is not found.

	'value' is one of the keys in the dictionary that is returned.

	The HTTP response body is received as a raw string (or bytes).

	.json() parses this string into native Python data types such as
	dictionaries.'''
	print(f'outlook.py type(response): {type(response)}')

	return response.json().get('value', [])


def search_messages(headers, search_query, filter=None,
										folder_id=None, fields='*', top=5, max_results=100):
	# Including folder_id in the search_messages function modifies the
	# scope of the search operation by specifying a target folder to
	# search within.
	if folder_id is None:
		endpoint = f'{MS_GRAPH_BASE_URL}/me/messages'
	else:
		endpoint = f'{MS_GRAPH_BASE_URL}/me/mailFolders/{folder_id}/messages'

	params = {
		# The $search query parameter specifies the content
		# that will be searched for.
		'$search': f'"{search_query}"',

		'''
		The $filter query parameter narrows down the results through
		applying a boolean expression to each resource. The items
		returned are the ones where the expressions evaluate to true.
		
		receivedDateTime ge 2025-03-01 would filter emails received
		after the 1st of March 1, 2025.

		The ge operator stands for "greater than or equal to".
		'''
		'$filter': filter,

		# The $select query parameter indicates the fields to include
		# in responses.

		# '*' ensures that all properties of each message, such as subject,
		# from, toRecipients, body, receivedDateTime, etc. are returned.
		'$select': fields,

		# $top limits the results to the smaller of "top" or "max_results".
		'$top': min(top, max_results)
	}

	messages = []

	# Will store the URL of the next page containing emails.
	next_link = endpoint

	# The while loop will persist given that the "next_link" variable
	# is not an empty string and that the size of the "messages" list
	# or the number of elements in it is less than "max_results".
	while next_link and len(messages) < max_results:
		response = httpx.get(next_link, headers=headers, params=params)
		response.raise_for_status()

		if response.status_code != 200:
			raise Exception(f'Failed to retrieve emails: {response.json()}')

		# Parse the string into a native Python data type such as a dictionary.
		json_response = response.json()

		# Retrieve the current page of email results from the
		# API response and add them to the messages list.
		messages.extend(json_response.get('value', []))

		'''
		This line retrieves the pagination link from the Microsoft Graph
		API response, which points to the next page of results.

		The @odata.nextLink property in the response indicates whether
		there are more results available and provides the URL to fetch
		them.

		get(): Safely retrieves the @odata.nextLink value from the JSON response.
		'''
		next_link = json_response.get('@odata.nextLink', None)

		# Clear the parameters for subsequent queries.
		params = None

		if next_link and len(messages) + top > max_results:
			# Adjust the number of items to fetch in the next page
			# to avoid exceeding max_results.
			params = {
				'$top': max_results - len(messages)
			}
	# Ensures the returned list never exceeds max_results.
	return messages[:max_results]