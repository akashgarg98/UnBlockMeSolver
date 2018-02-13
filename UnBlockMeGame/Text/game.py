import time
import sys
import os

# curses.noecho(): disable keypresses showing up on screen
# curses.cbreak(): respond to keys instantly
# thank you to the awesome documentation at https://docs.python.org/2/howto/curses.html

try:
	import curses
except:
	print "ERROR: Your OS version of python2.7 does not support curses. Please use GUI version instead."
	sys.exit(1)

def game_loop():
	stdscr = curses.initscr()

	# sample window 
	begin_x = 20; begin_y = 7
	height = 5; width = 40
	win = curses.newwin(height, width, begin_y, begin_x)
	pad = curses.newpad(100, 100)
	#  These loops fill the pad with letters; this is
	# explained in the next section
	for y in range(0, 100):
	    for x in range(0, 100):
	        try:
	            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
	        except curses.error:
	            pass

	#  Displays a section of the pad in the middle of the screen
	pad.refresh(0,0, 5,5, 20,75)
	time.sleep(3.0)

	# end curses window
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()

def run():
	if curses != None:
		game_loop()