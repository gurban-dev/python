import os
import httpx
from dotenv import load_dotenv
from automate_ms_graph import get_access_token, MS_GRAPH_BASE_URL

def search_file(headers, query):
  url = f'{MS_GRAPH_BASE_URL}/me/drive/search(q=\'{query}\')'

  response = httpx.get(url, headers=headers)

  if response.status_code == 200:
    return response.json()
  else:
    print(f'Failed to search for files with query {query}')
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

    query = 'test'
    results = search_file(headers, query)

    for result in results['value']:
      print(result['name'])
  except Exception as err:
    print(f'Error: {err}')

main()