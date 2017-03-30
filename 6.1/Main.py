import random

random.seed()

with open("input.txt", 'r') as content_file:
    content = content_file.read().split(" ")

length = len(content)

for i in range(length):
    content[i] = content[i].strip('\n')

fout = open("output.txt", "w")

for it in content:
    it = list(it)
    length = len(it)
    body = list(it)[1:length - 1]

    random.shuffle(body)
    fout.write(it[0] + ''.join(body) + it[length - 1] + " ")
