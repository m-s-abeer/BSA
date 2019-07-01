
 
Project Title: 
Blue Division Practice Automation



Introduction: 
Programming Practice Procedure that is currently in place in Daffodil International University is divided into three divisions based on the programming skill and level of programmer. 
The divisions are:
1.	Green Division
2.	Blue Division
3.	Red Division

We are emphasizing on the more intricate details of the Blue Division Practice where most of the guided programming practice happens and this division has the highest students now. 

Anyone who wants to join the Blue Division will have to pass the Green Division. They will get training classes taken by a selected Experienced Competitive Programmer having strong background and practice regularly on the Blue Division Practice Sheet. Anyone not maintaining the minimum requirement which is updated every week, will be removed from the sheet. Most of the Beginner and Intermediate level topics will be covered here.



Problem:
The coach uses Google sheet service to track the practice of the contestants. Tracking their progress and guiding them manually using a third party service like Google is not very efficient and as the population of blue division will grow in upcoming semesters. It will be a very difficult and tedious task for a coach to maintain everything manually. 

Solution: 
The solution of this problem is to stop using any third party service and automate the task of the practice sheet. By having a customized software for tracking practice, the coach can have more control and as the software will be automated, the coach can focus more on guiding the students more rather than maintaining the data.



Requirements:
We will require PYTHON language for this project. As this app should be accessible to everyone from everywhere. A web app for this scenario fits perfectly. We will use DJANGO Framework for this project which is based on Python. We will use POSTGRE Database Management System to store our data, its fast, secure and free DBMS. As this will be a web app, we will also need HTML, CSS, JAVASCRIPT. 
We will use tools like Text Editior, Bash/Shell, GitHub, 
We will need Domain and hosting server machine to up and run our project.
In summary:
% Technology: 
1.	Django Framework (for backend) 
2.	PostGre Database (for DBMS)
3.	HTML, CSS, JS (for frontend)

% Tools:
1.	Text Editor/IDE (Sublime, Atom, PyCharm)
2.	GitHub
3.	Anaconda (Python Environment) 
% System:
1.	Hosting Server
2.	Domain

Challenges:
The main challenge will be to release alpha within the short period of time. Maintaining ORM and the project structure is a challenge. Also bugs and slow system will cause hampering in the process of the project. But hopefully the Alpha will be released within time limit. 
To-Do list (Deadline):
1.	Learning technology and tools: Deadline 10th March
2.	Implementing ORM: 20th March
3.	Designing Front End: 30th March
4.	Dumping Database to PostGre: 1st April
5.	Testing/BugFixing: 7th April
6.	Releasing Alpha: 12th April


Future Scopes: 
If it gets successfully implemented and can replace the old tracking system of university, we will scale this project to work on national level. Also adding extra features like global ranking, real-time tracking, smart problem suggestions will be included. Gamifying the whole practice system like giving points and badges, and ways to spend these points will make the practicing more interesting to the contestants.
Conclusion:
This is a big project but if implemented successfully it will radically change the practice system of Daffodil International University. 
References:
Current Blue Division Practice sheets:-
Blue Division Fall, 2016 ( https://goo.gl/2HSLMC )
Blue Division Spring, 2017 ( https://goo.gl/kTqULd )
Blue Division, Summer 2017 ( https://goo.gl/9QPAiy )
Blue Division, Spring 2018 ( https://goo.gl/S1M6Sr )


# Blue Sheet Automation Project
## Installation instructions

### First of all, I suggest you to setup(optional) a virtual environment(to setup virtual environment you can use "Conda", Documentation="https://conda.io/docs/user-guide/tasks/manage-environments.html") and after activating your environment follow the below instructions:-


1.  install python 3.6.4 (through the environment or https://www.python.org/downloads/release/python-364/ if you haven't setup a custom environment)
2.  install django 2.0.2 (write 'pip install Django==2.0.2' in cmd)
3.  install django-bootstrap4 (write 'pip install django-bootstrap4' in cmd)
4.  install postgreSQL 10.x (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
5.  install psycopg2 (write 'pip install psycopg2' or 'pip install psycopg2-binary' if the first one doesn't work in cmd)
6.  change directory to the project folder (i.e. Blue/)
7.  create database (open pgmyAdmin 4 and create a new database with any name)
8.  connect database (open "Blue/Blue/settings.py" and change the 'Databases:name' and 'Databases:password' fields accordingly)
9.  makemigrations (write 'python manage.py makemigrations' in cmd)
10. migrate (write 'python manage.py migrate' in cmd)
11. createsuperuser (write 'python manage.py createsuperuser' in cmd and follow the instructions)
12. if everything goes fine, runserver (write 'python manage.py runserver')
13. open a web browser and hop on to the url (http://127.0.0.1:8000/)

**You can use either sqlite3 or postgreSQL. Both of the connections are available. So, you may skip over 4 and 5.**




