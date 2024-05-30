import numpy as np

class Sudoku:
	def __init__(self, board):
		self.board = board
		self.sboard = np.where(board == 0, False, True)
		self.grid_vals = {}
		for i in range(3):
			for j in range(3):
				self.grid_vals[(i, j)] = list([1,2,3,4,5,6,7,8,9])

	def get_board(self):
		return self.board

	def set_board(self, board):
		self.board = board

	def get_value(self, row, col):
		return self.get_board()[row][col]

	def set_value(self, row, col, val):
		self.board[row][col] = val

	def get_sboard(self):
		return self.sboard

	def is_static(self, row, col):
		return self.get_sboard()[row][col]

	def get_grid_vals(self):
		for i in range(9):
			for j in range(9):
				x = int(i / 3)
				y = int(j / 3)
				val = self.get_value(i, j)
				if self.is_static(i, j) and val in self.grid_vals[(x, y)]:
					self.grid_vals[(x, y)].remove(val)			
		
		return self.grid_vals

	def generate_random_board(self):
		grid_vals = self.get_grid_vals()
		board = np.zeros((9,9), dtype=int)
		for i in range(9):
			for j in range(9):
				if self.get_value(i, j) == 0:
					x = int(i / 3)
					y = int(j / 3)
					val = np.random.choice(grid_vals[(x, y)])
					board[i][j] = val
					grid_vals[(x,y)].remove(val)
				else:
					board[i][j] = self.get_value(i, j)

		return board
	

	def __str__(self):
		res = ""
		
		for col in range(9):
			for row in range(9):
				res += str(self.get_value(row,col))
				if(row == 2 or row == 5):
					res += "|"
				else:
					res += " "

			res += "\n"

			if(col == 2 or col == 5):
					for i in range(17):
						res += "-"

					res+= "\n"
		
		return res


