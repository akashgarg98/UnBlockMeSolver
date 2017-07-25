def toGraphs(board, path):
	"""
	Get a list of all the board positions that result in a 
	solved board.

	@type board:  Map
	@param board: Board to run path on
	@type path:   [Move]
	@param path:  Array of moves to generate baords
	@rtype:       [string]
	@return:      Array of string representation of boards
	"""
	boards = [board.hash]

	for move in path:
		board.makeConfidentMove(move)
		boards.append(board.hash)

	return boards
