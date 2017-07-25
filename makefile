server:
	$(shell cd UnBlockMeServer; make server)
	# @make server

clean:
	$(shell find . -name "*.pyc" -exec rm -f {} \;)
	@echo "*.pyc files deleted."

lines:
	@find . -name '*.py' | xargs wc -l

help:
	@echo "    clean"
	@echo "        Remove all pyc files."
	@echo "    lines"
	@echo "        Get the total number of lines of code in the project."