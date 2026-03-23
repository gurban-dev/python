import requests
from requests.exceptions import Timeout, ConnectionError

def main(test_case=""):
    try:
        if test_case == 'timeout':
            url = 'https://www.example.com/'
            response = requests.get(url, timeout=0.0001)

        elif test_case == 'connection':
            url = 'http://this-domain-does-not-exist-123456789.com'
            response = requests.get(url, timeout=5)

        else:
            url = 'https://www.w3schools.com/python/demopage.js'
            response = requests.get(url, timeout=5)
            response.raise_for_status()

        if test_case in ("timeout", "connection"):
            data = response.text
        else:
            try:
                data = response.json()
            except ValueError:
                data = response.text

        print("data:", data)

    except ConnectionError:
        print('Failed to connect to the server. Check your internet or the URL.')
    except Timeout:
        print('The request timed out. The server took too long to respond.')
    except Exception as e:
        print(f'\nAn error occurred:\n{e}')


if __name__ == '__main__':
    main()
    main('timeout')
    main('connection')