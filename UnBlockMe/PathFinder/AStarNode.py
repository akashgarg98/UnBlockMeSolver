from Node import Node

class AStarNode(Node):
	# step cost
	g = 0

	# heuristic cost
	h = 0

	def __init__(self, graph, move, parent, g, h):
		"""
		Initialize AStarNode class

		@type graph:   Map
		@param graph:  Map that moves can be made on 
		@type move:    Move
		@param move:   Move that resulted in the above graph
		@type parent:  AStarNode
		@param parent: Parent node of this. Contains previous moves to get
		               the current board.
		@type g:       number
		@param g:      Step cost for this node
		@type h:       number
		@param h:      Heuristic cost for this node
		"""
		super(AStarNode, self).__init__(graph, move, parent)
		self.g = g
		self.h = h

	def cost(self):
		"""
		Cost for this node.

		@rtype:  number
		@return: The cost to get to this state
		"""
		return self.g + self.h
