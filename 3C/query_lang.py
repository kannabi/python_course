def uniquer(seq, f=None):
    """ Keeps earliest occurring item of each f-defined equivalence class """
    if f is None:
        def f(x): return x
    already_seen = set()
    result = []
    for item in seq:
        marker = f(item)
        if marker not in already_seen:
            already_seen.add(marker)
            result.append(item)
    return result


with open("input.txt") as fin:
    dictionaries = dict()
    new_lang = fin.readline().split(' ')
    while new_lang[0] != '\n':
        dictionaries.update({new_lang[0]: new_lang[1]})
        new_lang = fin.readline().split(' ')

    for query in fin:
        query = query.lower().strip('\n')
        langs = list()
        for word in query.split(' '):
            counter = sorted([[i, 0] for i in dictionaries.keys()])
            for letter in word:
                for lang in counter:
                    if letter in dictionaries.get(lang[0]):
                        lang[1] += 1
            counter.sort(key=lambda x: x[1], reverse=True)
            counter = list(filter(lambda x: x[1] == counter[0][1], counter))
            counter.sort(key=lambda x: x[0])
            if counter[0][1] == 0:
                counter.insert(0, ['', '\n'])
            langs.append(counter[0][0])
            langs = list(filter(lambda x: x != '', langs))
        print(' '.join(uniquer(sorted(langs))))
