import requests
from bs4 import BeautifulSoup
url = "https://opentender.eu/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.get_text())