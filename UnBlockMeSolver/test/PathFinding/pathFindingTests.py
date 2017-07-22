from PathFinder.PathFinder import PathFinder
from Map.MapReader import MapReader
from PathFinder.Heuristics import *
from PathFinder.AStar import AStar
from PathFinder.bfs import BFS
from PathFinder.dfs import DFS
from Map.Move import Move
from Map.Map import Map
from test import files
import unittest
import time


def testPaths(self, solver, checkLength=True):
	# test simple solve with one move
	mr     = MapReader()
	mr.load(files.quick_solve)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
	
	path = None
	if solver == AStar:
		path = pf.getPath(self.heuristic)
	else:
		path = pf.getPath()

	self.solve(tester, path)
	self.assertTrue(tester.isSolved())
	if checkLength:
		self.assertEquals(len(path), 1)
	else:
		print len(path)

	# test simple solve with two moves
	mr     = MapReader()
	mr.load(files.right)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
	
	path = None
	if solver == AStar:
		path = pf.getPath(self.heuristic)
	else:
		path = pf.getPath()

	self.solve(tester, path)
	self.assertTrue(tester.isSolved())
	if checkLength:
		self.assertEquals(len(path), 1)

	# test simple solve with a few moves
	mr     = MapReader()
	mr.load(files.easy_solve)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
	
	path = None
	if solver == AStar:
		path = pf.getPath(self.heuristic)
	else:
		path = pf.getPath()

	self.solve(tester, path)
	self.assertTrue(tester.isSolved())
	if checkLength:
		self.assertEquals(len(path), 3)

	# test complex map
	start = time.clock()
	mr     = MapReader()
	mr.load(files.simple_solve)
	tester = Map(mr)
	tester.setUp()
	pf  = solver(tester)
	
	path = None
	if solver == AStar:
		path = pf.getPath(self.heuristic)
	else:
		path = pf.getPath()

	self.solve(tester, path)
	self.assertTrue(tester.isSolved())

	# AStar path will be 16, because the heuristic overestimates
	if checkLength:
		self.assertTrue(len(path) == 15 or len(path) == 16 or len(path) == 17)

	end = time.clock()
	print
	print solver, "time:", end - start

	# test handing a solved map to pathfinder
	pf  = solver(tester)

	path = None
	if solver == AStar:
		self.assertEquals(pf.getPath(self.heuristic), None)
	else:
		self.assertEquals(pf.getPath(), None)

	# test impossible map
	mr     = MapReader()
	mr.load(files.impossible)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
	
	path = None
	if solver == AStar:
		path = pf.getPath(self.heuristic)
	else:
		path = pf.getPath()

	self.assertEquals(path, None)

class PathFindingTest(unittest.TestCase):

	def solve(self, board, moves):
		for move in moves:
			board.makeConfidentMove(move)

	def test_pathFinder(self):
		pf = PathFinder(None)

		with self.assertRaises(NotImplementedError):
			pf.getPath()
	
	def test_dfs(self):
		testPaths(self, DFS, checkLength=False)

	def test_bfs(self):
		testPaths(self, BFS)

	def heuristic(self, board):
		"""
		Calculate heuristic cost for the given board.

		@type board:  Map
		@param board: Board being analyzed
		@rtype:       number
		@return:      Heuristic cost
		"""
		# position of player has to be adjusted based on where the player is
		return manhattan(board.pieces[board.playerPiece].x, board.pieces[board.playerPiece].y, \
			             board.pieces[board.goal].x,        board.pieces[board.goal].y)

	def test_AStar(self):
		testPaths(self, AStar)

		# test giving a non callable function
		mr     = MapReader()
		mr.load(files.quick_solve)
		tester = Map(mr)
		tester.setUp()
		pf = AStar(tester)

		path = pf.getPath(None)
		self.assertEquals(path, None)

		path = pf.getPath('None')
		self.assertEquals(path, None)

		path = pf.getPath(1)
		self.assertEquals(path, None)


