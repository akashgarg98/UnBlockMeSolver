from Map.mapReader import MapReader
from Map.mapReader import Map
from test import files
import unittest
import copy


class FakeMapReader(object):
	"""
	Fake object with method and member similar to mapreader
	class that the map class relies on
	"""
	def __init__(self):
		super(FakeMapReader, self).__init__()
		self.graph = None
		
	def get(self):
		pass

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

	def test_convertToMap(self):
		# initalizing class to test function on
		tester   = Map(self.sample_string)
		tester.convertToMap()
		str_list = self.sample_string.split('\n') 

		# test to make sure each row is properly changed
		for i in range(len(str_list)):
			self.assertEquals(tester.graph[i], list(str_list[i]))

	def test_setUp(self):
		# initalizing class to test function on
		tester   = Map(self.sample_string)

		# assume no exception is raised and everything is fine
		tester.setUp()

		# create tester with fake object which should throw a 
		# type error
		tester   = Map(FakeMapReader())
		with self.assertRaises(TypeError):
			tester.setUp()

		# test with a map reader. No exception should be thrown,
		# which means this will pass
		mr     = MapReader()
		mr.load(files.good)
		tester = Map(mr)
		tester.setUp()

		# test for a syntax error to be thrown when given an
		# invalid file
		mr     = MapReader()
		mr.load(files.bad_col)
		tester = Map(mr)
		with self.assertRaises(SyntaxError):
			tester.setUp()

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
		tester.convertToMap()

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

	def test_numColumnsMatch(self):
		# Test for standard example that should work
		tester       = Map(self.sample_string)
		tester.convertToMap()
		self.assertTrue(tester.numColumnsMatch())

		# Test for when the first row is different from the rest
		string          = copy.copy(self.sample_string)
		tester          = Map(string)
		tester.convertToMap()
		tester.graph[0] = tester.graph[0:-1]
		self.assertFalse(tester.numColumnsMatch())

		# Test for  when the last row is different from the rest
		string           = copy.copy(self.sample_string)
		tester           = Map(string)
		tester.convertToMap()
		tester.graph[-1] = tester.graph[0:-1]
		self.assertFalse(tester.numColumnsMatch())

	def test_topBottomRowsValid(self):
		# test both top and bottom valid
		tester            = Map(self.sample_string)
		tester.convertToMap()
		result, num_goals = tester.topBottomRowsValid(0)
		self.assertTrue(result)
		self.assertEquals(num_goals, 0)

		# test top row invalid
		string             = copy.copy(self.sample_string)
		tester             = Map(string)
		tester.convertToMap()
		tester.graph[0][1] = 'a'
		result, num_goals  = tester.topBottomRowsValid(0)
		self.assertFalse(result)
		self.assertEquals(num_goals, 0)

		# test bottom row invalid
		string              = copy.copy(self.sample_string)
		tester              = Map(string)
		tester.convertToMap()
		tester.graph[-1][2] = 'a'
		result, num_goals   = tester.topBottomRowsValid(0)
		self.assertFalse(result)
		self.assertEquals(num_goals, 0)

		# test both top and bottom rows invalid
		string              = copy.copy(self.sample_string)
		tester              = Map(string)
		tester.convertToMap()
		tester.graph[0][1]  = 'a'
		tester.graph[-1][3] = 'a'
		result, num_goals   = tester.topBottomRowsValid(0)
		self.assertFalse(result)
		self.assertEquals(num_goals, 0)

	def test_playerFound(self):
		# test for example where player is in the map
		tester            = Map(self.sample_string)
		tester.convertToMap()
		self.assertTrue(tester.playerFound())

		# test on example where no player is in the map
		string = copy.copy(self.sample_string)
		string = string.replace(tester.player, '00')
		tester = Map(string)
		tester.convertToMap()
		self.assertFalse(tester.playerFound())

	def test_isValid(self):
		# test for valid string
		tester = Map(self.sample_string)
		tester.convertToMap()
		self.assertTrue(tester.isValid())

		# test for valid mapreader
		mr     = MapReader()
		mr.load(files.good)
		tester = Map(mr)
		tester.setUp()
		self.assertTrue(tester.isValid())

		# test for invalid column count
		mr     = MapReader()
		mr.load(files.bad_col)
		tester = Map(mr)
		with self.assertRaises(SyntaxError):
			tester.setUp()

		# test for empty map
		mr     = MapReader()
		mr.load(files.empty)
		tester = Map(mr)
		with self.assertRaises(SyntaxError):
			tester.setUp()

		# test on there being no player
		mr     = MapReader()
		mr.load(files.no_player)
		tester = Map(mr)
		with self.assertRaises(SyntaxError):
			tester.setUp()

		# test on a string being given
		mr     = MapReader()
		mr.load(files.sample)
		tester = Map(mr)
		with self.assertRaises(SyntaxError):
			tester.setUp()

if __name__ == '__main__':
    unittest.main()