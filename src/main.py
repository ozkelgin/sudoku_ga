import sudoku
import chromosome
import sga
import numpy as np
import random
from matplotlib import pyplot as plt
import time

"""
Saves the 1 million sudoku csv dataset into a npz file for faster access.
No inputs required
"""
def generate_sudoku_npz():
	quizzes = np.zeros((1000000, 81), np.int32)
	solutions = np.zeros((1000000, 81), np.int32)
	for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:]):
	    quiz, solution = line.split(",")
	    for j, q_s in enumerate(zip(quiz, solution)):
	        q, s = q_s
	        quizzes[i, j] = q
	        solutions[i, j] = s
	quizzes = quizzes.reshape((-1, 9, 9))
	solutions = solutions.reshape((-1, 9, 9))

	np.savez('sudoku.npz', quizzes=quizzes, solutions=solutions)

"""
Solves single sudoku game. 
Required input: empty sudoku game. 
Optional inputs: population size, mutation rate, max generations, display, and verbose.
Output: Displays the final board (unless display=False) and prints the fitness value (0 is the best). 
Optional outputs: If verbose=True, prints all generations and their respective best fitness values. 

"""
def solve_game(quiz, population_size=1000, mutation_rate=0.2, max_generations=250, display=True, verbose=False):
	sga_instance = sga.SGA(quiz, population_size, mutation_rate, max_generations)
	print(sga_instance.evolution(display=display, verbose=verbose))

"""
Solves a randomly picked subset from the million sudoku puzzle.
Required input: subset size.
Optional inputs: population size, mutation rate, max generations.
Output: graphs the final fitness values of each random game attempted.
"""
def solve_random_subset(subset_size, population_size=1000, mutation_rate=0.2, max_generations=250):
	data = np.load("..\\data\\sudoku.npz")
	quizzes = data["quizzes"]

	subset = random.choices(quizzes, k=subset_size)

	x = np.arange(0, subset_size)
	y = np.zeros_like(x)
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
