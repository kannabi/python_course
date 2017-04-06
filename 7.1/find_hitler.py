import urllib.request
import ssl


def get_articles(domen, address):
    def proc_tag(item):
        try:
            if item[0] == 'a':
                item = item.split(" ")
                if item[1][0:11] == "href=\"/wiki" and item[2][0:6] == "title=":
                    return domen + item[1][11: -1]
        except IndexError:
            return

    ssl._create_default_https_context = ssl._create_unverified_context
    with urllib.request.urlopen(domen + address) as fin:
        data = str(fin.read()).split("<")
        # data = tuple(map(lambda x: x.split('>'), data))
        length = len(data)
        for i in range(length):
            data.extend(data.pop(0).split('>'))

        articles = tuple(filter(lambda x: x is not None, tuple(map(proc_tag, data))))

        return articles


wiki_addr = "https://en.wikipedia.org"
arts = get_articles(wiki_addr, "/wiki/Boris_Grebenshchikov")

for it in arts:
    print(it)
