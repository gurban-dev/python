import requests
from requests.exceptions import Timeout

def main():
  try:
    # Compatible with both .json() and .text.
    url = 'https://www.w3schools.com/python/demopage.js'

    # Compatible with .text, but not with .json().
    # url = 'https://www.example.com/'

    # The following is a keyword argument because the parameter
    # name "timeout" is included:
    # timeout=5

    # The timeout parameter in requests.get() specifies the
    # maximum time, in seconds, that the client will wait for
    # a response from the server before raising a
    # requests.exceptions.Timeout exception.
    response = requests.get(url, timeout=5)

    print('type(response):', type(response))

    # Raise an HTTPError for a bad status code.
    response.raise_for_status()

    # If the server's response body is a valid JSON object like:
    # { "name": "Alice", "age": 25 }, .json() will return a
    # dictionary.
    data = response.json()

    # The "text" property returns a string.
    # data = response.text

    print('\ndata:', data)

    print('\ntype(data):', type(data))
  except ConnectionError:
    print('Failed to connect to the server. Check your internet or the URL.')
  except Timeout:
    print('The request timed out. The server took too long to respond.')

if __name__ == '__main__':
  main()