import os
from pathlib import Path
import httpx
from dotenv import load_dotenv
from manual_ms_graph import get_access_token, MS_GRAPH_BASE_URL
from list_folder_and_files import list_folder_children

def download_file(headers, file_id, file_name):
  print(f'\nfile_id: {file_id}\n'
        f'file_name: {file_name}')

  url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{file_id}/content'

  response = httpx.get(url, headers=headers)

  if response.status_code == 302:
    # 302 indicates that the file was found.
    download_location = response.headers['location']

    response_file_download = httpx.get(download_location)

    with open(file_name, 'wb') as file:
      file.write(response_file_download.content)
    print(f'\nFile \"{file_name}\" downloaded successfully.')
  else:
    print(f'\nFailed to download file with ID {file_id}.')
    print(f'Description:\n{response.json()}')

def main():
  load_dotenv()

  APPLICATION_ID = os.getenv('APPLICATION_ID')

  CLIENT_SECRET = os.getenv('CLIENT_SECRET')

  SCOPES = ['User.Read', 'Files.ReadWrite.All']

  try:
    access_token = get_access_token(
      # The application ID is referred
      # to as the client ID.
      application_id=APPLICATION_ID,
      client_secret=CLIENT_SECRET,
      scopes=SCOPES
    )

    headers = {
      'Authorization': 'Bearer ' + access_token
    }

    '''
    The ID of the folder containing files
    that will be downloaded.'''
    folder_id = '66AF906D87EB4A94%21sa9a76508d6834eb681a0b9b3bd7b32b4'

    # Once the entire URL has been seen, it becomes
    # clear where the folder ID came from:
    # https://onedrive.live.com/?id=66AF906D87EB4A94%21sa9a76508d6834eb681a0b9b3bd7b32b4&cid=66AF906D87EB4A94

    '''
    The directory where the files will be downloaded.

    You must manually create the 'Downloads' directory/folder
    in "python_for_onedrive" before executing this program.
    Make sure that it is located in the same directory
    as the program.'''
    target_dir = Path('Downloads')

    files = list_folder_children(headers, folder_id)

    for file in files:
      if 'file' in file:
        file_id = file['id']
        download_file(headers, file_id, target_dir / file['name'])
  except Exception as err:
    print(f'Error: {err}')

# main()