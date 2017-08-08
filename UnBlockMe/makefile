OS := $(shell uname)

ifeq ($(OS),Linux)
	open_cmd = xdg-open
else
	open_cmd = open
endif

tests:
	@coverage run -m unittest discover -s test -p '*Tests.py'
	@coverage report

html_coverage:
	@if [ ! -d docs ]; then mkdir docs; fi
	@make tests
	@if [ -d docs/htmlcov ]; then rm -Rf docs/htmlcov; fi
	@coverage html
	@mv htmlcov docs/
	@$(open_cmd) docs/htmlcov/index.html

document:
	@echo "Generating documentation in docs/documentation folder."
	@if [ ! -d docs ]; then mkdir docs; fi
	@if [ -d docs/documentation ]; then rm -Rf docs/documentation; fi
	@epydoc -v -o docs/documentation --html --name "Unblock Me Solver" --exclude="test" .

open_doc:
	@$(open_cmd) docs/documentation/UnBlockMe-module.html

clean:
	$(shell find . -name "*.pyc" -exec rm -f {} \;)
	@echo "*.pyc files deleted."
	
help:
	@echo "    tests"
	@echo "        Run all unit tests."
	@echo "    html_coverage"
	@echo "        Run tests and open html documentation for code coverage." 
	@echo "    document"
	@echo "        Create new set of documentation."
	@echo "    open_doc"
	@echo "        Open generated documentation."
	@echo "    clean"
	@echo "        Remove python pyc files."
	@echo "    lines"
	@echo "        Get the total number of lines of code in the project."