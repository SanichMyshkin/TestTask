unittest:
	python3 -m unittest test/test_GeometryCalc.py
doctest:
	python3 -m doctest -v TestTask/GeometryCalc.py
lint:
	poetry run flake8 --exclude=.venv/
shell:
	poetry shell
