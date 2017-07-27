requirements:
	@pipreqs UnBlockMe --force

server:
	$(shell cd UnBlockMeServer; make server)

heroku:
	@heroku local web -p 8080

clean:
	$(shell find . -name "*.pyc" -exec rm -f {} \;)
	@echo "*.pyc files deleted."

lines:
	@find . -name '*.py' | xargs wc -l

help:
	@echo "    requirements"
	@echo "        Update requirements.txt with all of the required imports for Heroku."
	@echo "    server"
	@echo "        Start server. Source found in UnBlockMeServer. Port used is 8080 by default"
	@echo "    heroku"
	@echo "        Start server with heroku to replicate running on heroku server. Port used is 5000 by default."
	@echo "    clean"
	@echo "        Remove all pyc files."
	@echo "    lines"
	@echo "        Get the total number of lines of code in the project."