## Woofer

A sample database is provided. If you want to start with a blank one simply
delete the db.sqlite3 file.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT

## Depedencies

SQLlite 3
Django 1.9
Python 2.7

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

The rest of this project docmentation can be found on google docs.

## Contributors

Max Llewellyn
Alex Arsenault
Cole Sullivan
Nick Richards

## Coding Standard

Our project conforms to the PEP8 coding standard with some exceptions.
To check the status of the code run the lint.sh script in the same directory
as the pylintrc file.