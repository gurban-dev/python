import os
from textwrap import dedent
import httpx
from dotenv import load_dotenv
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL

def create_folder(headers, folder_name, parent_folder_id=None):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/root/children'

  if parent_folder_id:
    url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{parent_folder_id}/children'

  payload = {
    'name': folder_name,
    'folder': {},
    # Creates a folder with a different name if
    # there is already an exisitng one with the
    # same name.
    # '@microsoft.graph.conflictBehavior': 'rename'
    '@microsoft.graph.conflictBehavior': 'fail'
  }

  response = httpx.post(url, headers=headers, json=payload)

  if response.status_code == 201:
    data = response.json()
    return data
  else:
    print(f'Failed to create folder \"{folder_name}\"')
    print(f'Description:\n{response.json()['error']['message']}')
    return None
  
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

    folder_name = 'test_folder'

    created_folder = create_folder(headers, folder_name)

    if created_folder:
      print(dedent(
        f'''
          Folder ID: {created_folder['id']}
          Folder name: {created_folder['name']}
          Folder web url: {created_folder['webUrl']}
          Folder location: {created_folder['parentReference']['path']}
        ''')
      )

      # Create subfolder
      subfolder_name = 'test_subfolder'

      created_subfolder = create_folder(headers, subfolder_name, created_folder['id'])

      if created_subfolder:
        print(dedent(
          f'''
            Subfolder ID: {created_subfolder['id']}
            Subfolder name: {created_subfolder['name']}
            Subfolder web url: {created_subfolder['webUrl']}
            Subfolder location: {created_subfolder['parentReference']['path']}
          ''')
        )
  except Exception as err:
    print(f'Error: {err}')

main()