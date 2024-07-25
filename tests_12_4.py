import logging
import unittest
import code_12_4


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            object = code_12_4.Runner('walker', speed=-5)
            if object.speed >= 0:
                logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)
        for i in range(0, 10):
            object.walk()
        self.assertEqual(object.distance, 50, msg=f'должно получиться 50, а не {object.distance}')

    def test_run(self):
        try:
            object = code_12_4.Runner(777)
            if isinstance(object.name, str):
                logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)
        for i in range(0, 10):
            object.run()
        self.assertEqual(object.distance, 100, msg=f'должно получиться 100, а не {object.distance}')

    def test_challenge(self):
        object1 = code_12_4.Runner('walker')
        object2 = code_12_4.Runner('runner')
        for i in range(0, 10):
            object1.walk()
            object2.run()
        self.assertNotEqual(object1.distance, object2.distance, msg=f'результаты теста {object1.distance} и '
                                                                    f'{object2.distance} не должны совпадать')


logging.basicConfig(level=logging.INFO, filemode='r', filename='runner_tests.log', encoding="UTF-8",
                    format='%(asctime)s | %(levelname)s | %(message)s')
