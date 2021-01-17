"""Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного
числа start (по умолчанию 3) до заданного числа end. Далее необходимо:
Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000."""
import math
import time


def find_primes(end, start=3):
    print('Старт вычислений при end = {}'.format(end))
    lst = []
    while True:
        for x in range(2, int(math.sqrt(start) + 1)):
            if start % x == 0:
                break
        else:
            lst.append(start)
        start += 1
        if start > end:
            return lst, print('Конец вычислений при end = {}'.format(end))


print("Последовательная работа")
start_time = time.time()
find_primes(1000000)
find_primes(2000000, 1000001)
find_primes(3000000, 2000001)
print(time.time() - start_time)
