import random

import numpy as np


class Chromosome:

    def __init__(self, chromosome):
        self._chromosome = chromosome
        self._fitness = self._chromosome_fitness()

    def _chromosome_fitness(self):
        clashes = 0
        # just subtract the unique length of array from total length of array
        # [1,1,1,2,2,2] - [1,2] => 4 clashes
        row_col_clashes = abs(len(self._chromosome) - len(np.unique(self._chromosome)))
        clashes += row_col_clashes
        # calculate diagonal clashes
        for i in range(len(self._chromosome)):
            for j in range(len(self._chromosome)):
                if i != j:
                    dx = abs(i - j)
                    dy = abs(self._chromosome[i] - self._chromosome[j])
                    if dx == dy:
                        clashes += 1
        return clashes

    def mutate(self):
        n = len(self._chromosome)
        x = random.randint(0, int((n - 1) / 2))  # random index
        y = random.randint(int((n - 1) / 2) + 1, n - 1)  # random index
        self._chromosome[x], self._chromosome[y] = self._chromosome[y], self._chromosome[x]  # swap
        self._fitness = self._chromosome_fitness()  # update fitness

    def draw_chromosome(self):
        length = len(self._chromosome)
        for i in range(length):
            st = ""
            for j in range(length):
                if self._chromosome[j] == i:
                    st += ' * '
                else:
                    st += ' - '
            print(st)

    def get_fitness(self):
        return self._fitness

    def get_chromosome(self):
        return self._chromosome
