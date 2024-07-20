import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Тестируем метод walk
        :return:
        """
        object = Runner('walker')
        for i in range(0, 10):
            object.walk()
        self.assertEqual(object.distance,50, msg=f'должно получиться 50, а не {object.distance}')
        
    def test_run(self):
        """
        Тестируем метод run
        :return:
        """
        object = Runner('runner')
        for i in range(0, 10):
            object.run()
        self.assertEqual(object.distance,100, msg=f'должно получиться 100, а не {object.distance}')
        
    def test_challenge(self):
        """
        Тестируем методы walk и run на неравенство
        :return:
        """
        object1 = Runner('walker')
        object2 = Runner('runner')
        for i in range(0, 10):
            object1.walk()
            object2.run()
        self.assertNotEqual(object1.distance, object2.distance,msg=f'результаты теста {object1.distance} и {object2.distance} не должны совпадать')