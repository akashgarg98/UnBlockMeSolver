from PathFinder import Heuristics
import unittest
import math

class TestMap(unittest.TestCase):

	def test_manhattan(self):
		self.assertEquals(Heuristics.manhattan(3,3,2,2), 2)
		self.assertEquals(Heuristics.manhattan(3,3,4,4), 2)
		self.assertEquals(Heuristics.manhattan(-1,3,-3,4), 3)

	def test_euclidian(self):
		self.assertEquals(Heuristics.euclidian(3,5,2,2), math.sqrt(10))
		self.assertEquals(Heuristics.euclidian(5,3,3,5), math.sqrt(8))