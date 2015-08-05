.PHONY: env clean

env: __

__:
	virtualenv __
	__/bin/pip install -r requirements.txt

clean:
	rm -Rf __
