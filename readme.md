source ./venv/Scripts/activate && pip freeze && python manage.py runserver

## Step 1: Check Environment
$ pip freeze `check which environment you are in`

## Step 2: Do this if Pip Freeze tells you you're not in the local environment
$ source ./venv/Scripts/activate 

## Step 3: Confirm you're in local environment (You should have Django and sqlparse amonst others installed)
$ pip freeze 

## Step 4: Run Server on port 8000
$ python manage.py runserver
