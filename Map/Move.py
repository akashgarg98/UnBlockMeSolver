class Move(object):
	def __init__(self, piece, right, up):
		"""
		Initialize data structure with required variables. Throws an error
		on incorrect value ranges and types given

		@type piece:  character 
		@param piece: The piece to be moved
		@type right:  integer
		@param right: If the piece should be to the right by a space
		@type up:     integer
		@param up:    If the piece should be moved up by a space
		"""
		super(Move, self).__init__()
		self.piece = piece
		self.up    = up
		self.right = right

		if not self.isValid():
			raise AttributeError("Instantiated move is invalid.")

	def isValid(self):
		"""
		Ensure that the move is valid for the board and the piece
		is a character.
		"""
		# first check if the type of piece is a character and the
		# direction of the move is horizontal or vertical and not
		# diagnol
		return type(self.piece) == str             and \
		       ((self.up != 0 and self.right == 0)  or \
		       	(self.up != 0 and self.right == 0)  or \
		        (self.up == 0 and self.right != 0)  or \
		        (self.up == 0 and self.right != 0))

	def equals(self, move):
		"""
		Test whether the two moves are equal.

		@type move:  Move
		@param move: Move being tested for equality
		@rtype:      boolean
		@return:     Whether the two moves are equal
		"""
		return self.piece == move.piece and self.right == move.right and self.up == move.up

	def toStr(self):
		"""
		Convert self to string.

		@rtype:  str
		@return: String representation of the move
		"""
		return str(self.piece + ", " + str(self.right) + ", " + str(self.up))

	@staticmethod
	def left(piece, size=1):
		"""
		Instantiate a move that will go left

		@type piece:  character
		@param piece: Character that represents the piece to be moved
		"""
		return Move(piece, -abs(size), 0)

	@staticmethod
	def right(piece, size=1):
		"""
		Instantiate a move that will go right

		@type piece:  character
		@param piece: Character that represents the piece to be moved
		"""
		return Move(piece, abs(size), 0)

	@staticmethod
	def up(piece, size=1):
		"""
		Instantiate a move that will go up

		@type piece:  character
		@param piece: Character that represents the piece to be moved
		"""
		return Move(piece, 0, -abs(size))

	@staticmethod
	def down(piece, size=1):
		"""
		Instantiate a move that will go down

		@type piece:  character
		@param piece: Character that represents the piece to be moved
		"""
		return Move(piece, 0, abs(size))
