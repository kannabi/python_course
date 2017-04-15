#!/usr/bin/env python3
import re
import argparse
import random


class Dictogram:
    def __init__(self):
        self._keys = []
        self._key_gist = []
        self._word_gist = []

    def put(self, key, token):
        if not isinstance(key, str) or not isinstance(token, str):
            raise ValueError

        if '\n' in key:
            return

        self.add_key(key)

        if '\n' in token:
            return

        if token in self._word_gist[self._index(key)]:
            self._word_gist[self._index(key)][token] += 1
        else:
            self._word_gist[self._index(key)].update({token: 1})

    def add_key(self, key):
        if key not in self._keys:
            for k in self._keys:
                if k > key:
                    self._keys.insert(self._index(k), key)
                    break

            if key not in self._keys:
                self._keys.append(key)

            self._word_gist.insert(self._index(key), {})
            self._key_gist.insert(self._index(key), 1)
        else:
            self._key_gist[self._index(key)] += 1

    def get_probability(self, key, token):
        if token in self._word_gist[self._index(key)]:
            s = sum(self._word_gist[self._index(key)].values())
            return self._word_gist[self._index(key)].get(token) / s
        else:
            return 0.0

    def __getitem__(self, item):
        p = self._index(item)
        num = sum(self._word_gist[p].values())
        return {token: self._word_gist[p].get(token) / num for token in self._word_gist[p].keys()}

    def __str__(self):
        answer = '\n'
        single_words = [word for word in self._keys if ' ' not in word]
        single_words_gist = [self._key_gist[self._index(w)] for w in single_words]

        for i in range(len(single_words)):
            key_prob = single_words_gist[i] / sum(single_words_gist)
            answer += "  " + single_words[i] + ": " + '{:.2f}'.format(key_prob) + "\n"

        for word in self._keys:
            if not self._word_gist[self._index(word)]:
                continue
            gist = str()
            num_tokens = sum(self._word_gist[self._index(word)].values())
            for column in sorted(self._word_gist[self._index(word)].keys()):
                token_prob = self._word_gist[self._index(word)].get(column) / num_tokens
                gist += "  " + column + ": " + '{:.2f}'.format(token_prob) + "\n"
            answer += word + "\n" + gist
        answer = answer.rstrip('\n')
        return answer

    def get_random_word(self, depth):
        random.seed()
        suitable_words = [w for w in self._keys if len(w.split(' ')) == depth]
        return suitable_words[random.randint(0, len(suitable_words))]

    def get_next_word(self, key):
        splitted_key = key.split(' ')
        dep = len(splitted_key)
        for i in range(dep, 1, -1):
            key_index = self._index(' '.join(splitted_key[:-dep + 1]))
            if self._word_gist[key_index]:
                return max(self._word_gist[key_index], key=self._word_gist[key_index].get)
        random.seed()
        return self.get_random_word(random.randint(1, dep))

    def _index(self, key):
        return self._keys.index(key)


PATTERN = r'[a-zA-Zа-яА-Я\']+|[^a-zA-Z\d\n]{1}|[0-9]+|[\n]{1}'


def init_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name")

    prob_parser = subparsers.add_parser("probabilities")
    prob_parser.add_argument("--depth", action="store", nargs=1, type=int, required=True)

    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("--depth", action="store", nargs=1, type=int, required=True)
    generate_parser.add_argument("--size", action="store", nargs=1, type=int, required=True)

    test_parser = subparsers.add_parser("test")
    tokenize_parser = subparsers.add_parser("tokenize")

    return parser


def get_tokens(input_file):
    with open(input_file) as fin:
        fin.readline()
        return re.findall(PATTERN, fin.read())


def get_probabilities(input_file, depth):
    word_data = tuple(
        filter(lambda x: x.isalpha() or x.isdigit() or '\n' in x, get_tokens(input_file)))
    probabilities = Dictogram()
    try:
        for i in range(len(word_data)):
            cur_word = str()
            for k in range(i, i + depth):
                cur_word += ' ' + word_data[k]
                cur_word = cur_word.lstrip(' ')
                prob_word = word_data[k + 1]
                probabilities.put(cur_word, prob_word)
    except IndexError:
        # probabilities.add_key(cur_word)
        return probabilities


def generate_text(input_file, depth, size):
    dictogram = get_probabilities(input_file, depth)
    cur_word = dictogram.get_random_word(depth)
    text = str()
    for i in range(depth, size):
        text += cur_word
        text += ' '
        cur_word = dictogram.get_next_word(cur_word)
    text = text.lower()
    text = text[:1].upper() + text[1:]
    print(text)


with open("input_bg.txt") as f:
    args = init_parser().parse_args(f.readline().split())

if args.subparser_name == "probabilities":
    probs = get_probabilities("input.txt", args.depth[0])
    print(probs)
    exit()

if args.subparser_name == "tokenize":
    corpus = tuple(filter(lambda x: x != '\n', get_tokens("input.txt")))
    for word in corpus:
        print(word)
    exit()

if args.subparser_name == "generate":
    generate_text("input_bg.txt", args.depth[0], args.size[0])
    exit()

if args.subparser_name == "test":
    print("All the okey. Maybe. Or not. Are you okey?")
    exit()
