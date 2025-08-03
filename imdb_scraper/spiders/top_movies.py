import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) "
        "Gecko/20100101 Firefox/119.0"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1"
}

BASE_URL = "https://www.imdb.com"
TOP_URL = f"{BASE_URL}/chart/top/"

def get_soup(url):
    try:
        session = requests.Session()
        response = session.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.RequestException as e:
        print(f"Error al obtener {url}: {e}")
        return None

def parse_top_movies():
    soup = get_soup(TOP_URL)
    if not soup:
        return []
    
    with open(os.path.join(OUTPUT_DIR, "imdb_debug.html"), "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    rows = soup.select("tbody.lister-list tr")
    print(f"Películas encontradas: {len(rows)}")
    movies = []

    for row in rows[:50]:
        title_tag = row.select_one("td.titleColumn a")
        year_tag = row.select_one("td.titleColumn span.secondaryInfo")
        rating_tag = row.select_one("td.imdbRating strong")

        if not title_tag or not year_tag or not rating_tag:
            continue

        title = title_tag.get_text(strip=True)
        year = year_tag.get_text(strip=True).strip("()")
        rating = rating_tag.get_text(strip=True)
        detail_url = BASE_URL + title_tag["href"].split("?")[0]

        movie_data = {
            "title": title,
            "year": year,
            "rating": rating,
            "url": detail_url
        }

        movie_data.update(parse_movie_detail(detail_url))
        movies.append(movie_data)
        time.sleep(1.5)

    return movies

def parse_movie_detail(url):
    soup = get_soup(url)
    if not soup:
        return {"duration": None, "metascore": None, "actors": []}

    duration_tag = soup.select_one("li[data-testid='title-techspec_runtime']")
    metascore_tag = soup.select_one("span.metacriticScore span")
    actor_tags = soup.select("a[data-testid='title-cast-item__actor']")[:3]

    duration = duration_tag.get_text(strip=True).replace("m", "") if duration_tag else None
    metascore = metascore_tag.get_text(strip=True) if metascore_tag else None
    actors = [tag.get_text(strip=True) for tag in actor_tags]

    return {
        "duration": duration,
        "metascore": metascore,
        "actors": actors
    }

def save_to_csv(movies, filepath):
    df = pd.DataFrame(movies)
    df.to_csv(filepath, index=False, encoding="utf-8")
    print(f"CSV guardado en {filepath}")

if __name__ == "__main__":
    print("Iniciando scraping de IMDb Top 50 películas...")
    movies = parse_top_movies()
    if movies:
        save_to_csv(movies, os.path.join(OUTPUT_DIR, "top_movies.csv"))
    else:
        print("No se encontraron películas. Verifica el archivo 'output/imdb_debug.html'.")
