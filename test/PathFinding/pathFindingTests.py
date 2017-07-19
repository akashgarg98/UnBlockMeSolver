from PathFinder.PathFinder import PathFinder
from Map.MapReader import MapReader
from PathFinder.bfs import BFS
from PathFinder.AStar import AStar
from Map.Move import Move
from Map.Map import Map
from test import files
import unittest
import time


def testOptimalPath(self, solver):
	# test simple solve with one move
	mr     = MapReader()
	mr.load(files.quick_solve)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
	path = pf.getPath()
	self.solve(tester, path)
	self.assertTrue(tester.isSolved())
	self.assertEquals(len(path), 1)

	# test simple solve with two moves
	mr     = MapReader()
	mr.load(files.right)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
	path = pf.getPath()
	self.solve(tester, path)
	self.assertTrue(tester.isSolved())
	self.assertEquals(len(path), 1)

	# test simple solve with a few moves
	mr     = MapReader()
	mr.load(files.easy_solve)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
	path = pf.getPath()
	self.solve(tester, path)
	self.assertTrue(tester.isSolved())
	self.assertEquals(len(path), 3)

	# test complex map
	start = time.clock()
	mr     = MapReader()
	mr.load(files.simple_solve)
	tester = Map(mr)
	tester.setUp()
	pf  = solver(tester)
	path = pf.getPath()
	self.solve(tester, path)
	self.assertTrue(tester.isSolved())

	# AStar path will be 16, because the heuristic overestimates
	self.assertTrue(len(path) == 15 or len(path) == 16 or len(path) == 17)
	end = time.clock()
	print
	print solver, "time:", end - start

	# test handing a solved map to pathfinder
	pf  = solver(tester)
	self.assertEquals(pf.getPath(), None)

	# test impossible map
	mr     = MapReader()
	mr.load(files.impossible)
	tester = Map(mr)
	tester.setUp()
	pf = solver(tester)
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
	
	def test_bfs(self):
		testOptimalPath(self, BFS)

	def test_AStar(self):
		testOptimalPath(self, AStar)
		
