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

lint:
	pre-commit run -a -v

test:
	pytest -vvv

build: test
	python setup.py sdist
	python setup.py bdist_wheel

install-tools-for-release:
	pip install --upgrade setuptools wheel twine

test-release-package: clean install-tools-for-release build
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release-tag: clean
	git tag `python setup.py --version`
	git push origin `python setup.py --version`

release-package: clean install-tools-for-release build
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
