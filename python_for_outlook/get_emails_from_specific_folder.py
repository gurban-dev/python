import os
from dotenv import load_dotenv
import httpx
from ms_graph import get_access_token

# Reference the name of a module without the py file extension.
from outlook import search_folder, get_sub_folders, get_messages

# This program is making use of the Microsoft Graph API
# to retrieve emails from a Microsoft Outlook account.

def main():
  # Load the environment variables into the Python environment.
  load_dotenv()

  APPLICATION_ID = os.getenv('APPLICATION_ID')

  CLIENT_SECRET = os.getenv('CLIENT_SECRET')

  SCOPES = ['User.Read', 'Mail.ReadWrite']

  try:
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
    
    # Name of the folder where the program will retrieve emails.
    # Verify that this name matches one of the folders in a person's
    # email.
    folder_name = 'Inbox'

    # A Microsoft Graph API response object is returned
    # by search_folder().
    target_folder = search_folder(headers, folder_name)

    # Get the ID of the folder.
    folder_id = target_folder['id']

    # With the folder ID, the emails can now be retrieved.
    messages = get_messages(headers, folder_id)

    print(f'\nmessages: {messages}')

    for message in messages:
      print(f'Subject: {message['subject']}\n'
             '-' * 50)
      
    # Get the subfolders inside of the "Inbox" folder.
    sub_folders = get_sub_folders(headers, folder_id)

    # Iterate over all of the subfolders inside "Inbox".
    for sub_folder in sub_folders:
      if sub_folder['displayName'].lower() == 'sub folder':
        # Obtain the ID of the subfolder.
        sub_folder_id = sub_folder['id']

        # Now that the program has access to the ID of the
        # subfolder, it will acquire the emails within it.
        messages = get_messages(headers, sub_folder_id)

        for message in messages:
          print(f'Sub Folder Name: {sub_folder['displayName']}\n'
                f'Subject: {message['subject']}\n'
                '-' * 50)
  except httpx.HTTPStatusError as err:
    print(f'HTTP Error: {err}')
  except Exception as err:
    print(f'Error: {err}')

main()