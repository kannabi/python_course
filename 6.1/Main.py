import random
from sys import argv

random.seed()

with open("input.txt", 'r') as content_file:
    content = content_file.read().split(" ")

length = len(content)

for i in range(length):
    content[i] = content[i].strip('\n')

fout = open("output.txt", "w")

try:
    for it in content:
        it = list(it)
        length = len(it)
        body = list(it)[1:length - 1]

        if argv[1] == "-r":
            random.shuffle(body)
        else:
            body.sort()

        fout.write(it[0] + ''.join(body) + it[length - 1] + " ")
except IndexError:
    print("Run with argument: -a -- alphabet order; -r -- random order")
