"""Напишите свой класс итератор, который при итерации генерирует
простые числа (сколько задали при создании экземпляра
класса)"""

import math
import time


class Iterator:
    def __init__(self, num):
        self._num = num
        self._count = 0  # счётчик простых чисел
        self.n = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == self._num:
            raise StopIteration
        else:
            while True:
                for a in range(2, int(math.sqrt(self.n) + 1)):
                    if self.n % a == 0:
                        self.n += 1
                        break
                else:
                    a = self.n
                    self.n += 1
                    self._count += 1
                    return a

    @staticmethod
    def test_now(number):  # сделал этот метод специально для того, чтобы было удобно потом тестировать
        x_1 = Iterator(number)
        a = list(x_1)
        return a


start_time = time.time()
# x_1 = Iterator(7)
# print(next(x_1))
# print(next(x_1))
# print(next(x_1))
# print(next(x_1))
# print(next(x_1))
# print(next(x_1))
# print(next(x_1))

print(Iterator.test_now(10000))  # статический метод можно вызыввать без создания экземпляра
print(time.time() - start_time)
