class Piece(object):
	def __init__(self, x, y, vertical):
		"""
		Initialize piece class

		@type x:         integer
		@param x:        x coordinate
		@type y:         integer
		@param y:        y coordinate
		@type vertical:  boolean
		@param vertical: marks whether this piece can move vertically or not
		"""
		super(Piece, self).__init__()

		if type(x) != int or type(y) != int or type(vertical) != bool:
			raise AttributeError("Incorrect types given for class Piece")

		self.x          = x
		self.y          = y
		self.isVertical = vertical

	def move(self, move):
		"""
		TODO: Update documentation
		"""

		raise NotImplementedError("not implemented yet.")