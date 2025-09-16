import pandas as pd
import os
from pathlib import Path
import httpx
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL
from dotenv import load_dotenv
import sys

sys.path.append('/home/deniz/python/king/python_for_outlook')

from outlook import create_attachment

def send_emails(headers, attachments):
  # Assign the file path for the Excel spreadsheet
  # containing the email addresses.
  file_path = './python_for_onedrive/Downloads/Email Automation.xlsx'

  # Create a Pandas dataframe.
  # The "names" property makes it possible to
  # specify the columns names in the dataframe.
  df = pd.read_excel(
    file_path, sheet_name='Sheet1', names=['name',
    'to', 'cc', 'from', 'subject', 'attachment', 'salutation',
    'body', 'closing signature'])

  endpoint = f'{MS_GRAPH_BASE_URL}/me/sendMail'

  '''
  How does iterrows() skip the header row in the DataFrame?
  The iterrows() method in Pandas iterates over all
  rows in the DataFrame, including the header row
  if present. However, in this case, the header row
  is effectively skipped because the DataFrame is
  created with explicitly defined column names
  (names=['name', 'to', 'cc', 'from', 'subject',
  'attachment', 'salutation', 'body', 'closing signature']).

  How does Pandas know that "name" corresponds to the
  "Preferred name" column title in the Excel workbook
  in OneDrive if the two names are different?
  Pandas does not automatically map "name" to "Preferred
  name" or any other column title in the Excel workbook
  unless explicitly instructed. In your code, you
  specify names=['name', ...] while reading the Excel
  file, which replaces the original column headers (e.g.,
  "Preferred name") with custom names provided in the names
  parameter. This means Pandas will use "name" as a column
  header regardless of what was originally present in the
  Excel workbook. If you want to retain and use original
  column headers, you should avoid using names or ensure it
  matches the actual headers in the file.'''

  # Iterate through the rows in the dataframe.
  for index, row in df.iterrows():
    content = row['salutation'] + ' ' + row['name'] + '. ' + row['body']

    message = {
      'message': {
        'subject': row['subject'],
        'body': {
          'contentType': 'HTML',
          'content': content
        },
        'toRecipients': [
          {
            'emailAddress': {
              'address': row['to']
            }
          }
        ],
        # Include the secondary recipients in the
        # Outlook email message who receive a copy
        # of the email for informational purposes.
        'ccRecipients': [
          {
            'emailAddress': {
              'address': row['cc']
            }
          }
        ],
        'importance': 'high',
        'attachments': attachments
      }
    }

    response = httpx.post(endpoint, headers=headers, json=message)

    if response.status_code != 202:
      raise Exception(f'Failed to send email: {response.text}')
    print('Email sent successfully.')

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

    headers = {
      'Authorization': 'Bearer ' + access_token
    }

    # The folder where the items to be attached
    # will come from.
    dir_attachments = Path('./python_for_onedrive/Downloads')

    attachments = [
      create_attachment(attachment)

      for attachment in dir_attachments.iterdir()

      if attachment.is_file()
    ]

    send_emails(headers, attachments)
  except httpx.HTTPStatusError as err:
    print(f'HTTP Error: {err}')
  except Exception as err:
    print(f'Error: {err}')

main()