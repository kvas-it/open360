.PHONY: env

env: __

__:
	virtualenv __
	__/bin/pip install -r requirements.txt
