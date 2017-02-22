def delete_all_inserts(element):
    i = 0
    while i < text.count(element):
        text.remove(element)


fin = open("input.txt")

string = ''

for line in fin:
    string += line

string = string.lower()

text = list(string)

table = []

it = 0
while it < len(text):
    if text[it].isalpha():
        table.append([text.count(text[it]), text[it]])
        delete_all_inserts(text[it])
    else:
        it += 1

sorted_list = sorted(table, reverse=True)

res = {}

for it in sorted_list:
    if res.get(it[0]):
        res.get(it[0]).append(it[1])
    else:
        res.update({it[0]: [it[1]]})

sorted_list = sorted(res.items(), key=lambda x: x[0], reverse=True)

for i in sorted_list:
    i[1].sort()
    for j in i[1]:
        print(j + ':', i[0])
