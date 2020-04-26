source ./venv/Scripts/activate && pip freeze && python manage.py runserver

$ pip freeze `check which environment you are in`
$ source ./venv/Scripts/activate `do this if pip freeze tells you're not in the local environment`
$ pip freeze `check that you are now in the local environment. You should have Django and sqlparse amongst others installed`
$ python manage.py runserver `run server on port 8000`