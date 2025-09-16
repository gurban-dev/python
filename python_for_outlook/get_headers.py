import os
import httpx
from ms_graph import get_access_token
from dotenv import load_dotenv

def get_headers(SCOPES):
  load_dotenv()
  
  APPLICATION_ID = os.getenv('APPLICATION_ID')

  CLIENT_SECRET = os.getenv('CLIENT_SECRET')

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

    print('\nget_headers.py headers:', headers)

    return headers
  except httpx.HTTPStatusError as err:
    print(f'HTTP Error: {err}')
  except Exception as err:
    print(f'Error: {err}')