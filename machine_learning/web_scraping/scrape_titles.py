import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://news.ycombinator.com/"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
  # Parse the page content
  soup = BeautifulSoup(response.text, 'html.parser')
  
  # Find all the article title links
  titles = soup.find_all('a', class_='storylink') or soup.find_all('span', class_='titleline')

  print("Top Articles from Hacker News:\n")
  for idx, title in enumerate(titles, start=1):
    # Get the text content of the link
    print(f"{idx}. {title.get_text()}")
else:
  print(f"Failed to retrieve page. Status code: {response.status_code}")