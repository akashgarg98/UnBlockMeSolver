lines:
	@find . -name '*.py' | xargs wc -l

help:
	@echo "    lines"
	@echo "        Get the total number of lines of code in the project."