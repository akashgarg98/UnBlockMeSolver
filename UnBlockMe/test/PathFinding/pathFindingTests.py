from PathFinder.PathFinder import PathFinder
from PathFinder.TreeSearch import TreeSearch
from Map.MapReader import MapReader
from PathFinder.AStar import AStar
from Map.Move import Move
from Map.Map import Map
from test import files
import unittest
import time


def testPaths(self, solver, isBFS=False, checkLength=True):
	# test simple solve with one move
	mr     = MapReader()
	mr.load(files.quick_solve)
	tester = Map(mr)
	pf = None 

	# set path finder (BFS and DFS have different initializations)
	if solver == AStar:
		pf = solver(tester)
	else:
		pf = solver(tester, bfs=isBFS)
	
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
	pf.board = tester
	
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
	pf.board = tester
	
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
	pf.board = tester
	
	path = None
	if solver == AStar:
		path = pf.getPath(self.heuristic)
	else:
		path = pf.getPath()

	self.solve(tester, path)
	self.assertTrue(tester.isSolved())

	if checkLength:
		self.assertEquals(len(path), 15)

	end = time.clock()
	print
	print solver, "time ", isBFS, ":", end - start

	# test handing a solved map to pathfinder
	pf.board = tester

	path = None
	if solver == AStar:
		self.assertEquals(pf.getPath(self.heuristic), None)
	else:
		self.assertEquals(pf.getPath(), None)

	# test impossible map
	mr     = MapReader()
	mr.load(files.impossible)
	tester = Map(mr)
	pf.board = tester
	
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
		testPaths(self, TreeSearch, isBFS=False, checkLength=False)

	def test_bfs(self):
		testPaths(self, TreeSearch, isBFS=True)

	def heuristic(self, board):
		return 0

	def test_AStar(self):
		testPaths(self, AStar)

		# test giving a non callable function
		mr     = MapReader()
		mr.load(files.quick_solve)
		tester = Map(mr)
		pf = AStar(tester)

		path = pf.getPath(None)
		self.assertEquals(path, None)

		path = pf.getPath('None')
		self.assertEquals(path, None)

		path = pf.getPath(1)
		self.assertEquals(path, None)


