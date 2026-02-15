import requests
from requests.exceptions import Timeout

def main(test_case=""):
  try:
    if test_case == 'timeout':
      # Compatible with .text, but not with .json().
      url = 'https://www.example.com/'
      response = requests.get(url, timeout=0.0001)

    elif test_case == 'connection':
      url = 'http://this-domain-does-not-exist-123456789.com'

      # The following is a keyword argument because the parameter
      # name "timeout" is included:
      # timeout=5

      # The 'timeout' parameter in requests.get() specifies the
      # maximum time, in seconds, that the client will wait for
      # a response from the server before raising a
      # requests.exceptions.Timeout exception.
      response = requests.get(url, timeout=5)
    else:
      # Compatible with both .json() and .text.
      url = 'https://www.w3schools.com/python/demopage.js'

      response = requests.get(url, timeout=5)

    # Raise an HTTPError for a bad status code.
    response.raise_for_status()

    if test_case == "timeout" or test_case or "connection":
      # The "text" property returns a string.
      data = response.text
    else:
      # If the server's response body is a valid JSON object like:
      # { "name": "Alice", "age": 25 }, .json() will return a
      # dictionary.
      data = response.json()

    print('type(response):', type(response), '\n')

    print('data:', data)

    print('\ntype(data):', type(data))
  except ConnectionError:
    print('Failed to connect to the server. Check your internet or the URL.')
  except Timeout:
    print('The request timed out. The server took too long to respond.')

  # The last except clause handles any generic exception.
  except Exception as e:
    print(f'\nAn error occurred:\n{e}')

# If this module send_request.py is imported, the main() function
# will not automatically be executed as a result of the import.

# The __name__ dunder variable is equal to '__main__' only when
# this Python file is directly run:
# python3 send_request.py

# A dunder variable is one that has two leading and trailing undercores.
if __name__ == '__main__':
  main()

  main('timeout')

  main('connection')