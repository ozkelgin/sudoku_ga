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

subset = random.choices(quizzes, k=50)

x = np.arange(0, 50)
y = np.zeros_like(x)

for i in range(50):
	sga_instance = sga.SGA(subset[i], 1000, 0.1, 50)
	y[i] = sga_instance.evolution()

plt.plot(x, y)
plt.show()

# start = time.time()

# sga_instance = sga.SGA(quizzes[0], 1000, 0.1, 50)
# sga_instance.evolution()

# end = time.time()

# print((end-start), "s")

