from random import random


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.i = 0
        self.k = k

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


def random_generator(k):
    for _ in range(k):
        yield random()


if __name__ == '__main__':
    for x in RandomIterator(int(input('Enter number: '))):
        print(x)
    for y in random_generator(int(input('One more time: '))):
        print(y)
