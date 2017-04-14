import unittest
import text_generator


class GeneratorTest(unittest.TestCase):
    def setUp(self):
        self._test_text_1 = "Счастье всем, и пусть никто не уйдет обиженным."
        self._test_text_1_tokenized = ['Счастье', ' ', 'всем', ' ', ',', ' ', 'и', ' ',
                                       'пусть', ' ', 'никто', ' ', 'не', ' ', 'уйдет',
                                       ' ', 'обиженным', '.']
        self._test_text_2 = "We have no need of other world. We need mirrors."
        self._test_text_2_tokenized = ['We', ' ', 'have', ' ', 'no', ' ', 'need', ' ',
                                       'of', ' ', 'other', ' ', 'world', '.', ' ',
                                       'We', ' ', 'need', ' ', 'mirrors', '.']
        self._test_text_3 = "Life is a suffer."
        self._test_text_3_tokenized = ['Life', ' ', 'is', ' ', 'a', ' ', 'suffer', '.']
        self._tokenize_args = "tokenize\n"
        self._test_file = "test_input.txt"

    def test_first_text(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_1)
        test_corpus = text_generator.get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_1_tokenized]
        diff_correct = [i for i in self._test_text_1_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_second_text(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_2)
        test_corpus = text_generator.get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_2_tokenized]
        diff_correct = [i for i in self._test_text_2_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_third_text(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_3)
        test_corpus = text_generator.get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_3_tokenized]
        diff_correct = [i for i in self._test_text_3_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)


if __name__ == "__main__":
        unittest.main()
