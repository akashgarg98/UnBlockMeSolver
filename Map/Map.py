from Piece import Piece
from Move import Move
import traceback

class Map(object):

	# default pieces in a map
	wall   = "|"
	goal   = "$"
	empty  = "0"
	player = "**"

	def __init__(self, graph, delimeter='\n'):
		"""
		Initialize the class by setting the graph and delimeters variables.

		@type graph:      string | MapReader
		@param graph:     Represents the board that the game will be played on
		@type delimeter:  string
		@param delimeter: how to split the string
		"""
		super(Map, self).__init__()
		self.graph     = graph
		self.delimeter = delimeter

	def convertToMap(self):
		"""
		Convert the graph into a matrix that can be viewed and modified.
		"""
		# split the string by the delimeter to create the graph
		self.graph = self.graph.split(self.delimeter)

		# turn each string into an array of characters and make the new
		# array a member of the matrix
		self.graph = [list(self.graph[i]) for i in range(len(self.graph))]

	def setUpPieces(self):
		"""
		Find every piece available in the board and add it to an array
		to keep track of them for future use.
		"""
		self.pieces = {}

		for y in range(1, len(self.graph) - 1):
			for x in range(1, len(self.graph[y]) - 1):
				piece = self.graph[y][x]

				# make sure that this is a piece worth noting
				if piece != self.wall and piece != self.goal and \
				   piece != self.empty and piece not in self.pieces:
					# if there is a piece with the same kind to the right then
					# this is a horizontal piece. No checks are done for bounds
					# due to for loop structure
					if self.graph[y][x + 1] == piece:
						self.pieces[piece] = Piece(x, y, False)
					elif self.graph[y + 1][x] == piece:
						self.pieces[piece]  = Piece(x, y, True)

	def setUp(self):
		"""
		Set up the Map class and set the graph by either getting a
		a string from either a map reader or string as the graph 
		and breaking if not valid.
		"""
		# if the type is not a string
		if type(self.graph) != str:
			# get the string from the reader
			self.graph = self.graph.get()

		# if the type of graph is not string anymore than something
		# should be thrown here
		if type(self.graph) != str:
			raise TypeError("Incorrect type given to Map class (must be string or MapReader).")

		# convert the graph into a matrix that is reassignable
		self.convertToMap()

		# check if the graph created is valid
		if not self.isValid():
			# if the graph is not valid than raise an exception
			raise SyntaxError("Graph created is not valid. Refer to sample maps provided.")

		# get the pieces on the board to set up the 
		self.setUpPieces()

	def isWallOrGoal(self, point, num_goals_found):
		"""
		This will check if the point is a wall or goal and if not return 
		False. Additionally, it will update the number of goals that 
		have been found. 

		@type point:  character
		@param point: the point being checked in the graph. 
		@type num_goals_found:  integer
		@param num_goals_found: number of goals in the graph currently found
		@rtype:                 boolean, integer
		@return:                if the point is a wall or a goal and number of goals currently found
		"""
		# if it isn't a wall
		if point != self.wall: 
			# and it isn't a goal
			if point != self.goal:
				# them, the row isn't valid
				return False, num_goals_found
			else:
				# it is valid and we have a goal
				num_goals_found += 1

		return True, num_goals_found

	def largeRowValid(self, row_index, num_goals_found):
		"""
		This will test on the larger rows to see if it is valid. A 
		larger row indicates that it is either the top or the bottom
		of the graph. 

		@type row_index:        integer
		@param row_index:       index for the row to be checked
		@type num_goals_found:  integer
		@param num_goals_found: the number of goals that have been found
		@rtype:                 boolean, integer
		@return:                If a large row provided is valid and number of 
		                        goals currently found
		"""
		for j in range(len(self.graph[row_index])):
			result, num_goals_found = self.isWallOrGoal(self.graph[row_index][j], num_goals_found)

			# if the piece was not a wall or goal then we should break out because
			# the row is not valid and return false
			if result == False:
				return False, num_goals_found

		return True, num_goals_found

	def numColumnsMatch(self):
		"""
		Ensure that the number of columns matches for each row.

		@rtype:  boolean
		@return: if the number of columns matches for each row
		"""
		col_length = len(self.graph[0])
		for i in range(1, len(self.graph)):
			if col_length != len(self.graph[i]):
				return False

		return True

	def topBottomRowsValid(self, num_goals_found):
		"""
		Make sure that both the top and bottom rows are valid according
		to the topBottomRowsValid function.

		@type num_goals_found:  integer
		@param num_goals_found: number of goals presently found
		@rtype:                 boolean, integer
		@return:                If the top and bottom rows are valid and 
		                        number of goals currently found 
		"""
		# first check the first and last row
		valid_first,  num_goals_found = self.largeRowValid(0, num_goals_found)
		valid_second, num_goals_found = self.largeRowValid(len(self.graph) - 1, num_goals_found)

		# if either are invalid than the graph is not valid
		return valid_first and valid_second, num_goals_found

	def midRowsValid(self, num_goals_found):
		"""
		Ensure that all the middle rows are valid entries with walls or
		a goal on both sides.

		@type num_goals_found:  integer
		@param num_goals_found: number of goals presently found
		@rtype:                 boolean, integer
		@return:                if the middle rows are valid and the number
		                        of goals currently found
		"""
		for i in range(1, len(self.graph) - 1):
			close_result, num_goals_found = self.isWallOrGoal(self.graph[i][0], num_goals_found)
			far_result,   num_goals_found = self.isWallOrGoal(self.graph[i][len(self.graph[i]) - 1], num_goals_found)

			if not close_result or not far_result:
				return False, num_goals_found

		return True, num_goals_found

	def playerFound(self):
		"""
		Check to see if the player, defined in Map.py, is in the map.

		@rtype:  boolean
		@return: player found in map
		"""
		# loop through avoiding the edges in the map
		for i in range(1, len(self.graph) - 1):
			if self.player in ''.join(self.graph[i]):
				return True
		return False

	def isValid(self):
		"""
		Test if the graph in the map class is valid or not.

		@rtype:  boolean
		@return: graph is valid or not
		"""
		# there must be atleast 3 rows in the graph else, the 
		# puzzle can't be solved
		if len(self.graph) < 3:
			return False

		# make sure the number of columsn for each row works
		if not self.numColumnsMatch():
			return False

		# Check to make sure there is only one goal and contains
		# is completely surrounded by walls
		num_goals_found = 0

		# make sure the middle rows of the board are valid
		midValid, num_goals_found = self.midRowsValid(num_goals_found)
		if not midValid:
			return False

		# make sure top and bottom rows are valid
		topBotValid, num_goals_found = self.topBottomRowsValid(num_goals_found)
		if not topBotValid:
			return False

		# now make sure there is only one goal and return the result
		if num_goals_found != 1:
			return False

		# Check to make sure player is in the game and return the result
		return self.playerFound()

	def isValidAdditionMove(self, move):
		"""
		This will handle move verificatin for moving to the right or
		down in the board. If it is possible it will return True

		@type move: Move
		@param move: MOve that is being checked
		"""
		if move.up != 1 and move.right != 1:
			return False

		# get piece information
		x = self.pieces[move.piece].x
		y = self.pieces[move.piece].y

		# update x or y coordinate depending on the move
		if move.up == 0:
			x += 1
		else: 
			y += 1

		# avoid walls
		while x < len(self.graph[0]) and y < len(self.graph):
			# if the point is not a piece 
			if self.graph[y][x] != move.piece:
				# if the next space is empty
				if self.graph[y][x] == self.empty or self.graph[y][x] == self.goal:
					# add move
					return True

				break

			# increment variable
			if move.up == 0: x += 1
			else:            y += 1

		return None

	def isValidSubtractionMove(self, move):
		"""
		This will handle move verificatin for moving to the left or
		up in the board. If it is possible it will return True

		@type move: Move
		@param move: MOve that is being checked
		"""
		if move.up != -1 and move.right != -1:
			return False

		# get piece information
		x = self.pieces[move.piece].x
		y = self.pieces[move.piece].y

		# update x or y coordinate depending on the move
		if move.up == 0:
			x -= 1
		else: 
			y -= 1

		# avoid walls when checking new x or y position
		if y >= 0 and x >= 0: 
			if self.graph[y][x] == self.empty or self.graph[y][x] == self.goal:
				return True

		return None

	def isValidMove(self, move):
		# check the type and if the type is valid check if the moved
		# is also valid
		if type(move) != Move or not move.isValid():
			return False

		return self.isValidAdditionMove(move) or self.isValidSubtractionMove(move)

	def makeConfidentMove(self, move):
		"""
		Make a move on the board without checking for its validity.

		@type move:  Move
		@param move: move to make on the board
		"""
		# move on the board
		x = self.pieces[move.piece].x
		y = self.pieces[move.piece].y

		# find the point the furthest over and put in a new piece
		while self.graph[y][x] == move.piece:
			x += move.right
			y += move.up

		self.graph[y][x] = move.piece

		# trace back and put in an empty piece in the last avaialble piece
		while self.graph[y][x] == move.piece:
			x -= move.right
			y -= move.up

		self.graph[y + move.up][x + move.right] = self.empty

		# move piece in pieces dictionary
		self.pieces[move.piece].move(move)

	def makeMove(self, move):
		"""
		Make a move on the board. Raise syntax error on bad move given

		@type move:  Move
		@param move: move to make on the board
		"""
		if self.isValidMove(move):
			self.makeConfidentMove(move)
		else:
			raise SyntaxError("Invalid move given.")

	def getMoves(self):
		"""
		Get the moves available on the board.

		@rtype:  [Move]
		@return: Array of moves available
		"""
		moves = []

		for piece in self.pieces:
			if self.pieces[piece].isVertical:
				up   = Move.up(piece)
				down = Move.down(piece)

				if self.isValidSubtractionMove(up): moves.append(up)
				if self.isValidAdditionMove(down):  moves.append(down)
			else:
				left  = Move.left(piece)
				right = Move.right(piece)

				if self.isValidSubtractionMove(left): moves.append(left)
				if self.isValidAdditionMove(right):   moves.append(right)

		return moves

	def isSolved(self):
		raise NotImplementedError("isSolved not implemented")


		