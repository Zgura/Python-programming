"""Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного
числа start (по умолчанию 3) до заданного числа end. Далее необходимо:
Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью
multiprocessing.Process. Что будет, если 'забыть' выполнить start или join для процессов? """
import math
import time
import multiprocessing


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


if __name__ == '__main__':
    start_time = time.time()
    print("Так работают процессы")
    p1 = multiprocessing.Process(target=find_primes, args=(100000,))
    p2 = multiprocessing.Process(target=find_primes, args=(200000, 100001))
    p3 = multiprocessing.Process(target=find_primes, args=(300000, 200001))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(time.time() - start_time)
