import os
import httpx
from dotenv import load_dotenv
from ms_graph import get_access_token
from outlook import search_messages

def main():
  # Load the environment variables
  # into the Python environment.
  load_dotenv()

  # Obtain the environment variables declared
  # in the .env file.
  APPLICATION_ID = os.getenv('APPLICATION_ID')

  CLIENT_SECRET = os.getenv('CLIENT_SECRET')

  # Configure/establish the permissions.
  SCOPES = ['User.Read', 'Mail.ReadWrite']

  try:
    '''
    Retrieve an access token because it serves as the key to
    authenticate and authorize requests to the Microsoft Graph API.'''
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
    If you do a search on messages and specify only a value without
    specific message properties, the search is carried out on the
    default search properties of from, subject, and body.'''
    search_query = 'Microsoft Cash Reward'

    '''
    The first five emails will be searched because 5 is the
    default parameter for the "top" parameter that makes up
    the search_messages() function definition.
    
    "messages" is assigned a list of dictionaries, where each dictionary
    represents an email message retrieved from the Microsoft Graph Search
    API.'''
    messages = search_messages(headers, search_query)

    print(f'type(messages): {type(messages)}')

    '''
    All of the keys in the dictionary that is returned can be viewed at
    the following link:
    https://learn.microsoft.com/en-us/graph/api/message-get?view=graph-rest-1.0&tabs=http#response-1
    '''

    for index, mail_message in enumerate(messages):
      # Save the results in a sharepoint.
      print(f'''
        Email {index + 1}\n
        Subject: {mail_message['subject']}\n
        From: {mail_message['from']['emailAddress']['name'],
               f'{mail_message['from']['emailAddress']['address']}'}\n
        Received Date Time: {mail_message['receivedDateTime']}\n
        Body Preview: {mail_message['bodyPreview']}\n''')
      print('-' * 150)
  except httpx.HTTPStatusError as err:
    print(f'HTTP Error: {err}')
  except Exception as err:
    print(f'Error: {err}')

main()