.PHONY: env clean prep

prep: db.sqlite3

env: __

__:
	virtualenv __
	__/bin/pip install -r requirements.txt

clean:
	rm -Rf __ db.sqlite3

db.sqlite3: env
	./manage.py migrate
