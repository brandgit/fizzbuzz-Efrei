.PHONY: docs

docs:
	mkdir -p docs
	sphinx-apidoc -o docs/ .
	sphinx-build -b html docs/ docs/_build/html