def ann_filter(x, item):
    print(item)
    if tuple(filter(lambda l: l in x, item)) == tuple(item):
        return True
    return False

with open("input.txt") as fin:
    n = fin.readline()
    data = fin.read().lower().split('\n')
    annagrams = []
    for k in range(len(data)):
        annagrams.append(data[k])
        s = k
        for s in range(len(data)):
            if ann_filter(data[k], data[s]):
                annagrams.append(data[s])
                data.remove(data[s])
        print(annagrams)
        if len(annagrams) > 1:
            print(' '.join(annagrams))
        annagrams.clear()
