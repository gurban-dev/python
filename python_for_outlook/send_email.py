import os
from pathlib import Path
import httpx
from dotenv import load_dotenv
from ms_graph import get_access_token, MS_GRAPH_BASE_URL
from outlook import create_attachment

def draft_message_body(subject, attachments):
  # The structure of the message object comes from
  # the Microsoft Graph API's message resource:
  # https://learn.microsoft.com/en-us/graph/api/resources/message?view=graph-rest-1.0#properties
  message = {
    'subject': subject,
    'body': {
      'contentType': 'HTML',
      'content': 'This is a test email sent from Python.'
    },
    'toRecipients': [
      {
        'emailAddress': {
          'address': 'dennisgurban43@gmail.com'
        }
      },
      {
        'emailAddress': {
          'address': 'dennisgurban44@gmail.com'
        }
      }
    ],
    # Include the secondary recipients in the
    # Outlook email message who receive a copy
    # of the email for informational purposes.
    'ccRecipients': [
      {
        'emailAddress': {
          'address': 'youssefabdul6@gmail.com'
        }
      }
    ],
    'importance': 'high',
    'attachments': attachments
  }
  return message

def main():
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
    The Authorization: Bearer {access_token} header
    validates the request by proving the app has
    permission to access emails in Outlook.'''
    headers = {
      'Authorization': 'Bearer ' + access_token
    }

    '''
    Path() returns a Path object pointing to the
    attachments directory where attachment files
    are stored.

    This attachments directory will have to be created
    if it does not already exist in the same directory
    as this program.

    The ./ indicates that "attachments" is in the current
    directory that this program is located in.'''
    dir_attachments = Path('./attachments')

    '''
    Python list data structure to store the files that
    are to be attached to the email message. The
    create_attachment() function is necessary to invoke
    because it converts each file to an attachment object.'''
    attachments = [
      create_attachment(attachment)

      # iterdir() generates an iterator over all files and
      # directories in dir_attachments.
      for attachment in dir_attachments.iterdir()

      # Filters out directories/exclude the directories
      # (e.g., subfolder) and only keeps files.
      if attachment.is_file()
    ]

    endpoint = f'{MS_GRAPH_BASE_URL}/me/sendMail'

    # Send two emails.
    for i in range(1, 3):
      message = {
        'message': draft_message_body(
          'Test Email with Attachments_' + str(i), attachments)
      }

      '''
      A HTTP POST request is needed to send an email message.
      To send a JSON message using httpx.post, a Python
      dictionary can be directly passed, and then assigned to
      the "json" parameter.'''
      response = httpx.post(endpoint, headers=headers, json=message)

      # For debugging:
      # print(f'response.status_code: {response.status_code}')

      # The 202 status code indicates that the server has
      # received and understood a client's request. The
      # server may still be processing it.
      if response.status_code != 202:
        # "text" is an attribute of the httpx.Response class
        # that holds the response body as a string.
        raise Exception(f'Failed to send email: {response.text}')
      print('Email sent successfully.')
  except httpx.HTTPStatusError as err:
    print(f'HTTP Error: {err}')
  except Exception as err:
    print(f'Error: {err}')

main()