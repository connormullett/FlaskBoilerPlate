
# FlaskIT
A Flask API starter template to make a Flask web API *FAST*. If you are using this,  
you are expected to have knowledge of Flask

# What this template comes with
This template is designed for getting started with building API's fast with Flask. 
It gives a boilerplate template that can be used to build RESTful services.  
- User Authentication
- Database Models with Flask-SQLAlchemy 
- Example Blueprint view to get started
- Easy database migrations with Flask-Script and Flask-Migrate

# Necessary Steps
In order to run the app you need a couple of things. One, you need the proper  
environment variables

linux/mac  
`export FLASK_ENV=development`  

windows  
`$env:FLASK_ENV="development"`  

This sets the configuration for the app object. Your two options for `FLASK_ENV` are  
`development` and `production`

The jwt (Json Web Token) secret key is used in user authentication. If you opted out  
of user auth in the CLI, you don't need to worry about the next command 

linux/mac  
`export JWT_SECRET_KEY={your secret key here}`  
windows  
`$env:JWT_SECRET_KEY="{your secret key here}"`  

The database URI is the connection string to your database. If you plan on using  
a database, you need the following command. If you opted out of using a DB, you can  
skip the next command

linux/mac  
`export DATABASE_URL={your database URI here}`  
windows  
`$env:DATABASE_URL="{your database URI here}"`  


# Running the App
Running the app is as simple as `python app.py`  

# Migrations
To perform first time migrations, you need to import the modules that hold you  
models into `manage.py`, then run the following command  

`python manage.py db init`  

This will create a migrations folder in your projects root directory. This only needs  
to be done once. Every other time use the following commands  

`python manage.py db migrate`  

This will create the migrations based on Schema changes in your models. If you don't  
import the modules that hold your Schemas/Models, this won't do anything  

`python manage.py db upgrade`  

Upgrade changes and persist them to the DB

