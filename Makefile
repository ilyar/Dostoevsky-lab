venv:
	python3 -m venv venv
	. venv/bin/activate; if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

freeze: venv
	. venv/bin/activate; pip freeze > requirements.txt

test:\
src/app

clean:
	rm -rf venv

src/%: venv
	. venv/bin/activate; python src/$*.py

app: src/app
