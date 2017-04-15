import unittest
import Whole_gen


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
        self._test_text_3_prob = ("\nLife: 0.25\na: 0.25\nis: 0.25\nsuffer: 0.25\nLife\n" +
                                  "  is: 1.00\na\n  suffer: 1.00\nis\n  a:1.00")
        self._tokenize_args = "tokenize\n"
        self._probabilities_args = "probabilities --depth 1\n"
        self._test_file = "test_input.txt"

    def test_first_text_tokenize(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_1)
        test_corpus = Whole_gen.get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_1_tokenized]
        diff_correct = [i for i in self._test_text_1_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_second_text_tokenize(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_2)
        test_corpus = Whole_gen.get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_2_tokenized]
        diff_correct = [i for i in self._test_text_2_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_third_text_tokenize(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._tokenize_args)
            fout.write(self._test_text_3)
        test_corpus = Whole_gen.get_tokens(self._test_file)
        diff_corpus = [i for i in test_corpus if i not in self._test_text_3_tokenized]
        diff_correct = [i for i in self._test_text_3_tokenized if i not in test_corpus]
        self.assertEqual(len(diff_correct) + len(diff_corpus), 0)

    def test_third_text_probabilities(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._probabilities_args)
            fout.write(self._test_text_3)
        dictogram = str(Whole_gen.get_probabilities(self._test_file, 1))
        diff_dictogram = [i for i in dictogram if i not in self._test_text_3_prob]
        diff_correct = [i for i in self._test_text_3_prob if i not in dictogram]
        self.assertEqual(len(diff_correct) + len(diff_dictogram), 0)


if __name__ == "__main__":
        unittest.main()
