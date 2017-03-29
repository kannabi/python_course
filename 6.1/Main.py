import random

random.seed()

with open("input.txt", 'r') as content_file:
    content = content_file.read().split(" ")

fout = open("output.txt", "w")

for i in range(len(content)):
    content.extend(content.pop(i).split('\n'))

for it in content:
    it = list(it)
    length = len(it)

    for i in range(length - 1):
        it.insert(length - 2, it.pop(random.randint(1, length - 2)))
    fout.write("".join(it) + " ")
