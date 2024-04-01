# Blog_App

Follow these commands to run this project:

```bash
git clone https://github.com/Mahadi-Public/Blog_App.git
or using SSH
git clone git@github.com:Mahadi-Public/Blog_App.git
```

create a virtual environment using these commands:

```bash
python -m venv env or python3 -m venv env

to activate the environment, use these commands:

on Ubuntu: source env/bin/activate or
on Windows: env\Scripts\activate

To deactivate, use this command: deactivate
```

```bash
use this command to install dependencies: pip install -r requirements.txt
```

create .env file in the root of the project.
add the contents of using .env.example to COPY, .


```bash
the PASTE .env file this content  this contents are required

DEBUG=True
SECRET_KEY='dfsvdfsvdfvdf'

EMAIL_HOST_USER= PASTE HOST NAME
EMAIL_HOST_PASSWORD=PASTE PASSWORD

```


```bash
to Add user host and passwords

Go to Google Accounts => Security => 2-Step-Verification = > enter your gmail passwords => App passwords => Enter app name => create
```


```bash
Use these commands to python manage.py migrate
and create a superuser using this command: python manage.py createsuperuser
now run the server using this command: python manage.py runserver
```








