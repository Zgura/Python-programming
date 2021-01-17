"""Напишите unit-тест для класса из задания 2, сформируйте coverage
report в формате html и оцените степень покрытия исходного кода
тестами"""


import unittest
# import sys  # для указания пути для подгрузки модуля, но лучше, чтобы PyCharm сам всё нашёл
# sys.path.append(r"D:\Job\ucheba\Unittest_pract")
from zgura_16_2_ITERATOR import Iterator


class TestIterator(unittest.TestCase):
    def test_iter(self):
        self.assertEqual(Iterator.test_now(5), [2, 3, 5, 7, 11])


if __name__ == "__main__":
    unittest.main()
