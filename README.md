# 🎬 IMDb Scraper - Prueba Técnica (Perfil Senior)

Este repositorio corresponde al desarrollo de la **Prueba Técnica: Scraping Avanzado + SQL + Red + Evaluación Comparativa**, cuyo objetivo principal era implementar un scraper robusto y profesional sobre la plataforma IMDb, incluyendo persistencia de datos, análisis SQL avanzado y estrategias de evasión de bloqueo por red.

---

## 📌 Objetivo General

- Desarrollar un **scraper eficiente y mantenible** para extraer al menos 50 películas desde:  
  👉 [https://www.imdb.com/chart/top/](https://www.imdb.com/chart/top/)

- Capturar los siguientes campos por película:
  - Título
  - Año de estreno
  - Calificación
  - Duración (desde página de detalle)
  - Metascore (si está disponible)
  - Al menos 3 actores principales

- Cumplir con prácticas profesionales de scraping:
  - Headers y cookies personalizados
  - Manejo de errores y backoff
  - Estructura modular
  - Exportación a CSV y/o base de datos
  - Evaluación de arquitectura de scraping vs otras herramientas

---

## ⚙️ ¿Qué se intentó implementar?

Durante este proceso se desarrollaron varios enfoques progresivos:

### 1. Scraper con `requests` + `BeautifulSoup`

- Se implementó el archivo `top_movies.py` ubicado en `spiders/` para extraer las películas más populares desde `/chart/top`.
- Se aplicaron headers personalizados, cookies simuladas y un `User-Agent` realista.
- Se intentó parsear los campos requeridos y acceder al detalle de cada película.
- Se generó un archivo `output/top_movies.csv` (actualmente vacío por fallas de extracción).
- Se descargó localmente el HTML (`data/top_movies.html`) para intentar debug offline.

### 2. Script auxiliar de verificación

- Se construyó `scripts/fetch_top_movies_html.py` para guardar manualmente la página HTML y analizar la estructura.

### 3. Pruebas estructuradas con Scrapy

- Se definió un `Item` (`items.py`) para estandarizar los datos de película.
- Se preparó una estructura `scrapy` clásica con `middlewares.py`, `pipelines.py`, `settings.py`.
- El spider `top_movies.py` aún se ejecuta como script tradicional, pero está alineado con la estructura Scrapy para una transición futura.

---

## ⚠️ Estado actual del scraper

- Se logró simular múltiples headers, construir la estructura base del spider y obtener el HTML completo.
- **Sin embargo, IMDb implementa mecanismos de bloqueo que devuelven HTML vacío o incompleto**, lo cual impidió parsear los datos correctamente incluso desde el archivo guardado offline.
- El archivo `.csv` generado se encuentra vacío como evidencia del fallo de parsing.

---

## 📝 Consideraciones finales

Este repositorio representa el avance real alcanzado en el tiempo disponible, documentando el enfoque, los scripts desarrollados, y las barreras encontradas.
