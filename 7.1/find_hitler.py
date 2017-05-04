import urllib.request
import ssl
import re
from lxml.html import parse

pattern = re.compile(r"""<a\shref=\"/wiki/[\w]+_?[\w]+\"\stitle=\"[\w\s]+\">""", re.IGNORECASE)
link_pattern = re.compile("""/wiki/[\w]+_[\w]+""", re.IGNORECASE)


def get_way(domen, start_address, target_address):
    ssl._create_default_https_context = ssl._create_unverified_context

    move_history = list()
    finded = list()
    cur_move = domen + start_address
    destiny = domen + target_address
    while cur_move != destiny:
        k = 0
        while cur_move in move_history:
            k += 1
            try:
                cur_move = domen + finded[k]
            except IndexError:
                print("We are in the endless recursion!")
        print(cur_move)
        with urllib.request.urlopen(cur_move) as fin:
            finded = tuple(map(lambda x: link_pattern.search(x).group(0), link_pattern.findall(str(fin.read()))))
            print(finded)
        move_history.append(cur_move)
        cur_move = domen + finded[0]
        time.sleep(0.5)


wiki_addr = "https://en.wikipedia.org"
get_way(wiki_addr, "/wiki/Boris_Grebenshchikov", "/wiki/Philosophy")
