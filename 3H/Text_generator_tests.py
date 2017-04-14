import unittest
import text_generator


class GeneratorTest(unittest.TestCase):
    def setUp(self):
        self._test_text_1 = "Счастье всем, и пусть никто не уйдет обиженным."
        self._test_text_1_tokenized = "Счастье\n \nвсем\n,\n \nи\n \nпусть\n \nникто\n \nне\n \nуйдет\n \nобиженным\n.\n"
        self._test_text_2 = "We have no need of other world. We need mirrors."
        self._test_text_2_tokenized = "We\n \nhave\n \nno\n \nneed\n \nof\n \nother\n \nworld\n.\n \nWe\n \nneed\n \nmirrors\n.\n"
        self._test_text_3 = "Life is a suffer"
        self._test_text_3_tokenized = "Life\n \nis\n \na\n \nsuffer"
        self._test_file = "test_input.txt"

    def test_first_text(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._test_text_1)
        test_corpus = text_generator.get_tokens(self._test_file)
        self.assertEqual(test_corpus, self._test_text_1_tokenized)

    def test_second_text(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._test_text_2)
        test_corpus = text_generator.get_tokens(self._test_file)
        self.assertEqual(test_corpus, self._test_text_2_tokenized)

    def test_third_text(self):
        with open(self._test_file, "w") as fout:
            fout.write(self._test_text_3)
        test_corpus = text_generator.get_tokens(self._test_file)
        self.assertEqual(test_corpus, self._test_text_3_tokenized)

if __name__ == "__main__":
        unittest.main()
