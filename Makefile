freeze:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt

test: _rmpyc
	PYTHONPATH="$(shell pwd)/src" PYTHONDONTWRITEBYTECODE=1 pytest -s

_rmpyc:
	find . -type f -name '*.pyc' -delete
	find . -name __pycache__ -delete

.PHONY:		\
	freeze 	\
	install \
	test 	\
	_rmpyc