__START__ = 'START'
__END__ = 'END'
PUNCTUATIONS = {',', ':', ';', '!', '?', '.'}


def get_words_set(input_file):

    def proc_punctuation(word):
        char = word[len(raw_word[w]) - 1]
        if char in PUNCTUATIONS:
            if char == '.':
                raw_word.insert(w + 1, __START__)
                raw_word.insert(w + 1, __END__)
            raw_word.remove(word)
            raw_word.insert(w + 1, char)
            raw_word.insert(w + 1, word[:-1])

    with open(input_file) as fin:
        data = fin.read().lower()

    data = data.split(' ')
    data.insert(0, __START__)
    length = len(data)
    for i in range(length):
        raw_word = data.pop(0).split('\n')
        ln = len(raw_word)
        for w in range(ln):
            proc_punctuation(raw_word[w])
        data.extend(raw_word)
    data = [i for i in data[:-1] if i]
    word_number = len(data)
    _corpus = dict()
    for word in data:
        _corpus.update({word: data.count(word) / word_number})

    return _corpus

corpus = get_words_set("input.txt")

for word in corpus:
    print(word, corpus.get(word))
