tests:
	$(shell python -m unittest discover -s test/* -p '*.py')

doc:
	@echo "Generating documentation in doc folder."
	$(shell epydoc -v -o doc --pdf --name "Epydoc" .)

clean:
	$(shell find . -name "*.pyc" -exec rm -f {} \;)
	@echo "*.pyc files deleted."

help:
	@echo "    unit_test"
	@echo "        Run all unit tests."
	@echo "    clean"
	@echo "        Remove python pyc files."