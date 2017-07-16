tests:
	# @python -m unittest discover -s test -p '*Tests.py' 
	@coverage run -m unittest discover -s test -p '*Tests.py'
	@coverage report

html_coverage:
	@make tests
	@coverage html
	@open htmlcov/index.html

document:
	@echo "Generating documentation in doc folder."
	@if [ -d doc ]; then rm -Rf doc; fi
	@epydoc -v -o doc --pdf --name "Epydoc" .

open_doc:
	@open doc/api.pdf

clean:
	$(shell find . -name "*.pyc" -exec rm -f {} \;)
	@echo "*.pyc files deleted."

lines:
	@find . -name '*.py' | xargs wc -l
	
help:
	@echo "    tests"
	@echo "        Run all unit tests."
	@echo "    html_coverage"
	@echo "        Open html documentation for the code coverage and run tests." 
	@echo "    document"
	@echo "        Create new set of documentation."
	@echo "    open_doc"
	@echo "        Open generated documentation."
	@echo "    clean"
	@echo "        Remove python pyc files."
	@echo "    lines"
	@echo "        Get the total number of lines of code in the project."