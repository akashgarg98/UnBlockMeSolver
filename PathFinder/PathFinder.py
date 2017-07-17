class PathFinder(object):
	
	def __init__(self, board):
		super(PathFinder, self).__init__()
		self.board = board

	def getPath(self):
		raise NotImplementedError("Solve base class does not implement getPath.")
		