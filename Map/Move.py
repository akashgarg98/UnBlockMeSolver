class Move(object):
	def __init__(self, piece, up, right):
		"""
		Initialize data structure with required variables. Throws an error
		on incorrect value ranges and types given

		@type piece:  character 
		@param piece: The piece to be moved
		@type up:     integer
		@param up:    If the piece should be moved up by a space
		@type right:  integer
		@param right: If the piece should be to the right by a space
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
		return type(self.piece) == str              and \
		       ((self.up ==  1 and self.right ==  0) or \
		       	(self.up == -1 and self.right ==  0) or \
                (self.up ==  0 and self.right ==  1) or \
                (self.up ==  0 and self.right == -1))


		