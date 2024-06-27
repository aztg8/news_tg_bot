import requests
from bs4 import BeautifulSoup
import sqlite3

response = requests.get("https://showbiz.uz/scandals/")

html = response.text

soup = BeautifulSoup(html, "html.parser")

news_section = soup.find("div", id="dle-content")

news = news_section.find_all("div", class_="short-story")

database = sqlite3.connect("news.db")
cursor = database.cursor()
category_id = 2

for n in news:
    title = n.find("h2", class_="sh-tit").get_text()
    published_at = n.find("span", class_="tdat").get_text()
    link = n.find("a").get("href")
    image = "https://showbiz.uz" + n.find("img").get("data-src")

    cursor.execute("""
    INSERT INTO news(news_title, date, link, image, category_id)
    VALUES (?,?,?,?,?); 
    """, (title, published_at, link, image, category_id))

database.commit()

database.close()
