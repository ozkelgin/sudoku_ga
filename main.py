import sudoku
import chromosome
import sga
import numpy as np
import random
from matplotlib import pyplot as plt
import time

"""Turning csv data into saved numpy arrays"""

# quizzes = np.zeros((1000000, 81), np.int32)
# solutions = np.zeros((1000000, 81), np.int32)
# for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:]):
#     quiz, solution = line.split(",")
#     for j, q_s in enumerate(zip(quiz, solution)):
#         q, s = q_s
#         quizzes[i, j] = q
#         solutions[i, j] = s
# quizzes = quizzes.reshape((-1, 9, 9))
# solutions = solutions.reshape((-1, 9, 9))

# np.savez('sudoku.npz', quizzes=quizzes, solutions=solutions)

data = np.load('sudoku.npz')

quizzes = data['quizzes']
solutions = data['solutions']
# c = chromosome.Chromosome(s1.get_board())
# c.display()
subset_size = 100
subset = random.choices(quizzes, k=subset_size)

x = np.arange(0, subset_size)
y = np.zeros_like(x)

population_size = 1000
mutation_rate = 0.2
max_generations = 100
solved_games = 0

for i in range(subset_size):
	sga_instance = sga.SGA(subset[i], population_size, mutation_rate, max_generations)
	y[i] = sga_instance.evolution()
	if y[i] == 0:
		solved_games += 1

plt.plot(x, y)
plt.title(str(solved_games) + " games solved out of " + str(subset_size) +  " games with population_size: " + str(population_size) +  " mutation_rate: " + str(mutation_rate) + " max_generations: " + str(max_generations))
plt.xlabel("Games chosen randomly from the million sudoku dataset")
plt.ylabel("Fitness value (number of repeated numbers in solution)")
plt.show()
