import urllib.request
import ssl
import random

import time


def get_articles(domen, start_address, target_address):
    def proc_tag(item):
        try:
            if item[0] == 'a':
                item = item.split(" ")
                if (item[1][0:11] == "href=\"/wiki"
                    and item[2][0:6] == "title="
                    and item[1][0:16] != "href=\"/wiki/File"
                    and item[1][0:22] != "href=\"/wiki/Wikipedia:"):
                    return domen + "/wiki" + item[1][11: -1].replace(' ', '_')
        except IndexError:
            return

    ssl._create_default_https_context = ssl._create_unverified_context

    articles = list()
    articles.append(domen + start_address)
    print(articles)
    destiny = domen + target_address
    random.seed()
    while destiny not in articles:
        cur_move = articles[random.randint(0, int(len(articles) / 2))]
        print(cur_move)
        with urllib.request.urlopen(cur_move) as fin:
            data = str(fin.read()).split("<")
            length = len(data)
            for i in range(length):
                data.extend(data.pop(0).split('>'))
            articles = tuple(filter(lambda x: x is not None, tuple(map(proc_tag, data))))
        time.sleep(1)


wiki_addr = "https://en.wikipedia.org"
get_articles(wiki_addr, "/wiki/Boris_Grebenshchikov", "/wiki/Philosophy")
