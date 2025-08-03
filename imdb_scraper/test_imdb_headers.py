import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html",
    "Connection": "keep-alive"
}

url = "https://www.imdb.com/chart/top/"

response = requests.get(url, headers=headers)
print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
rows = soup.select("tbody.lister-list tr")
print("Películas encontradas:", len(rows))