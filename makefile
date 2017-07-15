tests:
	$(shell python -m unittest discover -s test -p '*Tests.py')

document:
	@echo "Generating documentation in doc folder."
	@if [ -d doc ]; then rm -Rf doc; fi
	@epydoc -v -o doc --pdf --name "Epydoc" .

clean:
	$(shell find . -name "*.pyc" -exec rm -f {} \;)
	@echo "*.pyc files deleted."

help:
	@echo "    tests"
	@echo "        Run all unit tests."
	@echo "    document"
	@echo "        Create new set of documentation."
	@echo "    clean"
	@echo "        Remove python pyc files."