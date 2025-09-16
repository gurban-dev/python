import os
import httpx
from dotenv import load_dotenv
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL
from list_folder_and_files import list_folder_children

def delete_item(headers, file_id):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{file_id}'

  response = httpx.delete(url, headers=headers)

  if response.status_code == 204:
    print(f'File (file ID: {file_id} deleted successfully.')
  else:
    print(f'Failed to delete file with ID {file_id}.')
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

    folder_id = '4467206A6E7732FA%21s8c5c1685a4454903a7fbae1f059ca127'

    # For deleting a folder.
    delete_item(headers, folder_id)

    # For deleting files.
    # files = list_folder_children(headers, folder_id)

    # for file in files:
    #   if 'file' in file:
    #     print(file['name'])
    #     file_id = file['id']
    #     delete_item(headers, file_id)
  except Exception as err:
    print(f'Error: {err}')

main()