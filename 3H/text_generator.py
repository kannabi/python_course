import re
from Dictogram import Dictogram

PATTERN = r'[a-zA-Zа-яА-Я\']+|[^a-zA-Z\d\n]{1}|[0-9]+|[\n]{1}'


def get_raw_data(input_file):
    with open(input_file) as fin:
        return re.findall(PATTERN, fin.read())


def get_words_set(input_file):
    data = get_raw_data(input_file)
    data = tuple(filter(lambda x: x != ' ', data))
    number_words = len(data)
    _corpus = {}
    for word in set(data):
        _corpus.update({word: data.count(word) / number_words})
    return _corpus


def get_probabilities(input_file, depth):
    word_data = tuple(filter(lambda x: x != ' ', get_raw_data(input_file)))
    probabilities = Dictogram()
    try:
        for i in range(len(word_data)):
            cur_word = word_data[i]
            for k in range(1, depth + 1):
                prob_word = word_data[i + k]
                probabilities.put(cur_word, prob_word)
    except IndexError:
        probabilities.add_key(prob_word)
        return probabilities

res = get_probabilities("input.txt", 1)

print(res)
