class Map(object):

	wall   = "|"
	goal   = "$"
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
		# split the string by the delimeter to create the graph
		self.graph = self.graph.split(self.delimeter)
		self.graph = [list(self.graph[i]) for i in range(len(self.graph))]

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

	def isWallOrGoal(self, point, num_goals_found):
		"""
		This will check if the point is a wall or goal and if not return 
		False. Additionally, it will update the number of goals that 
		have been found. 

		@type point:  character
		@param point: the point being checked in the graph. 
		@type num_goals_found:  integer
		@param num_goals_found: number of goals in the graph currently found
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

		@type row_index:  integer
		@param row_index: index for the row to be checked
		@type num_goals_found:  integer
		@param num_goals_found: the number of goals that have been found
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
		Update documentation
		"""
		# check if the number of columns is the same as every row
		col_length = len(self.graph[0])
		for i in range(1, len(self.graph)):
			if col_length != len(self.graph[i]):
				return False

		return True

	def topBottomRowsValid(self, num_goals_found):
		"""
		Update documentation
		"""
		# first check the first and last row
		valid_first,  num_goals_found = self.largeRowValid(0, num_goals_found)
		valid_second, num_goals_found = self.largeRowValid(len(self.graph) - 1, num_goals_found)

		# if either are invalid than the graph is not valid
		return valid_first and valid_second, num_goals_found

	def midRowsValid(self, num_goals_found):
		"""
		Update documentation
		"""
		# now check to make sure the other rows are surrounded by walls
		for i in range(len(self.graph)):
			close_result, num_goals_found = self.isWallOrGoal(self.graph[i][0], num_goals_found)
			far_result,   num_goals_found = self.isWallOrGoal(self.graph[i][len(self.graph[i]) - 1], num_goals_found)

			if not close_result or not far_result:
				return False, num_goals_found

		return True, num_goals_found

	def playerFound(self):
		"""
		Update documentation
		"""
		# loop through avoiding the edges in the map
		for i in range(1, len(self.graph) - 1):
			if self.player in ''.join(self.graph[i]):
				return True
		return False


	def isValid(self):
		"""
		Test if the graph in the map class is valid or not

		@rtype:  boolean
		@returN: graph is valid or not
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
		