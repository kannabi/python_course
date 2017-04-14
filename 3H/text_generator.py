import re
import argparse
from Dictogram import Dictogram

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
    word_data = tuple(filter(lambda x: x != ' ', get_tokens(input_file)))
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


with open("input.txt") as f:
    args = init_parser().parse_args(f.readline().split())

if args.subparser_name == "probabilities":
    probs = get_probabilities("input.txt", args.depth[0])
    print(probs)
    exit()

if args.subparser_name == "tokenize":
    corpus = tuple(filter(lambda x: x != '\n', get_tokens("input.txt")))
    for word in corpus:
        print(word)

if args.subparser_name == "generate":
    print("How to make fcking generating?!")

if args.subparser_name == "test":
    print("All the okey. Maybe. Or not. Are you okey?")
