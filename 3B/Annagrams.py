def ann_filter(x, item):
    if tuple(filter(lambda l: l in x, item)) == tuple(item):
        return True
    return False


with open("input.txt") as fin:
    n = fin.readline()
    data = fin.read().lower().split('\n')

    res = []
    for it in data:
        annagrams = tuple(filter(lambda x: ann_filter(x, it), data))
        for w in annagrams[1:]:
            data.remove(w)
        res.append(annagrams)

for l in res[:-1]:
    print(' '.join(l))
