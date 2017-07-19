from PathFinder import PathFinder
from Queue import PriorityQueue
from AStarNode import AStarNode
from Heuristics import *

class AStar(PathFinder):

	def heuristic(self, board):
		# TODO: document
		# position of player has to be adjusted based on where the player is
		return manhattan(board.pieces[board.playerPiece].x + len(board.player), board.pieces[board.playerPiece].y, \
			             board.pieces[board.goal].x, board.pieces[board.goal].y)

	def populateQueue(self, graph, queue, parent):
		# TODO: document

		# get possible moves
		moves = graph.getMoves()

		# put into queue all the moves possible
		for move in moves:
			# make move and get copy
			newBoard = graph.copyConfidentMove(move)

			# calculate heuristic for this move that was made
			h = self.heuristic(newBoard)

			# create node
			node = AStarNode(newBoard, move, parent, parent.g + 1, h)

			# put the node in priority queue
			queue.put((node.cost(), node))

	def getPath(self):
		# TODO: document
		# make sure the board isn't already solved
		if self.board.isSolved():
			return None

		# initialize data structures for A*
		queue    = PriorityQueue()
		explored = {self.board.hash: True}

		# populate queue with moves and nodes
		self.populateQueue(self.board, queue, AStarNode(None, None, None, 0, 0))

		while not queue.empty():
			# get the next position from the queue
			cost, node = queue.get()

			# make sure this position hasn't been explored
			if node.graph.hash not in explored:
				# check if the board is solved
				if node.graph.isSolved():
					return node.reconstructPath()

				# if not solved, add to explored and populate queue
				explored[node.graph.hash] = True
				self.populateQueue(node.graph, queue, node)

		return None

