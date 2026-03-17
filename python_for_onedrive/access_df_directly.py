import os
from pathlib import Path
from textwrap import dedent
from dotenv import load_dotenv
from download_files import download_file
from list_folder_and_files import list_folder_children
from manual_ms_graph import get_access_token, MS_GRAPH_BASE_URL

# Import everything from the
# empty_status_column module.
from empty_status_column import *

# Styles the email sent to make it appear
# more official.
from get_html_content import get_html_content

import requests
import pandas as pd
import httpx
import sys

sys.path.append('/home/deniz/python/king/python_for_outlook')

from outlook import create_attachment # type: ignore

def get_dataframe(headers):
  # Link for the Excel spreadsheet in OneDrive:
  # https://onedrive.live.com/personal/66af906d87eb4a94/_layouts/15/doc2.aspx?resid=0f9c5d8f-0e53-4ba4-ab12-452c17a3a95c&cid=66af906d87eb4a94&ct=1744442033750&wdOrigin=OFFICECOM-WEB.MAIN.EDGEWORTH&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=387200b0-d3f2-4491-adc2-f7462e49f6c7

  FILE_ID = '66AF906D87EB4A94!s0f9c5d8f0e534ba4ab12452c17a3a95c'
  WORKSHEET_ID = 'Sheet1'

  url = f"https://graph.microsoft.com/v1.0/me/drive/items/{FILE_ID}/workbook/worksheets/{WORKSHEET_ID}/range(address='A1:Z500')"

  # Sending an HTTP GET request.
  response = requests.get(url, headers=headers)

  # A status code of 200 indicates that the HTTP
  # request was successfully processed.
  if response.status_code == 200:
    # Parse the JSON response to extract values.
    data = response.json()

    values = data.get("values", [])

    # Assuming first row contains headers.
    df = pd.DataFrame(values[1:], columns=values[0])

    # Remove columns consisting of entirely
    # NaN (not a number) values.
    df = df.loc[:, df.columns != '']

    # Removes rows that have empty strings
    # in every column.
    df = df.loc[~(df == '').all(axis=1)]

    return df
  else:
    print(f'\nFailed to fetch data: {response.status_code}'
          f' - {response.text}')

def update_status_in_onedrive(
    headers, index, column_letter, status):
  # Add 1, so that the header row
  # is skipped and not edited.
  row_no = index + 2

  range_address = f"{column_letter}{row_no}"

  '''
  Prepare the body for the PATCH request
  (the updated value for the status column).

  The program inserts "sent" or "failed" in the
  Excel spreadsheet depending on whether the email
  was sent successfully.'''
  data = {
    # If the email was successfully sent:
    # "values": [['sent']]
    "values": [[status]]
  }

  FILE_ID = '66AF906D87EB4A94!s0f9c5d8f0e534ba4ab12452c17a3a95c'
  WORKSHEET_ID = 'Sheet1'

  # Send the PATCH request to update
  # the cell in the Excel workbook.
  url = f"https://graph.microsoft.com/v1.0/me/drive/items/{FILE_ID}/workbook/worksheets/{WORKSHEET_ID}/range(address='{range_address}')"

  # The HTTP PATCH request is utilised when updating
  # only some of the fields in a database row/record.
  response = httpx.patch(url, headers=headers, json=data)

  if response.status_code == 200:
    print(f'\nRow {row_no} status updated in '
          f'OneDrive: \"{status}\"')
  else:
    print(f'\nFailed to update status in OneDrive:\n'
          f'{response.status_code} - {response.text}')

'''
Declaring a function to determine if a row has
missing values was necessary because there was
difficulty with removing all of the rows with
missing values from the "df" DataFrame.'''
def row_is_missing_data(row):
  for key in row.keys():
    # Assume key was "to":
    # row[key] would be:
    # dennisgurban44@gmail.com
    if row[key] == '' and key != 'status':
      return True
  return False

def send_email_to_all():
  # \" is a double quote escape sequence.
  return input(dedent('''
    Enter \"yes\" if you would like to send the
    email to all of your co-workers. Anything
    else will be interpreted as \"no\": '''))

def download_attachment(headers, file_name):
  folder_id = '66AF906D87EB4A94%21sa9a76508d6834eb681a0b9b3bd7b32b4'

  files = list_folder_children(headers, folder_id)

  target_dir = Path('Downloads')

  for file in files:
    if 'file' in file and file_name == file['name']:
      file_id = file['id']

      download_file(headers, file_id, target_dir / file['name'])

def get_attachments(file_name):
  dir_attachments = Path('./Downloads')

  return [
    create_attachment(attachment)

    for attachment in dir_attachments.iterdir()

    if attachment.is_file() and attachment.name == file_name
  ]

def send_emails(headers):
  # Get the Pandas DataFrame 
  df = get_dataframe(headers)

  if send_email_to_all() == 'yes':
    empty_status_column(headers, df)

    # Get the Pandas DataFrame again
    # since the "status" column has
    # been updated.
    df = get_dataframe(headers)

  # Get the Pandas DataFrame 
  df = get_dataframe(headers)

  endpoint = f'{MS_GRAPH_BASE_URL}/me/sendMail'

  # Iterate through the rows in the DataFrame.
  for index, row in df.iterrows():
    if row_is_missing_data(row) or \
      row['status'] == 'sent':
      continue

    file_name = row['attachment']

    download_attachment(headers, file_name)

    salutation_and_name = row['salutation'] + ' ' + \
                          row['preferred name'] + '. '
    email_body = row['body']

    message = {
      'message': {
        'subject': row['subject'],
        'body': {
          'contentType': 'HTML',
          'content': get_html_content(
            salutation_and_name, email_body)
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
        'attachments': get_attachments(file_name)
      }
    }

    # Send the email by making an HTTP POST request.
    response = httpx.post(endpoint, headers=headers, json=message)

    # 'status' is the value in row 1 of column J.
    # find_letter_value_for_col() is defined
    # in the empty_status_column.py module.
    column_letter = find_letter_value_for_col(df, 'status')

    if response.status_code != 202:
      update_status_in_onedrive(
        headers, index, column_letter, 'failed')

      raise Exception(f'Failed to send email: {response.text}')

    update_status_in_onedrive(headers, index, column_letter, 'sent')

    print('\nEmail sent successfully.')

def main():
  load_dotenv()

  APPLICATION_ID = os.getenv('APPLICATION_ID')

  CLIENT_SECRET = os.getenv('CLIENT_SECRET')

  SCOPES = ['User.Read', 'Files.ReadWrite.All']

  try:
    # with sync_playwright() as playwright:
    #   access_token = get_access_token(
    #     playwright,
    #     application_id=APPLICATION_ID,
    #     client_secret=CLIENT_SECRET,
    #     scopes=SCOPES
    #   )

    access_token = get_access_token(
      # The application ID is also referred
      # to as the client ID.
      application_id=APPLICATION_ID,
      client_secret=CLIENT_SECRET,
      scopes=SCOPES
    )

    headers = {
      'Authorization': 'Bearer ' + access_token
    }

    send_emails(headers)
  except Exception as err:
    print(f'Error: {err}')

main()