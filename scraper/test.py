import requests
from bs4 import BeautifulSoup

# Send a GET request to google.com
response = requests.get("https://www.google.com")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Get the title tag
title = soup.title.string

print("Title of the page:", title)