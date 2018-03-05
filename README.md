# Blue Sheet Automation Project

## first of all, I would suggest you to setup a virtual environment and then do the below instructions:-
## to setup virtual environment you can use "Conda"(Documentation="https://conda.io/docs/user-guide/tasks/manage-environments.html").

1.  install python 3.6.4 (https://www.python.org/downloads/release/python-364/)
2.  install django 2.0.2 (write 'pip install Django==2.0.2' in cmd)
3.  install django-bootstrap4 (write 'pip install django-bootstrap4' in cmd)
4.  install postgreSQL 10.x (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
5.  install psycopg2 (write 'pip install psycopg2' in command-prompt)
6.  change directory to the project folder (i.e. Blue/)
7.  create database (open pgmyAdmin 4 and create a new database with any name)
8.  connect database (open "Blue/Blue/settings.py" and change the 'Databases:name' and 'Databases:password' fields accordingly)
9.  makemigrations (write 'python manage.py makemigrations' in cmd)
10. migrate (write 'python manage.py migrate' in cmd)
11. createsuperuser (write 'python manage.py createsuperuser' in cmd and follow the instructions)
12. if everything goes fine, runserver (write 'python manage.py runserver')
13. open a web browser and hop on to the url (http://127.0.0.1:8000/)
