"""Домашнее задание по теме "Систематизация и пропуск тестов".
Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при помощи встроенных
 в unittest декораторов.

Задача "Заморозка кейсов":
Подготовка:
В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest."""

import test_12_3
import unittest

"""Часть 1. TestSuit.
Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
Создайте объект класса TextTestRunner, с аргументом verbosity=2."""

codeTS = unittest.TestSuite()
codeTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
codeTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
result = unittest.TextTestRunner(verbosity=2)

"""Часть 2. Пропуск тестов.
Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False
будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase."""


result.run(codeTS)