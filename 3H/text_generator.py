def get_words_set(input_file):
    with open(input_file) as fin:
        data = fin.read().lower()

    data = data.split(' ')
    length = len(data)
    for i in range(length):
        raw_word = data.pop(0).split('\n')
        data.extend(list(map(lambda x: ''.join([l for l in x if l.isalpha()]), raw_word)))

    word_number = len(data)
    _corpus = dict()
    for word in data:
        _corpus.update({word: data.count(word) / word_number})

    return _corpus

corpus = get_words_set("input.txt")

for word in corpus:
    print(word, corpus.get(word))
