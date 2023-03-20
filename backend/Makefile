run: 
	python3 providers/manage.py runserver

make: 
	python3 provider/manage.py makemigrations 

migrate: 
	python3 migrate 

setup: 
	python3 -m venv venv 
	python3 pip install -r requirement.txt 

fastapi: 
	python3 api/main.py 

venv: 
	source venv/bin/activate

bot: 
	python3 providers/bot.py 