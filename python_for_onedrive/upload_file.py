import os
from pathlib import Path
from textwrap import dedent
import httpx
from dotenv import load_dotenv
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL

def upload_file(headers, file_path, folder_id=None, if_exists='rename'):
  base_name = os.path.basename(file_path)

  url = f'{MS_GRAPH_BASE_URL}/me/drive/root:/{base_name}:/content'

  if if_exists == 'rename':
    headers['Content-Type'] = 'application/octet-stream'
    params = {
      '@microsoft.graph.conflictBehavior': 'rename'
    }
  elif if_exists == 'replace':
    params = {}
  else:
    return None

  with open(file_path, 'rb') as file:
    response = httpx.put(url, headers=headers, params=params, data=file)

  if response.status_code in (200, 201):
    print(f'File \"{file_path}\" uploaded successfully.')
  else:
    print(f'Failed to upload file \"{file_path}\"')
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

    asset_folder = Path('assets')
    files = asset_folder.glob('*')

    for file in files:
      file_path = str(file)

      folder_id = '4467206A6E7732FA%21sccab2592fd0d45f9a0dd83b03e659e3e'

      file_metadata = upload_file(headers, file_path, folder_id)

      if file_metadata:
        print(dedent(
          f'''
            File ID: {file_metadata['id']}
            File parent ID: {file_metadata['parentReference']['path']}
            File web url: {file_metadata['webUrl']}
            {'-' * 50}
          ''')
        )
  except Exception as err:
    print(f'Error: {err}')

main()