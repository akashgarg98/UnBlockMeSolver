from Map.mapReader import Map
from test import files
import unittest

class TestMap(unittest.TestCase):

	sample_string = "|||||\n" + \
	                "|000|\n" + \
	                "|**0$\n" + \
	                "|||||"

	default_delimeter = "\n"
	new_delimeter     = ","

	def test_init(self):
		## test if string and default delimeter works
		t1 = Map(self.sample_string)

		self.assertEquals(t1.delimeter, self.default_delimeter)
		self.assertEquals(t1.graph, self.sample_string)

		## test changing the delimeter
		t1 = Map(self.sample_string, delimeter=self.new_delimeter)

		self.assertEquals(t1.delimeter, self.new_delimeter)
		self.assertEquals(t1.graph, self.sample_string)

	def test_isWallOrGoal(self):
		# initalizing class to test function on
		tester = Map(self.sample_string)

		## Test if wall is valid
		isWall, num_goals = tester.isWallOrGoal(tester.wall, 0)
		self.assertTrue(isWall)
		self.assertEquals(num_goals, 0)

		## Test if goal is valid
		isWall, num_goals = tester.isWallOrGoal(tester.goal, 0)
		self.assertTrue(isWall)
		self.assertEquals(num_goals, 1)

		## test if random character fails
		isWall, num_goals = tester.isWallOrGoal(tester.player, 0)
		self.assertFalse(isWall)
		self.assertEquals(num_goals, 0)

	def test_largeRowValid(self):
		# initalizing class to test function on
		tester       = Map(self.sample_string)
		tester.graph = tester.graph.split(tester.delimeter)

		# test top row
		valid, num_goals = tester.largeRowValid(0, 0)
		self.assertTrue(valid)
		self.assertEquals(num_goals, 0)

		# test bottom row
		valid, num_goals = tester.largeRowValid(len(tester.graph) - 1, 0)
		self.assertTrue(valid)
		self.assertEquals(num_goals, 0)

		# test middle row to make sure it fails
		valid, num_goals = tester.largeRowValid(1, 0)
		self.assertFalse(valid)
		self.assertEquals(num_goals, 0)

		# test middle row to make sure the num goals is not updated
		# because an error has already been found
		valid, num_goals = tester.largeRowValid(2, 0)
		self.assertFalse(valid)
		self.assertEquals(num_goals, 0)


if __name__ == '__main__':
    unittest.main()