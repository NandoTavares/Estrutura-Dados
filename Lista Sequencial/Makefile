PYTHON := python3
SRC := lista.py

run:
	$(PYTHON) $(SRC)

lint:
	flake8 $(SRC)

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

.PHONY: run lint clean
