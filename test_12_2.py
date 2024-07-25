import unittest
import code_12_2


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = code_12_2.Runner(name='Usain', speed=10)
        self.runner2 = code_12_2.Runner(name='Andrey', speed=9)
        self.runner3 = code_12_2.Runner(name='Nick', speed=3)

    def test1(self):
        race1 = code_12_2.Tournament(90, self.runner1, self.runner3)
        results = race1.start()
        self.assertTrue(bool(results.get(len(results)) == self.runner3))
        self.all_results[1] = results

    def test2(self):
        race2 = code_12_2.Tournament(90, self.runner2, self.runner3)
        results = race2.start()
        self.assertTrue(bool(results.get(len(results)) == self.runner3))
        self.all_results[2] = results

    def test3(self):
        race3 = code_12_2.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = race3.start()
        self.assertTrue(bool(results.get(len(results)) == self.runner3))
        self.all_results[3] = results

    @classmethod
    def tearDownClass(cls):
        out = {}
        for key, value in cls.all_results.items():
            for key_, value_ in value.items():
                out[key_] = str(value_)
            print(out)
