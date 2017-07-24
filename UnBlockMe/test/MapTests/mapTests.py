from Map.MapReader import MapReader
from Map.Piece import Piece
from Map.Move import Move
from Map.Map import Map
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

	def test_setUpPieces(self):
		# test on simple file to make sure the pieces are properly
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)

		# make sure only one valid piece is found
		self.assertEquals(len(tester.pieces), 2)

		# make sure the piece found is coherent to the expected values
		valid_piece = Piece(1,1,False)
		self.assertEquals(tester.pieces['*'].x,          valid_piece.x)
		self.assertEquals(tester.pieces['*'].y,          valid_piece.y)
		self.assertEquals(tester.pieces['*'].isVertical, valid_piece.isVertical)

		# test if the goal piece is found
		valid_piece = Piece(4,1,None)
		self.assertEquals(tester.pieces['$'].x,          valid_piece.x)
		self.assertEquals(tester.pieces['$'].y,          valid_piece.y)
		self.assertEquals(tester.pieces['$'].isVertical, valid_piece.isVertical)

	def test_init(self):
		## test if string and default delimeter works
		t1 = Map(self.sample_string, setUp=False)

		self.assertEquals(t1.delimeter, self.default_delimeter)
		self.assertEquals(t1.graph, self.sample_string)

		## test changing the delimeter
		t1 = Map(self.sample_string, setUp=False, delimeter=self.new_delimeter)

		self.assertEquals(t1.delimeter, self.new_delimeter)
		self.assertEquals(t1.graph, self.sample_string)

	def test_convertToMap(self):
		# initalizing class to test function on
		tester   = Map(self.sample_string, setUp=False)
		tester.convertToMap()
		str_list = self.sample_string.split('\n') 

		# test to make sure each row is properly changed
		for i in range(len(str_list)):
			self.assertEquals(tester.graph[i], list(str_list[i]))

	def test_setUp(self):
		# initalizing class to test function on and assume no exception 
		# is raised and everything is fine
		tester = Map(self.sample_string)

		# create tester with fake object which should throw a 
		# type error
		with self.assertRaises(TypeError):
			tester = Map(FakeMapReader())

		# test with a map reader. No exception should be thrown,
		# which means this will pass
		mr     = MapReader()
		mr.load(files.good)
		tester = Map(mr)

		# test for a syntax error to be thrown when given an
		# invalid file
		mr     = MapReader()
		mr.load(files.bad_col)
		
		with self.assertRaises(SyntaxError):
			tester = Map(mr)

	def test_isWallOrGoal(self):
		# initalizing class to test function on
		tester = Map(self.sample_string, setUp=False)

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
		tester       = Map(self.sample_string, setUp=False)
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
		tester       = Map(self.sample_string, setUp=False)
		self.assertTrue(tester.numColumnsMatch())

		# Test for when the first row is different from the rest
		string          = copy.copy(self.sample_string)
		tester          = Map(string, setUp=False)
		tester.convertToMap()
		tester.graph[0] = tester.graph[0:-1]
		self.assertFalse(tester.numColumnsMatch())

		# Test for  when the last row is different from the rest
		string           = copy.copy(self.sample_string)
		tester           = Map(string, setUp=False)
		tester.convertToMap()
		tester.graph[-1] = tester.graph[0:-1]
		self.assertFalse(tester.numColumnsMatch())

	def test_topBottomRowsValid(self):
		# test both top and bottom valid
		tester            = Map(self.sample_string, setUp=False)
		result, num_goals = tester.topBottomRowsValid(0)
		self.assertTrue(result)
		self.assertEquals(num_goals, 0)

		# test top row invalid
		string             = copy.copy(self.sample_string)
		tester             = Map(string, setUp=False)
		tester.convertToMap()
		tester.graph[0][1] = 'a'
		result, num_goals  = tester.topBottomRowsValid(0)
		self.assertFalse(result)
		self.assertEquals(num_goals, 0)

		# test bottom row invalid
		string              = copy.copy(self.sample_string)
		tester              = Map(string, setUp=False)
		tester.convertToMap()
		tester.graph[-1][2] = 'a'
		result, num_goals   = tester.topBottomRowsValid(0)
		self.assertFalse(result)
		self.assertEquals(num_goals, 0)

		# test both top and bottom rows invalid
		string              = copy.copy(self.sample_string)
		tester              = Map(string, setUp=False)
		tester.convertToMap()
		tester.graph[0][1]  = 'a'
		tester.graph[-1][3] = 'a'
		result, num_goals   = tester.topBottomRowsValid(0)
		self.assertFalse(result)
		self.assertEquals(num_goals, 0)

	def test_midRowsValid(self):
		# test on invalid mid row
		mr     = MapReader()
		mr.load(files.bad_mid_row)
		
		with self.assertRaises(SyntaxError):
			tester = Map(mr)

	def test_playerFound(self):
		# test for example where player is in the map
		tester            = Map(self.sample_string, setUp=False)
		tester.convertToMap()
		self.assertTrue(tester.playerFound())

		# test on example where no player is in the map
		string = copy.copy(self.sample_string)
		string = string.replace(tester.player, '00')
		tester = Map(string, setUp=False)
		tester.convertToMap()
		self.assertFalse(tester.playerFound())

	def test_isValid(self):
		# test for valid string
		tester = Map(self.sample_string, setUp=False)
		tester.convertToMap()
		self.assertTrue(tester.isValid())

		# test for valid mapreader
		mr     = MapReader()
		mr.load(files.good)
		tester = Map(mr)
		self.assertTrue(tester.isValid())

		# test for invalid column count
		mr     = MapReader()
		mr.load(files.bad_col)
		
		with self.assertRaises(SyntaxError):
			tester = Map(mr)

		# test for empty map
		mr     = MapReader()
		mr.load(files.empty)
		
		with self.assertRaises(SyntaxError):
			tester = Map(mr)

		# test on there being no player
		mr     = MapReader()
		mr.load(files.no_player)
		
		with self.assertRaises(SyntaxError):
			tester = Map(mr)

		# test on a string being given
		mr     = MapReader()
		mr.load(files.sample)
		
		with self.assertRaises(SyntaxError):
			tester = Map(mr)

		# test fail on multiple goals
		mr     = MapReader()
		mr.load(files.multiple_goals)
		tester = Map(mr, setUp=False)	
		with self.assertRaises(SyntaxError):
			tester.setUp()

		# test fail on no goals
		mr     = MapReader()
		mr.load(files.no_goals)
		tester = Map(mr, setUp=False)
		with self.assertRaises(SyntaxError):
			tester.setUp()

		# test topBottomRowsValid invalid for isValid call
		mr     = MapReader()
		mr.load(files.bottom_row_bad)
		tester = Map(mr, setUp=False)
		with self.assertRaises(SyntaxError):
			tester.setUp()

		mr     = MapReader()
		mr.load(files.top_row_bad)
		tester = Map(mr, setUp=False)
		with self.assertRaises(SyntaxError):
			tester.setUp()

	def validate_move(self, move1, move2):
		self.assertEquals(move1.piece, move2.piece)
		self.assertEquals(move1.up,    move2.up)
		self.assertEquals(move1.right, move2.right)
		self.assertTrue(move1.isValid())

	def validate_moves(self, moves1, moves2):
		self.assertEquals(len(moves1), len(moves2))

		for i in range(len(moves1)):
			self.validate_move(moves1[i], moves2[i])

	def test_isValidMove(self):
		mr     = MapReader()
		mr.load(files.good)
		tester = Map(mr)

		# test on none Move object
		self.assertFalse(tester.isValidMove("not move"))

		# test when move isn't valid
		move = Move.right(')')
		move.up = 3
		self.assertFalse(tester.isValidMove(move))

		# test on invalid subtraction move
		move = Move.left('*', size=2)
		self.assertFalse(tester.isValidMove(move))

		# test on invalid addition move
		move = Move.left('a')
		self.assertFalse(tester.isValidMove(move))

		# test on valid addition move
		move = Move.right('9')
		self.assertTrue(tester.isValidMove(move))

		# test on valid subtraction move
		mr     = MapReader()
		mr.load(files.left)
		tester = Map(mr)
		move   = Move.left('*')
		self.assertTrue(tester.isValidMove(move))

		# make sure we can move to the goal as well
		move   = Move.right('*')
		self.assertTrue(tester.isValidMove(move))

	def test_makeConfidentMove(self):
		# test moving left
		mr     = MapReader()
		mr.load(files.left)
		tester = Map(mr)
		tester.makeConfidentMove(Move.left('*'))
		correct = [['|', '|','|', '|', '|', '|'], \
		           ['|', '0','*', '*', '0', '$'], \
		           ['|', '|','|', '|', '|', '|']]
		self.assertEquals(tester.graph, correct)

		# test moving right
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		tester.makeConfidentMove(Move.right('*'))
		correct = [['|', '|', '|', '|', '|'], \
		           ['|', '0', '*', '*', '$'], \
		           ['|', '|', '|', '|', '|']]
		self.assertEquals(tester.graph, correct)

		# test moving down
		mr     = MapReader()
		mr.load(files.down)
		tester = Map(mr)
		tester.makeConfidentMove(Move.down('1'))
		correct = [['|', '|', '|', '|', '|'], \
		           ['|', '*', '*', '0', '$'], \
		           ['|', '0', '0', '0', '|'], \
		           ['|', '1', '0', '0', '|'], \
		           ['|', '1', '0', '0', '|'], \
		           ['|', '1', '0', '0', '|'], \
		           ['|', '0', '0', '0', '|'], \
		           ['|', '|', '|', '|', '|']]
		self.assertEquals(tester.graph, correct)

		# test moving up
		mr     = MapReader()
		mr.load(files.up)
		tester = Map(mr)
		tester.makeConfidentMove(Move.up('1'))
		correct = [['|', '|', '|', '|', '|'], \
				   ['|', '*', '*', '0', '$'], \
				   ['|', '1', '0', '0', '|'], \
				   ['|', '1', '0', '0', '|'], \
				   ['|', '0', '0', '0', '|'], \
				   ['|', '|', '|', '|', '|']]
		self.assertEquals(tester.graph, correct)

	def test_makeMove(self):
		# test valid move type
		mr     = MapReader()
		mr.load(files.left)
		tester = Map(mr)
		with self.assertRaises(SyntaxError):
			tester.makeMove(None)

		# test valid move type
		tester.makeMove(Move.left('*'))
		correct = [['|', '|','|', '|', '|', '|'], \
		           ['|', '0','*', '*', '0', '$'], \
		           ['|', '|','|', '|', '|', '|']]
		self.assertEquals(tester.graph, correct)

		# test multi-move valid move type
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		with self.assertRaises(SyntaxError):
			tester.makeMove(None)

		# test moving right twice
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		tester.makeMove(Move.right('*',size=2))
		correct = [['|', '|', '|', '|', '|'], \
		           ['|', '0', '0', '*', '*'], \
		           ['|', '|', '|', '|', '|']]
		self.assertEquals(tester.graph, correct)

	def test_getMoves(self):
		# these tests also handle tests for addition and 
		# subtraction moves

		# test on map where only right move is possible
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		valid_moves = [Move.right('*'), Move.right('*', size=2)]
		found_moves = tester.getMoves()
		self.validate_moves(valid_moves, found_moves)

		# test on map where only left move is possible
		mr     = MapReader()
		mr.load(files.left)
		tester = Map(mr)
		valid_moves = [Move.left('*', size=1), Move.left('*', size=2), Move.right('*')]
		found_moves = tester.getMoves()
		self.validate_moves(valid_moves, found_moves)

		# test on map where only up move is possible
		mr     = MapReader()
		mr.load(files.up)
		tester = Map(mr)
		valid_moves = [Move.up('1'), Move.right('*'), Move.right('*', size=2)]
		found_moves = tester.getMoves()
		self.validate_moves(valid_moves, found_moves)

		# test on map where only down move is possible
		mr     = MapReader()
		mr.load(files.down)
		tester = Map(mr)
		valid_moves = [Move.down('1'), Move.down('1', size=2), Move.right('*'),  Move.right('*', size=2)]
		found_moves = tester.getMoves()
		self.validate_moves(valid_moves, found_moves)

		# test where no move is possible
		mr     = MapReader()
		mr.load(files.no_move)
		tester = Map(mr)
		valid_moves = []
		found_moves = tester.getMoves()
		self.validate_moves(valid_moves, found_moves)

		# test when the goal is on the left side
		mr     = MapReader()
		mr.load(files.left_goal)
		tester = Map(mr)
		valid_moves = [Move.left('*', size=1), Move.left('*', size=2), Move.left('*', size=3)]
		found_moves = tester.getMoves()
		self.validate_moves(valid_moves, found_moves)

	def test_isSolved(self):
		# test for solved example
		mr     = MapReader()
		mr.load(files.quick_solve)
		tester = Map(mr)
		tester.makeConfidentMove(Move.right('*'))
		self.assertTrue(tester.isSolved())

		# test for not solved example
		mr     = MapReader()
		mr.load(files.up)
		tester = Map(mr)
		tester.makeConfidentMove(Move.up('1'))
		self.assertFalse(tester.isSolved())

	def test_copy(self):
		# get a valid graph set up
		mr     = MapReader()
		mr.load(files.quick_solve)
		tester = Map(mr)
		
		# get a copy
		copy = tester.copy()

		# test if tester and copy references are different
		self.assertNotEqual(copy, tester)

		# test if the matrix references are different
		self.assertFalse(copy.graph is tester.graph)

		# test if the board elements are the same
		for y in range(len(copy.graph)):
			for x in range(len(copy.graph[y])):
				self.assertEquals(copy.graph[y][x], tester.graph[y][x])

		# test if hash is still the same
		self.assertTrue(copy.hash, tester.hash)

	def test_copyMove(self):
		# get a right graph and move right on it
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		old_hash = tester.hash
		copy = tester.copyMove(Move.right('*'))
		
		# get the graph that should result and test for equality
		mr     = MapReader()
		mr.load(files.left)
		tester = Map(mr)

		# test if tester and copy references are different
		self.assertNotEqual(copy, tester)

		# test if the matrix references are different
		self.assertFalse(copy.graph is tester.graph)

		# test if the board elements are the same
		good_map = "|||||\n|0**$\n|||||"
		self.assertEquals(copy.hash, good_map)

		# test if hash is same as the moved map
		self.assertTrue(copy.hash, tester.hash)

		# test if hash has been updated from the old one
		self.assertNotEqual(copy.hash, old_hash)

		# test if we move again to solve the puzzle
		copy = copy.copyMove(Move.right('*'))
		self.assertTrue(copy.isSolved())

	def test_copyConfidentMove(self):
		# get a right graph and move right on it
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		old_hash = tester.hash
		copy = tester.copyConfidentMove(Move.right('*'))
		good_map = "|||||\n|0**$\n|||||"
		self.assertEquals(copy.hash, good_map)

	def test_validSubractionMoves(self):
		# get a right graph and move right on it
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		self.assertEquals(len(tester.validSubtractionMoves(Move.right('*'))), 0)
		self.assertEquals(len(tester.validSubtractionMoves(Move.up('*'))), 0)

	def test_validAdditionMoves(self):
		# get a right graph and move right on it
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		self.assertEquals(len(tester.validAdditionMoves(Move.left('*'))), 0)
		self.assertEquals(len(tester.validAdditionMoves(Move.down('*'))), 0)


