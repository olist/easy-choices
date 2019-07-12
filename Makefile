clean: clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr `find . -type d -name '*.egg-info'`

dev-requirements:
	pip install -e ".[dev]"

test:
	pytest -vvv

build: test
	python setup.py sdist
	python setup.py bdist_wheel

lint:
	pre-commit run -a -v
