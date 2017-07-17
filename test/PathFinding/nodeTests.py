from Map.MapReader import MapReader
from PathFinder.Node import Node
from Map.Move import Move
from Map.Map import Map
from test import files
import unittest

class NodeTest(unittest.TestCase):

	def test_reconstructPath(self):
		r1        = Node()
		r1.move   = 1
		r1.parent = None
		r2        = Node()
		r2.move   = 2
		r2.parent = r1
		r3        = Node()
		r3.move   = 3
		r3.parent = r2

		self.assertEquals([1,2,3], r3.reconstructPath())

	
