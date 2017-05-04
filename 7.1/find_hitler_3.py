from bs4 import BeautifulSoup
import urllib.request
import ssl
import time


def find_way(root, start_article, destination_article):

    def validate_tag(tag):
        name = tag.name
        if name == "ul" or name == "p":
            return True
        return False

    def is_link_correct(link, paragraph):
        if not link or link.find('/wiki/') != 0:
            return False
        pref = paragraph[:paragraph.find(link)]
        return True if pref.count('(') == pref.count(')') else False

    def find_correct_link(paragraph):
        for a in paragraph.find_all('a'):
            ref = a.get('href')
            if is_link_correct(str(ref), str(paragraph)):
                return ref

    visited_articles = set()
    current_article = root + start_article

    while current_article != destination_article:
        if current_article in visited_articles:
            print("Programm has fallen into endless cyrcle")
            return

        page = urllib.request.urlopen(current_article)
        soup = BeautifulSoup(page, "lxml")

        print("Current link: " + current_article)
        print("Article: " + soup.find('h1', id='firstHeading').get_text())
        raw_data = soup.find('div', id='mw-content-text')

        for paragraph in raw_data.find_all(validate_tag, recursive=False):
            link = find_correct_link(paragraph)
            if link:
                break

        current_article = root + link
        time.sleep(0.5)

    print("We have found Philosophy!")

wiki_addr = "https://en.wikipedia.org"
find_way(wiki_addr, '/wiki/Boris_Grebenshchikov', '/wiki/Philosophy')
