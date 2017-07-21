tests:
	@coverage run -m unittest discover -s test -p '*Tests.py'
	@coverage report

html_coverage:
	@if [ ! -d docs ]; then mkdir docs; fi
	@make tests
	@if [ -d docs/htmlcov ]; then rm -Rf docs/htmlcov; fi
	@coverage html
	@mv htmlcov docs/
	@open docs/htmlcov/index.html

document:
	@echo "Generating documentation in docs/documentation folder."
	@if [ ! -d docs ]; then mkdir docs; fi
	@if [ -d docs/documentation ]; then rm -Rf docs/documentation; fi
	@epydoc -v -o docs/documentation --pdf --name "Unblock Me Solver" .

open_doc:
	@open docs/documentation/api.pdf

clean:
	$(shell find . -name "*.pyc" -exec rm -f {} \;)
	@echo "*.pyc files deleted."

lines:
	@find . -name '*.py' | xargs wc -l
	
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
