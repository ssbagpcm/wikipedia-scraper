import requests
from bs4 import BeautifulSoup
import random
import time

def obtenir_article_wikipedia_aleatoire():
    response = requests.get("https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard")
    soup = BeautifulSoup(response.content, 'html.parser')
    titre = soup.find(id="firstHeading")
    paragraphs = soup.find(id="bodyContent").find_all("p")
    contenu = "\n".join([paragraphe.text for paragraphe in paragraphs])
    return titre, response.url, contenu

def extraire_articles_wikipedia(max_articles):
    liens_visites = set()

    for _ in range(max_articles):
        titre, url_actuelle, contenu = obtenir_article_wikipedia_aleatoire()
        print(titre.text)

        if url_actuelle in liens_visites:
            continue

        liens_visites.add(url_actuelle)

        with open("articles_extraits.txt", "a", encoding="utf-8") as fichier:
            fichier.write(f"Titre : {titre.text}\nURL : {url_actuelle}\n\nContenu :\n{contenu}\n\n")

        time.sleep(0.1)

nombre_articles_a_extraire = 2593505

extraire_articles_wikipedia(nombre_articles_a_extraire)
