unittest:
	sdasda
doctest:
	python3 -m doctest -v TestTask/GeometryCalc.py
lint:
	poetry run flake8 --exclude=.venv/
shell:
	poetry shell
