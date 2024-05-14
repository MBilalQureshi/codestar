# Notes
App creation : python3 manage.py startapp about
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


Prepare the project for multiple template directories: TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates'), Scroll down in the codestar/settings.py file to TEMPLATES and add your newly created TEMPLATES_DIR constant to the list of 'DIRS'.
'DIRS': [TEMPLATES_DIR], Add a new top-level templates directory, Add a new base.html file to your newly created top-level templates directory.
explanation:
Finding our templates
How does Django know where to find the templates?

That is controlled by the TEMPLATES setting in settings.py.
The DIRS key tells Django which directories to look in. This is a Python list, so we add the TEMPLATES_DIR variable, which was set at the top of settings.py.
The TEMPLATES setting also has APP_DIRS set to True, which means that Django will also look for a templates directory inside all our app directories.
Finally, in our project, we set TEMPLATES_DIR value to the templates directory in our base, or top-level directory.

--------
Whitenoise -> Deployment with static files: The deployed app will then look as nicely styled as the local development version. This package will allow your Heroku app to serve its own static files without relying on any external file hosting services like a content delivery network (CDN).

To do this, we will use a Python package named WhiteNoise. pip3 install whitenoise~=5.3.0, python3 manage.py collectstatic , python3 -V(check python version), add python version in runtime.txt file, use heroku link :https://devcenter.heroku.com/articles/python-support#specifying-a-python-version

Run the collectstatic command in the terminal to collect the static files into a staticfiles directory.
Note: The command has created a staticfiles directory that you can see in the left-hand explorer panel. We will explain this in detail in the next topic.
python3 manage.py collectstatic

Return to the Heroku dashboard, and click on the Settings tab and the Reveal config vars button. Remove the DISABLE_COLLECTSTATIC key/value pair.

Note: This environment variable prevented collectstatic from running on deploy up till now, but as static files are set up, we can remove this.
--------

As we added static default image, Collect the new static files to the staticfiles directory. Type yes when prompted to overwrite the existing files.

python3 manage.py collectstatic
Note: Only the one new image file in static was copied to staticfiles.

-------------
Filter : https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#ref-templates-builtins-filters

-------------
Django All auth https://docs.allauth.org/en/latest/installation/quickstart.html
AllAuth offers distinct advantages, such as sending password and account confirmation emails, enforcing password complexity and providing single sign-on using Google or Facebook.
pip3 install django-allauth~=0.57.0
pip3 freeze --local > requirements.txt
python3 manage.py migrate
From the terminal, check the location of your django-allauth package files on your computer. Copy the file path labelled Location:
You will need this in the next step.
pip3 show django-allauth
Copy the allauth template files to the projects templates directory using this terminal command where <Location> is the file path you copied in the previous step.
cp -r <Location>/allauth/templates/* ./templates/
Open the templates/accounts/logout.html file and replace the code with all the code in this file.
Note: You will update the signup template code in an upcoming topic.
https://github.com/Code-Institute-Solutions/blog/blob/main/11_authorisation/01_allauth/templates/account/login.html
https://github.com/Code-Institute-Solutions/blog/blob/main/11_authorisation/01_allauth/templates/account/logout.html
Source code
https://github.com/Code-Institute-Solutions/blog/tree/main/11_authorisation/01_allauth


pip3 show django-allauth, We use this command to find the package location, so we can copy the template files from it.

Crispy Forms
pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7
To write a comment, we will use a library
called Django Crispy Forms. You don’t need to use an external library in your projects, you
can create standard HTML forms if you wish. We’re using Crispy Forms for the following reasons:
It makes creating well-structured, nicely designed
forms easy with just a few lines of code. Secondly Crispy Forms integrates easily with
Bootstrap and adds the relevant classes for us. It also allows us to customise the structure
of our forms easily, which allows us to make complex, multi-column forms.

pip3 freeze --local > requirements.txt
'allauth.socialaccount',
'crispy_forms',
'crispy_bootstrap5',
'django_summernote',
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

------------------------------------------------------
Cloudinary to store user-uploaded media
pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15
pip3 freeze --local > requirements.txt
Click the provided link to sign up for Cloudinary.

Provide your name and email address and choose a password or sign in with a social account.
If asked, How would you best describe yourself? you can click on Developer.
Depending on your chosen sign-up method, you may have to respond to an email verification.

os.environ.setdefault(
    "CLOUDINARY_URL", "<URL copied from Cloudinary in last step>")

INSTALLED_APPS = [
    # …
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'django.contrib.sites',
    # …
    'django_summernote',
    'cloudinary',
    'blog',
    'about',
]
The main reason for adding 'cloudinary_storage' to the INSTALLED_APPS in Django's settings.py when setting up Cloudinary => 'cloudinary_storage' overrides Django's default media file storage so that we can use Cloudinary instead.


You may be wondering why we don’t just store user-uploaded media on Heroku along with the
staticfiles?
Why do we need a separate media hosting provider?
This is because Heroku has what’s known as an “ephemeral file system”.
When you create a Heroku app, it provides what's known as a dyno.
And this is effectively like a small container to run your project in.
A user-uploaded image is stored by the dyno within the project file structure.
However, when your project has been idle, and no one has accessed it for a while, then
the dyno stops to conserve resources.
When that happens, any files that have been uploaded since the project was created are
lost.
When the next user accesses the project only the image alt text is seen.
Therefore, we're going to upload media images to a persistent file store, which is where
Cloudinary comes in.
Now we could have chosen to use another provider, such as Microsoft Azure or Amazon S3, but
these are more complicated to set up.
For everything we want to do in this project, Cloudinary is a perfectly good solution.

STATIC AND CLOUDINARY MEDIA FILES:
But why do we make a distinction between static and media files?
You learned previously that static files are those that are unchanged during the application
execution.
Using staticfiles directories and whitenoise keeps these separate, making deployment, backups
and version control easier.
Media files, however, are unique to a user and may change frequently.
As a result, they are not collected or managed by Django, but Django will serve them from
a specified media URL.
In this case, the Cloudinary API will generate a URL for each image that the Django project
can use.
This is a separation of concerns.
Heroku hosts an application of a known size and doesn’t want an unknown quantity of
files to be uploaded to their servers.
Cloudinary, on the other hand, hosts media files but not running applications.
---------------------