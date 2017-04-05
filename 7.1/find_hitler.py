import urllib.request
from pprint import pprint
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
f = urllib.request.urlopen("https://ru.wikipedia.org/wiki/Web_Ontology_Language")
print(f.read())
