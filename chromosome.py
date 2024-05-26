import sudoku
import numpy as np 

class Chromosome:
	def __init__(self, chromosome):
		self.chromosome = chromosome
	
	def get_gene(self, row, col):
		return self.chromosome[row][col]

	def set_gene(self, row, col, val):
		self.chromosome[row][col] = val
	
	def get_fitness(self):
		num_repeats = 0
		rowlist = []
		collist = []
		chrom = self.chromosome

		for i in range(9):
			for x in chrom[:,i]:
				if x not in rowlist:
					rowlist += [x]

			for y in chrom[i,:]:
				if y not in collist:
					collist += [y]

			num_repeats += 18-len(rowlist)-len(collist)
			rowlist = []
			collist = []

		return num_repeats

	def mutate(self, mutation_rate, sboard, grid_vals):
		mutation_grid = np.random.rand(3,3)
		for x in range(3):
			for y in range(3):
				n = len(grid_vals[(x, y)])
				cutoff = int(n/2)
				loc1 = np.random.randint(cutoff)
				loc2 = np.random.randint(cutoff, n)
				if mutation_rate > mutation_grid[x][y] and n > 1:
					self.mutate_helper(x, y, sboard, loc1, loc2)

	def mutate_helper(self, x, y, sboard, loc1, loc2):
		temp = (0,0,0)
		count = 0
		for i in range(3*x, 3*(x+1)):
			for j in range(3*y, 3*(y+1)):
					if sboard[i][j] == False and count == loc1:
						temp = (i, j, self.get_gene(i,j))
						count += 1
					elif sboard[i][j] == False and count == loc2:
						self.set_gene(temp[0], temp[1], self.get_gene(i, j))
						self.set_gene(i, j, temp[2])
						count += 1
					elif sboard[i][j] == False:
						count += 1

	def display(self):
		res = ""
		for col in range(9):
			for row in range(9):
				res += str(self.get_gene(row,col))
				if(row == 2 or row == 5):
					res += "|"
				else:
					res += " "

			res += "\n"

			if(col == 2 or col == 5):
					for i in range(17):
						res += "-"

					res+= "\n"
		print(res)