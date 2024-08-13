import unittest

import code_12_1
import code_12_2


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        Тестируем метод walk
        :return:
        """
        object = code_12_1.Runner('walker')
        for i in range(0, 10):
            object.walk()
        self.assertEqual(object.distance, 50, msg=f'должно получиться 50, а не {object.distance}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Тестируем метод run
        :return:
        """
        object = code_12_1.Runner('runner')
        for i in range(0, 10):
            object.run()
        self.assertEqual(object.distance, 100, msg=f'должно получиться 100, а не {object.distance}')

    def test_challenge(self):
        """
        Тестируем методы walk и run на неравенство
        :return:
        """
        object1 = code_12_1.Runner('walker')
        object2 = code_12_1.Runner('runner')
        for i in range(0, 10):
            object1.walk()
            object2.run()
        self.assertNotEqual(object1.distance, object2.distance, msg=f'результаты теста {object1.distance} и '
                                                                    f'{object2.distance} не должны совпадать')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = code_12_2.Runner(name='Usain', speed=10)
        self.runner2 = code_12_2.Runner(name='Andrey', speed=9)
        self.runner3 = code_12_2.Runner(name='Nick', speed=3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        race1 = code_12_2.Tournament(90, self.runner1, self.runner3)
        results = race1.start()
        self.assertTrue(bool(results.get(len(results)) == self.runner3))
        self.all_results[1] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        race2 = code_12_2.Tournament(90, self.runner2, self.runner3)
        results = race2.start()
        self.assertTrue(bool(results.get(len(results)) == self.runner3))
        self.all_results[2] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
