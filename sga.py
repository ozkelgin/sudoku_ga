import sudoku
import chromosome
import numpy as np 
import random

class SGA:
	def __init__(self, constraints, pop_size, mutation_rate, max_generations):
		self.population_size = pop_size
		self.mutation_rate = mutation_rate
		self.max_generations = max_generations
		self.constraints = constraints
		self.elite_cutoff = 0.1

		plist = []
		for i in range(self.population_size):
			s = sudoku.Sudoku(self.constraints)
			c = chromosome.Chromosome(s.generate_random_board())
			plist += [c]

		self.population = np.array(plist)

	def get_chromosome(self, idx):
		return self.population[idx]

	def rank_fitness(self):
		flist = [c.get_fitness() for c in self.population]
		fitnesses = np.array(flist)

		idx = fitnesses.argsort()
		self.population = self.population[idx]


	def parent_selection(self):
		n = int(self.population_size*self.elite_cutoff)
		midpoint = int(self.population_size/2)

		elite = self.population[:n]
		top_half = self.population[n: midpoint]
		bottom_half = self.population[midpoint:]

		elite1 = random.choices(top_half, k=n)
		elite2 = random.choices(bottom_half, k=n)
		
		non_elite1 = random.choices(top_half, k=n)
		non_elite2 = random.choices(top_half, k=n)

		p1 = [(elite[i], elite1[i]) for i in range(n)]
		p2 = [(elite[i], elite2[i]) for i in range(n)]
		p3 = [(non_elite1[i], non_elite2[i]) for i in range(n)]

		return p1 + p2 + p3

	def crossover(self, parent1, parent2):
		child_board = np.zeros((9,9), dtype=int)
		grid_map = np.random.randint(2, size=9).reshape((3,3))

		for x in range(3):
			for y in range(3):
				for i in range(3*x, 3*(x+1)):
					for j in range(3*y, 3*(y+1)):
						
						if(grid_map[x][y] == 0):
							child_board[i][j] = parent1.get_gene(i,j)
						else:
							child_board[i][j] = parent2.get_gene(i,j)

		return chromosome.Chromosome(child_board)

	def mutation(self):
		sboard = sudoku.Sudoku(self.constraints).get_sboard()
		grid_vals = sudoku.Sudoku(self.constraints).get_grid_vals()

		for i in range(int(self.elite_cutoff*self.population_size), self.population_size):
			self.population[i].mutate(self.mutation_rate, sboard, grid_vals)

	def evolution(self):
		generation = 1
		self.rank_fitness()

		while(self.population[0].get_fitness() > 0 and generation < self.max_generations):
			next_gen = []
			for i in range(int(len(self.population)*self.elite_cutoff)):
				next_gen += [self.population[i]]

			pairs = self.parent_selection()

			for p in pairs:
				for i in range(3):
					next_gen += [self.crossover(p[0], p[1])]

			for i in range(self.population_size):
				self.population[i] = next_gen[i]

			self.mutation()
			self.rank_fitness()

			generation += 1
			# print("max fitness", self.population[0].get_fitness(), " generation", generation, "mutation", self.mutation_rate)

		return self.population[0].get_fitness()



		
					


		





	


