setup:
	python -m venv venv
	source myvenv/bin/activate
	pip install -r requirements.txt

deploy-local:
	flask run