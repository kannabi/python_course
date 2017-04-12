class Dictogram:
    def __init__(self):
        self._keys = []
        self._key_gist = []
        self._word_gist = []

    def put(self, key, token):
        if not isinstance(key, str) or not isinstance(token, str):
            raise ValueError

        self.add_key(key)

        if token[0].isupper():
            return

        if token in self._word_gist[self._index(key)]:
            self._word_gist[self._index(key)][token] += 1
        else:
            self._word_gist[self._index(key)].update({token: 1})

    def add_key(self, key):
        if key not in self._keys:
            for k in self._keys:
                if k > key:
                    self._keys.insert(self._index(k), key)
                    break

            if key not in self._keys:
                self._keys.append(key)

            self._word_gist.insert(self._index(key), {})
            self._key_gist.insert(self._index(key), 1)
        else:
            self._key_gist[self._index(key)] += 1

    def get_probability(self, key, token):
        if token in self._word_gist[self._index(key)]:
            return self._word_gist[self._index(key)].get(token) / sum(self._word_gist[self._index(key)].values())
        else:
            return 0.0

    def __getitem__(self, item):
        pos = self._index(item)
        num = sum(self._word_gist[pos].values())
        return {token: self._word_gist[pos].get(token) / num for token in self._word_gist[pos].keys()}

    def __str__(self):
        answer = str()
        for i in range(len(self._key_gist)):
            answer += "  " + self._keys[i] + ": " + str(self._key_gist[i] / sum(self._key_gist)) + "\n"

        for word in self._keys:
            if not self._word_gist[self._index(word)]:
                continue
            gist = str()
            num_tokens = sum(self._word_gist[self._index(word)].values())
            for column in self._word_gist[self._index(word)].keys():
                gist += "  " + column + ": " + str(self._word_gist[self._index(word)].get(column) / num_tokens) + "\n"
            answer += word + ":\n" + gist
        return answer

    def _index(self, key):
        return self._keys.index(key)