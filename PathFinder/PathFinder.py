class PathFinder(object):
	
	def __init__(self, board):
		"""
		Initialize Pathfinder class instance.

		@type board:  Map
		@param board: board to be solved
		"""
		super(PathFinder, self).__init__()
		self.board = board

	def getPath(self):
		"""
		Get the best path to solve the given graph.

		@rtype:  [Move]
		@return: Array of moves which represent the path found to solve the puzzle
		"""
		raise NotImplementedError("Solve base class does not implement getPath.")
		