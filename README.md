# pictures_API

## Endpoints


## Technologies
Project is created with:
* Python 3.6
* Django 
* Django Rest Framework

For further details see `requirements.txt`

## Setup
To run the project locally:
* clone the repository locally
* create virtual environment using Python 3.6.9
* install `requirements.txt`
* replace placeholders in `pictures/example_settings.py` using your own creditentials
  * if you want to use sqlite3 database, comment DATABASES dictionnary
* rename `pictures/example_settings.py` to `pictures/local_settings.py` 
* run `python manage.py migrate`
* run `python manage.py make_plans` to create default plans
* if you want to create fake users to test the project, run `python manage.py fake_users`. Users names and passwords will display in terminal.
* run `python manage.py createsuperuser` to access Django admin endpoint
* run `python manage.py runserver`
