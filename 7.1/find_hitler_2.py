import ssl
import urllib.request
from bs4 import BeautifulSoup


import lxml.html as html


def find_brackets_end(tags):
    for i in tags:
        if ')' in i:
            return tags.index(i)

wiki_addr = "https://en.wikipedia.org"

ssl._create_default_https_context = ssl._create_unverified_context

cl = html.parse(urllib.request.urlopen(wiki_addr + "/wiki/Boris_Grebenshchikov"))

# tags = cl.xpath('//*[@id="mw-content-text"]/p[1]/text()')
# print(''.join(tags))

raw_data = cl.xpath('//*[@id="mw-content-text"]/p[1]')
print(raw_data[0].text)

for el in raw_data: #[find_brackets_end(cl.xpath('//*[@id="mw-content-text"]/p[1]/text()')) - 1:]:
    print(el)
