fin = open("input.txt")

n = fin.readline()
text = []
for it in fin:
    text.append(it)

# print(text)

i = 1
j = 0

res = ''

for it in text:
    if it.find('\n') != -1:
        it = it[0: len(it) - 1]
    while i < len(it):
        while j + i - 1 < len(it):
            res += it[j: j + i] + ' '
            j += 1
        i += 1
        j = 0
    res += it + ' '
    print(res)
    res = ''
    i = 1
