import os
import httpx
from dotenv import load_dotenv
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL

def generate_share_link(headers, file_id):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{file_id}/createLink'

  payload = {
    # {view, edit, embed}
    'type': 'view',

    # {anonymous, organization, users}
    'scope': 'anonymous',

    # yyyy-MM-ddTHH:mm:ssZ
    # 'expirationDateTime': expiration
    # 'password': ''
  }

  response = httpx.post(url, headers=headers, json=payload)

  if response.status_code == 200:
    print(f'Share link for file (file ID: {file_id}):')
    return response.json()['link']['webUrl']
  else:
    print(f'Failed to generate link for file with ID {file_id}.')
    print(f'Description:\n{response.json()['error']['message']}')

def generate_download_link(headers, file_id):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/items/{file_id}/content'
  response = httpx.get(url, headers=headers, follow_redirects=True)

  if response.status_code == 200:
    download_link = response.url
    print(f'Download link for file (file ID: {file_id}): {download_link}')
    return str(download_link)
  else:
    print(f'Failed to generate download link for file with ID {file_id}.')
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

    # share_link = generate_share_link(headers, file_id)
    # print('share_link:', share_link)

    # download_link = generate_download_link(headers, file_id)
    # print('download_link:', download_link)
  except Exception as err:
    print(f'Error: {err}')

main()