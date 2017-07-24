class Node(object):

	def __init__(self, graph, move, parent):
		"""
		Initialize AStarNode class

		@type graph:   Map
		@param graph:  Map that moves can be made on 
		@type move:    Move
		@param move:   Move that resulted in the above graph
		@type parent:  Node
		@param parent: Parent node of this. Contains previous moves to get
		               the current board.
		"""
		self.graph  = graph
		self.move   = move
		self.parent = parent

	def reconstructPath(self):
		"""
		Construct the path from here that it took to make it here.

		@rtype:  [Move]
		@return: array of moves to get to this point from the root node
		"""
		# initialize variables
		parent = self
		path   = [self.move]

		# loop through parents
		while parent != None:
			if parent.move != None:
				path.append(parent.move)
				
			parent = parent.parent

		# reverse list and return result. Remove the first as it will be None
		return list(reversed(path[1:]))		