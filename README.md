# Python Projects

Python and Django projects built while learning to code.

## Projects

**Python - Part 1**
Core Python practice: functions, lists, inheritance and polymorphism, file handling, SQLite databases, a Tkinter student tracker and a text adventure game.

**DjangoUniversity**
A Django project with two apps, `classApp` (university classes) and `campusApp` (campuses), managed through Django Admin.

**Django Checkbook (BlueBird Banking)**
A Django app for tracking bank accounts. Create an account, add deposits and withdrawals, and see the current balance with a running-balance transaction list.

## Running a Django project

```
python -m venv venv
venv\Scripts\activate
python -m pip install django
cd <folder containing manage.py>
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser. For the admin site at `/admin/`, first run `python manage.py createsuperuser`.

## Running a Part 1 script

```
python script_name.py
```

## Author

Piyush Kumar Vekariya
