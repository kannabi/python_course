import unittest
import random
from string import ascii_letters

class Grt_url_tests(unittest.TestCase):

    def setUp(self):
        self.url_set = ["ttps://pythonworld.ru/moduli/modul-random.html",
                        "www.google.ru/search?q=read+from+file+python+3&oq=read+from+file+p&aqs=chrome.2.69i57j0l5.8071j0j7&sourceid=chrome&ie=UTF-8#newwindow=1&safe=off&q=python+3+string+equal&*",
                        "https://vk.com/falko_s?z=photo-119287258_456239064%2Fwall23850766_7649"]

        self.input_file_name = "test_input.txt"
        self.output_file_name = "test_input.txt"
        f = open(self.input_file_name, "w")
        f.close()
        f = open(self.output_file_name, "w")
        f.close()
        random.seed()

    def test_simple_file(self):
        fin = open(self.input_file_name, "w")

        i = 0
        n = random.randint(3, 12)

        for j in range(n):
            if i < len(self.url_set) and random.randint(0, 1) == 1:
                fin.write(self.url_set[i] + ' ')
                i += 1
            fin.write(''.join([random.choice(ascii_letters) for _ in range(random.randint(1, 20))]))
        fin.close()

