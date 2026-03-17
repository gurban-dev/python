import os
import httpx
from dotenv import load_dotenv
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL

def copy_file(headers, file_id, target_folder_id):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{file_id}/copy'

  payload = {
    'parentReference': {
      'id': target_folder_id
    },
    # '@microsoft.graph.conflictBehavior': 'rename'
  }

  response = httpx.post(url, headers=headers, json=payload)

  if response.status_code == 202:
    print(f'File (file ID: {file_id}) copied successfully.')
  else:
    print(f'Failed to copy file with ID {file_id}.')
    print(f'Description:\n{response.json()['error']['message']}')

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

    file_id = '4467206A6E7732FA%21sfeeffa5e4ccf4997b3fb624a7a90674b'

    target_folder_id = '4467206A6E7732FA%21s86bdfde3b1b44f9380349d9edecf1450'

    copy_file(headers, file_id, target_folder_id)
  except Exception as err:
    print(f'Error: {err}')

main()