# Notes
gunicorn: gunicorn my_project.wsgi is the command heroku will use to start the server. It works similarly to python3 manage.py runserver.

psycopg2: psycopg2 is a driver for interacting with PostgreSQL databases using Python. The dj-database-url Python package is a utility to connect Django to a database using a URL.

dj_database_url: The dj_database_url import is used to convert the database URL we copied from the ElephantSQL details tab into a format that Django can use to connect to an external database server.

SECRET_KEY: Another variable considered secret in Django is the SECRET_KEY in settings.py. This is a unique, secret, and random string that is used for cryptographic signing. That means that it ensures the integrity of the data stored in the cookies, forms, and much more, which is essential for the security of your Django application. This is the next thing we need to secure.

Slug: In publishing, a slug is a short name for an article that is still in production. It comes from the lead casts used in print typesetting. You can tell Django was created for the newspaper industry! In Django, the slug is what you'll use to build a URL for each of your posts.

model: So a model is a Python class that defines the structure of a database table. Within the class, we then define fields and their relationships
to fields in other tables.
Fields are the named places where we store single pieces of data, such as a person's
name, email address, or password.

 Django models documentation: https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types

 Views: https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/


 Design philosophies: https://docs.djangoproject.com/en/4.2/misc/design-philosophies/

 Cool URIs don't change: https://www.w3.org/Provider/Style/URI

Summernote Package: pip3 install django-summernote~=0.8.20.0, The ready-made SummernoteModelAdmin class defines the text editor, enabling you to access its functionality in the admin panel for your posts.

Fixtures: they help move data into databases. Think of a fixture as a file containing data tailored to your database. You can use it to save database contents or, as we'll see here, to fill a database for development. We'll work with a JSON fixture, but Django also supports XML and YAML. use python3 manage.py loaddata posts after adding posts.json data.You can now add blog/fixtures/ to the .gitignore file.
Note: You can keep the directory locally, as this technique will be helpful in the future if you run into database errors.


