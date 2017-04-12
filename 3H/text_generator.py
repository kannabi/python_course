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


# TODO: Refactor this fucking try block!
def get_probabilities(input_file, depth):
    # word_data = tuple(filter(lambda x: x != ' ', get_raw_data(input_file)))
    word_data = tuple(filter(lambda x: x.isalpha() or x.isdigit(), get_raw_data(input_file)))
    probabilities = Dictogram()
    try:
        for i in range(len(word_data)):
            cur_word = word_data[i]
            prob_word = str()
            for k in range(1, depth + 1):
                prob_word += word_data[i + k] + ' '
            prob_word = prob_word.rstrip(' ')
            probabilities.put(cur_word, prob_word)
    except IndexError:
        while i < len(word_data):
            probabilities.add_key(word_data[i])
            i += 1
        return probabilities

res = get_probabilities("input_dovlatov.txt", 1)

print(res)

cur_world = res.get_random_world()

line = str()
for i in range(7):
    cur_world = res.get_next_word(cur_world)
    line += cur_world + ' '
print(line.rstrip())

