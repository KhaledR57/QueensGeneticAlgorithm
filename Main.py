from GeneticAlgo import let_the_game_begin

if __name__ == '__main__':
    gen, res = let_the_game_begin(boardSize=12, populationSize=300, mutation_probability=0.2)
    print(gen)
    res.draw_chromosome()
