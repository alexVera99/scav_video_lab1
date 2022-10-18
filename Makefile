lint:
	./venv/bin/python -m pylint src
	./venv/bin/python -m pydocstyle src
	./venv/bin/python -m pycodestyle --select E,W src
	./venv/bin/python -m mypy src