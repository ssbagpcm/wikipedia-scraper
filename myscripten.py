import requests
from bs4 import BeautifulSoup
import random
import time

def get_random_wikipedia_article():
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    paragraphs = soup.find(id="bodyContent").find_all("p")
    content = "\n".join([paragraph.text for paragraph in paragraphs])
    return title, response.url, content

def scrape_wikipedia_articles(max_articles):
    visited_links = set()

    for _ in range(max_articles):
        title, current_url, content = get_random_wikipedia_article()
        print(title.text)

        if current_url in visited_links:
            continue

        visited_links.add(current_url)

        with open("extracted_articles.txt", "a", encoding="utf-8") as file:
            file.write(f"Title: {title.text}\nURL: {current_url}\n\nContent:\n{content}\n\n")

        time.sleep(0.1)

num_articles_to_scrape = 6787981

scrape_wikipedia_articles(num_articles_to_scrape)
