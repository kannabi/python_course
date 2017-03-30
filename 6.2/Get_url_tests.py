import unittest
import random
from string import ascii_letters
from Get_url import get_url


class Grt_url_tests(unittest.TestCase):
    def setUp(self):
        self.url_set = ("https://pythonworld.ru/moduli/modul-random.html",
                        "www.google.ru/search?q=read+from+file+python+3&oq=read+from+file+p&aqs=chrome.2.69i57j0l5.8071j0j7&sourceid=chrome&ie=UTF-8#newwindow=1&safe=off&q=python+3+string+equal&*",
                        "https://vk.com/falko_s?z=photo-119287258_456239064%2Fwall23850766_7649")

        self.separators = " \n"
        self.input_file_name = "test_input.txt"
        self.output_file_name = "test_input.txt"
        f = open(self.input_file_name, "w")
        f.close()
        f = open(self.output_file_name, "w")
        f.close()
        random.seed()

    def test_simple_file(self):
        fin = open(self.input_file_name, "w")

        symbols_set = ascii_letters + "\n"
        i = 0
        n = random.randint(3, 12)
        for j in range(n):
            if i < len(self.url_set) and random.randint(0, 1) == 1:
                fin.write(self.url_set[i] + random.choice(self.separators))
                i += 1
            fin.write(''.join([random.choice(symbols_set) for _ in range(random.randint(1, 20))])
                      + random.choice(self.separators))

        length = len(self.url_set)
        if i < length - 2:
            for k in range(i, length - 1):
                fin.write(self.url_set[k] + random.choice(self.separators))

        fin.close()

        get_url(self.input_file_name, self.output_file_name)

        f = open(self.output_file_name, "r")

        check = True
        for line in f:
            check = line.strip("\n") in self.url_set

        f.close()
        self.assertEqual(check, True)

    def test_empty_file(self):
        f = open(self.output_file_name, "w")
        f.close()

        get_url(self.input_file_name, self.output_file_name)

        f = open(self.output_file_name, "r")
        res = []
        for line in f:
            res.extend(line)
        f.close()
        self.assertEqual(len(res), 0)

    def test_file_without_urls(self):
        fin = open(self.input_file_name, "w")

        symbols_set = ascii_letters + "\n"
        n = random.randint(3, 12)
        for j in range(n):
            fin.write(''.join([random.choice(symbols_set) for _ in range(random.randint(1, 20))])
                      + random.choice(self.separators))

        fin.close()

        get_url(self.input_file_name, self.output_file_name)

        f = open(self.output_file_name, "r")

        res = []
        for i in f:
            res.extend(i)

        f.close()

        self.assertEqual(len(res), 0)

if __name__ == "__main__":
        unittest.main()
