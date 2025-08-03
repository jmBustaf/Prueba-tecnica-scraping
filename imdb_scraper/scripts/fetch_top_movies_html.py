import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Referer": "https://www.imdb.com/",
}

COOKIES = {
    "session-id": "136-7514078-2152549",
    "session-id-time": "2082787201l",
    "ubid-main": "133-1492162-1446361",
}

url = "https://www.imdb.com/chart/top/"

response = requests.get(url, headers=HEADERS, cookies=COOKIES)

if response.status_code == 200:
    with open("data/top_movies.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("✅ HTML guardado con éxito en data/top_movies.html")
else:
    print(f"Error al obtener la página: {response.status_code}")
