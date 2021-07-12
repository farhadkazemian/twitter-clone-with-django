# twitter-clone-with-django
![twitter clone with django](https://raw.githubusercontent.com/farhadkazemian/twitter-clone-with-django/master/accounts/static/logo.jpg)
## Setup:
```
python manage.py makemigrations accounts
python manage.py makemigrations posts
python manage.py migrate
python manage.py loaddata initial_interests_data.json 
python manage.py runserver
```
## Requirements:
- Python==3.9
- Django==3.1.7
