## LAB - Class 34

#### Project: Django Backend Deployment 
#### Author: JJ Escandor

#### Description
 - This is project introduces Django Rest Framework, Docker, Postgresql, JWT

### To get tokens
 - source .venv/bin/activate
 - docker compose up -d
 - go to http://44.202.123.64/admin/ in the browser
 - admin username: code01 password: ASDFzxcv!@34 

### Features - Django
- Create a new public repo cookie-stand-api that uses API Quick Start as a template, or use one that you have created.
- Modify your application using instructions in README.md found in root of repo.
- Install from requirements.txt.
- Export (aka freeze) requirements.
- Change things app folder to be cookie_stands.
- Go through code base looking for Thing,thing and things change to cookie-stand related names.

### Features - AWS
- Deploy Docker container (Heroku, Azure, AWS, Digital Ocean, etc..)

### Storage Options - ElephantSQL
- Host your Database at ElephantSQL


### Tests
1. run docker compose run web python3 manage.py test
