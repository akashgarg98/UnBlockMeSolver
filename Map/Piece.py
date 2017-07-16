from Move import Move

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
		Move the piece if the given move is valid

		@type move:  Move
		@param move: Move that will change the location of the piece
		"""
		if type(move) != Move:
			raise AttributeError("Incorrect type given to move a piece")

		if not move.isValid():
			raise AttributeError("Move given is not valid and can't be used")

		if self.isVertical:
			if move.up == 0:
				raise AttributeError("Horizontal move given for piece that can only move vertically")
		elif move.right == 0:
			raise AttributeError("Vertical move given for piece that can only move horizontally")

		self.x += move.right
		self.y += move.up