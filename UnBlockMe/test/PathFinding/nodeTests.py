from Map.MapReader import MapReader
from PathFinder.Node import Node
from Map.Move import Move
from Map.Map import Map
from test import files
import unittest

class NodeTest(unittest.TestCase):

	def test_reconstructPath(self):
		r1        = Node(None, 1, None)
		r2        = Node(None, 2, r1)
		r3        = Node(None, 3, r2)

		self.assertEquals([1,2,3], r3.reconstructPath())

	
