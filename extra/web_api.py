import requests
from bs4 import BeautifulSoup


url = 'https://www.indeed.com/jobs?q=web+developer&l=New+York'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
print(results.prettify())
