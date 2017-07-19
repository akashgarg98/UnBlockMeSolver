import math

def manhattan(x1, y1, x2, y2):
	# return 0
	return abs(x2 - x1) + abs(y2 - y1)

def euclidian(x1, y1, x2, y2):
	return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
