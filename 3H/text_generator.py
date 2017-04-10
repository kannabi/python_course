import re


def get_words_set(input_file):
    with open(input_file) as fin:
        data = fin.read()
    pattern = r'[a-zA-Zа-яА-Я]+|[^a-zA-Z\d\n]{1}|[0-9]+'
    data = re.findall(pattern, data)
    number_words = len(data)
    _corpus = {}
    for word in set(data):
        _corpus.update({word: data.count(word) / number_words})
    return _corpus

corpus = get_words_set("input.txt")
for w in corpus:
    print(w, corpus.get(w))
