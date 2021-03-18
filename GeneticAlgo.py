import random

from Chromosome import Chromosome


def _generate_chromosome(boardSize):
    positions = random.sample(range(boardSize), boardSize)
    return positions


def generate_population(boardSize, populationSize):
    population = [Chromosome(_generate_chromosome(boardSize)) for _ in range(populationSize)]
    return population


def cross_over(x, y):
    x = x.get_chromosome()
    y = y.get_chromosome()
    n = len(x)
    split = random.randint(0, n - 1)
    return Chromosome(x[0:split] + y[split:])


def random_pick(population):
    return population[random.randint(0, len(population) - 1)]


def thanos_gauntlet(population):
    population.sort(key=lambda val: val.get_fitness())
    return population[0:int(len(population) / 4) + 1]


def genetic_algo(boardSize, populationSize, mutation_probability):
    new_population = []
    population = generate_population(boardSize, populationSize)
    survivors = thanos_gauntlet(population)  # select parents (snap)
    for _ in range(len(population)):
        x = random_pick(survivors)  # pick random parent from survivors
        y = random_pick(survivors)  # pick random parent from survivors
        child = cross_over(x, y)
        if random.random() < mutation_probability and child.get_fitness() != 0:
            child.mutate()
        new_population.append(child)
        if child.get_fitness() == 0:
            break
    return new_population


def let_the_game_begin(boardSize=5, populationSize=30, mutation_probability=0.7, generation=-1):
    gen = 0
    fittest = None
    while generation != gen:
        population = genetic_algo(boardSize, populationSize, mutation_probability)
        fittest = min(population, key=lambda val: val.get_fitness())
        gen += 1
        if fittest.get_fitness() == 0:
            break
    return gen, fittest
