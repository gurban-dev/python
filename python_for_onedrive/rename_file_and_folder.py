import os
import httpx
from dotenv import load_dotenv
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL

def rename_item(headers, file_id, new_name):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{file_id}'

  payload = {
    'name': new_name
  }

  response = httpx.patch(url, headers=headers, json=payload)

  if response.status_code == 200:
    print(f'File (file ID: {file_id}) renamed successfully.')
  else:
    print(f'Failed to rename file with ID {file_id}.')
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

    file_id = '4467206A6E7732FA!s23dd01256baa4e05816f15b95a8ee34f'
    new_name = 'Email Directory'

    rename_item(headers, file_id, new_name)
  except Exception as err:
    print(f'Error: {err}')

main()