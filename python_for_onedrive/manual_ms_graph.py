import os
import webbrowser
import msal
from dotenv import load_dotenv

MS_GRAPH_BASE_URL = 'https://graph.microsoft.com/v1.0'

# Request an access token
def get_access_token(application_id, client_secret, scopes):
  print('python_for_onedrive/manual_ms_graph.py')

  client = msal.ConfidentialClientApplication(
    client_id=application_id,
    client_credential=client_secret,
    authority='https://login.microsoftonline.com/consumers/'
  )

  auth_request_url = client.get_authorization_request_url(scopes)

  webbrowser.open(auth_request_url)

  authorization_code = input('\nEnter the authorization code: ')

  token_response = client.acquire_token_by_authorization_code(
    code=authorization_code,
    scopes=scopes
  )

  if 'access_token' in token_response:
    return token_response['access_token']
  else:
    raise Exception('Failed to acquire access token ' + str(token_response))

def main():
  load_dotenv()

  APPLICATION_ID = os.getenv('APPLICATION_ID')

  CLIENT_SECRET = os.getenv('CLIENT_SECRET')

  SCOPES = ['User.Read', 'Files.ReadWrite.All']

  try:
    access_token = get_access_token(
      application_id=APPLICATION_ID,
      client_secret=CLIENT_SECRET,
      scopes=SCOPES
    )

    headers = {
      'Authorization': 'Bearer ' + access_token
    }

    print(f'headers: {headers}\n')
  except Exception as err:
    print(f'Error: {err}')

# main()