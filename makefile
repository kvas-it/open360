.PHONY: env clean db run

PIP=__/bin/pip
PYTHON=__/bin/python

db: db.sqlite3

env: __

__:
	virtualenv __
	${PIP} install -r requirements.txt

clean:
	rm -Rf __ db.sqlite3

db.sqlite3: __
	${PYTHON} manage.py migrate

run: db.sqlite3
	${PYTHON} manage.py runserver
