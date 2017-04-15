#!/usr/bin/env python3
import re
import argparse
import random
import unittest

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
        if cur_word != '\n':
            probabilities.add_key(cur_word)
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
    text = text[:1].upper() + text[1:-1] + '.'
    print(text)

if __name__ == "__main__":
    inp = "input.txt"
    with open(inp) as f:
        args = init_parser().parse_args(f.readline().split())

    if args.subparser_name == "probabilities":
        probs = get_probabilities(inp, args.depth[0])
        print(str(probs))
        print(probs)

    if args.subparser_name == "tokenize":
        corpus = tuple(filter(lambda x: x != '\n', get_tokens(inp)))
        for word in corpus:
            print(word)

    if args.subparser_name == "generate":
        generate_text(inp, args.depth[0], args.size[0])

    if args.subparser_name == "test":
        print("All the okey. Maybe. Or not. Are you okey?")


class GeneratorTest(unittest.TestCase):
    def setUp(self):
        self._test_text_1 = "Счастье всем, и пусть никто не уйдет обиженным."
        self._test_text_1_tokenized = ['Счастье', ' ', 'всем', ' ', ',', ' ', 'и', ' ',
                                       'пусть', ' ', 'никто', ' ', 'не', ' ', 'уйдет',
                                       ' ', 'обиженным', '.']
        self._test_text_2 = "We have no need of other world. We need mirrors."
        self._test_text_2_tokenized = ['We', ' ', 'have', ' ', 'no', ' ', 'need', ' ',
                                       'of', ' ', 'other', ' ', 'world', '.', ' ',
                                       'We', ' ', 'need', ' ', 'mirrors', '.']
        self._test_text_3 = "Life is a suffer."
        self._test_text_3_tokenized = ['Life', ' ', 'is', ' ', 'a', ' ', 'suffer', '.']
        self._test_text_3_prob = ("\nLife: 0.25\na: 0.25\nis: 0.25\nsuffer: 0.25\nLife\n" +
                                  "  is: 1.00\na\n  suffer: 1.00\nis\n  a:1.00")
        self._tokenize_args = "tokenize\n"
        self._probabilities_args = "probabilities --depth 1\n"
        self._test_file = "test_input.txt"

    def test_first_text_tokenize(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_1)
        test_corpus = get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_1_tokenized]
        diff_correct = [i for i in self._test_text_1_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_second_text_tokenize(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_2)
        test_corpus = get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_2_tokenized]
        diff_correct = [i for i in self._test_text_2_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_third_text_tokenize(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_3)
        test_corpus = get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_3_tokenized]
        diff_correct = [i for i in self._test_text_3_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_third_text_probabilities(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._probabilities_args)
            fout.write(self._test_text_3)
        dictogram = str(get_probabilities(self._test_file, 1))
        diff_dictogram = [i for i in dictogram if i not in self._test_text_3_prob]
        diff_correct = [i for i in self._test_text_3_prob if i not in dictogram]
        self.assertEqual(len(diff_correct) + len(diff_dictogram), 0)
