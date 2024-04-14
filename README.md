# Notes
gunicorn: gunicorn my_project.wsgi is the command heroku will use to start the server. It works similarly to python3 manage.py runserver.

psycopg2: psycopg2 is a driver for interacting with PostgreSQL databases using Python. The dj-database-url Python package is a utility to connect Django to a database using a URL.

dj_database_url: The dj_database_url import is used to convert the database URL we copied from the ElephantSQL details tab into a format that Django can use to connect to an external database server.

SECRET_KEY: Another variable considered secret in Django is the SECRET_KEY in settings.py. This is a unique, secret, and random string that is used for cryptographic signing. That means that it ensures the integrity of the data stored in the cookies, forms, and much more, which is essential for the security of your Django application. This is the next thing we need to secure.

Slug: In publishing, a slug is a short name for an article that is still in production. It comes from the lead casts used in print typesetting. You can tell Django was created for the newspaper industry! In Django, the slug is what you'll use to build a URL for each of your posts.