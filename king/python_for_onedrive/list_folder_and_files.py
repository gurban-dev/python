import os
from textwrap import dedent
import httpx
from dotenv import load_dotenv
from manual_ms_graph import get_access_token, MS_GRAPH_BASE_URL

def list_root_folder(headers):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/root/children'

  response = httpx.get(url, headers=headers)

  if response.status_code == 200:
    data = response.json()
    return [item for item in data['value']]
  else:
    print(f'Failed to list root folder: {response.status_code}')
    return []
  
def list_folder_children(headers, folder_id):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{folder_id}/children'

  response = httpx.get(url, headers=headers)

  if response.status_code == 200:
    data = response.json()
    return [item for item in data['value']]
  else:
    print(f'Failed to list children of folder {folder_id}: {response.status_code}')
    return []
  
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

    root_folder = list_root_folder(headers)
    for folder in root_folder:
      if 'folder' in folder:
        print(dedent(
          f'''
            Folder ID: {folder['id']}
            Folder name: {folder['name']}
            Folder web url: {folder['webUrl']}
            Folder created date: {folder['createdDateTime']}
            Created by: {folder['createdBy']['user']['displayName']}
            Folder modified date: {folder['lastModifiedDateTime']}
            Last modified by: {folder['lastModifiedBy']['user']['displayName']}
            Folder parent ID: {folder['parentReference']['id']}
            Item Count: {folder['folder']['childCount']}
            {'-' * 50}
          ''')
        )
      elif 'file' in folder:
        print(dedent(
          f'''
            Folder ID: {folder['id']}
            Folder name: {folder['name']}
            Folder web url: {folder['webUrl']}
            File size (in KB): {folder['size'] / 1024:.2f}
            File created date: {folder['createdDateTime']}
            Created by: {folder['createdBy']['user']['displayName']}
            Folder modified date: {folder['lastModifiedDateTime']}
            Last modified by: {folder['lastModifiedBy']['user']['displayName']}
            Folder parent ID: {folder['parentReference']['id']}
            File Mime type: {folder['file']['mimeType']}
            {'-' * 50}
          ''')
        )
      print('-' * 50)

    # Obtain the folder ID through the URL:
    # https://onedrive.live.com/?id=4467206A6E7732FA%21sccab2592fd0d45f9a0dd83b03e659e3e&cid=4467206A6E7732FA

    # Notice how it is made up of the characters
    # between "id=" and "&cid=".
    folder_id = '4467206A6E7732FA%21sccab2592fd0d45f9a0dd83b03e659e3e'
    list_children = list_folder_children(headers, folder_id)

    for child in list_children:
      if 'folder' in child:
        print(dedent(
          f'''
            Folder ID: {child['id']}
            Folder name: {child['name']}
            Folder web url: {child['webUrl']}
            Folder created date: {child['createdDateTime']}
            Created by: {child['createdBy']['user']['displayName']}
            Folder modified date: {child['lastModifiedDateTime']}
            Last modified by: {child['lastModifiedBy']['user']['displayName']}
            Folder parent ID: {child['parentReference']['id']}
            Item Count: {child['folder']['childCount']}
            {'-' * 50}
          ''')
        )
      elif 'file' in child:
        print(dedent(
          f'''
            Folder ID: {child['id']}
            Folder name: {child['name']}
            Folder web url: {child['webUrl']}
            File size (in KB): {child['size'] / 1024:.2f}
            File created date: {child['createdDateTime']}
            Created by: {child['createdBy']['user']['displayName']}
            Folder modified date: {child['lastModifiedDateTime']}
            Last modified by: {child['lastModifiedBy']['user']['displayName']}
            Folder parent ID: {child['parentReference']['id']}
            File Mime type: {child['file']['mimeType']}
            {'-' * 50}
          ''')
        )
      print('-' * 50)
  except Exception as err:
    print(f'Error: {err}')

# main()