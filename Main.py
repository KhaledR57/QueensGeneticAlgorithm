from GeneticAlgo import let_the_game_begin

if __name__ == '__main__':
    gen, res = let_the_game_begin(boardSize=10, populationSize=100, mutation_probability=0.4)
    print(gen)
    res.draw_chromosome()
