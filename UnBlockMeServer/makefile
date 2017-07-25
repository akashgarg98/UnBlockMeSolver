server:
	@python server.py

kill_server:
	@ps -f | grep server.py | sed -n 1p | awk '{print $2}' | xargs kill -9

tests:
	@echo "If tests fail, run 'make kill_server'"
	@make server & 
	@python serverTest.py
	make kill_server

help:
	@echo "    server"
	@echo "        Start UnBlockMe server for remote way to solve puzzles."
	@echo "    kill_server"
	@echo "        Find and kill process that is running the server."
	@echo "    tests"
	@echo "        Run unit tests for the server. Note: on fail, call 'make kill_server'."