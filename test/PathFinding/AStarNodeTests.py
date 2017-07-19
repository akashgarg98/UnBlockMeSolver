from PathFinder.AStarNode import AStarNode
from Map.MapReader import MapReader
from Queue import PriorityQueue
from Map.Move import Move
from Map.Map import Map
from test import files
import unittest

class NodeTest(unittest.TestCase):

	def test_cost(self):
		a1 = AStarNode(None, None, None, 2, 3)
		self.assertEquals(a1.cost(), 5)
