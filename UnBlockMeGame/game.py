from Text import game as TextGame
from GUI import game as GUIGame
import argparse

def register_sys_args():
	'''
	Generate system argument parser and return results
	
	@rtype:  argparse.Namespace
	@return: parsed command line arguments
	'''
	parser = argparse.ArgumentParser(description='UnBlockMe: The Python Game')

	parser.add_argument('--gui', help='run game as GUI version rather than text', action='store_true')
	args = parser.parse_args()

	return args
def main():
	args = register_sys_args()
	
	if args.gui:
		GUIGame.run()
	else:
		TextGame.run()

if __name__ == '__main__':
	main()