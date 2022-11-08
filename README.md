# sh_model
A Django implementation of a socio-hydrological model for smallholder farmers in Maharashtra, India.

---

## Table of Contents
- [Intro](#intro)
- [Project Layout](#project-layout)
  - [Project config](#project-config)
  - [App config](#app-config)
  - [Requirements](#requirements)
  - [Django config](#django-config)
  - [AWS config](#aws-config)
- [Database diagram](#database-diagram)
- [Application launched](#application-launched)
- [References](#references)

## Intro
This repository contains a basic Django implementation into an Elastic Beanstalk AWS instance. The main goal of this project is to show database management under an OOP approach by using the framework's tools: urls, forms, models, and views. The code is mainly written in python, but the content is displayed using HTML5 and CC3.

This example uses two models: Farmer and Parcel. The instances' attributes are based on the state variables of the socio-hydrological dynamic system exposed in [1] While the instance's values are randomly set up.

## Project Layout

Here is the project layout:
```
.
├── .ebextensions
│   └── django.config
├── .elasticbeanstalk
│   └── config.yml
├── .gitignore
├── manage.py
├── model_mgmt
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── model_mgmt
│   │       ├── add_farmer.html
│   │       ├── add_parcel.html
│   │       ├── edit_farmer.html
│   │       ├── edit_parcel.html
│   │       ├── farmers.html
│   │       ├── home.html
│   │       ├── layout.html
│   │       └── parcels.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── shm_prj
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── settings.cpython-38.pyc
    │   ├── urls.cpython-38.pyc
    │   └── wsgi.cpython-38.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### Project config

Directory shm_pjr contains the configuration of the project. Please, pay attention to line 28 of file shm_prj/settings.py, where it's indicated the domain host.

```
ALLOWED_HOSTS = ['shm-env.eba-drfyvdui.us-west-2.elasticbeanstalk.com']
```

Also, it's important to indicated configuration of the database engine:

```
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ebdb',
            'USER': 'superuser',
            'PASSWORD': '****',
            'HOST': '****.****.us-west-2.rds.amazonaws.com',
            'PORT': '5432',
        }
    }
```

### App config

The app's settings are included in the directory model_mgmt. There are written two models: Farmers and Parcels; which inherit from the class Models.

### Requirements

File requirements.txt contains the freeze of pip. This is used by Elastic Beanstalk to set the environment up. 

```
asgiref==3.2.10
Django==3.1
psycopg2-binary==2.9.5
pytz==2022.6
sqlparse==0.4.3
```

it's important to remark on the python version because eb-aws instances support 3.7 or 3.8. For this case:

```
$ python --version
Python 3.8.15
```

### Django config

File .ebextensions/django.config contains both: settings to launch the ec2 instance in AWS; and, sh commands to be executed in every deployment, in order to migrate the database.

### AWS config

I used the EB-AWS client to initialize, create and deploy the application from the bash. It's important to indicate the python version at the moment of initialising the instance.

```
$ eb init -p python-3.8 app_name
$ eb create env_name
```

The identifiers app_name and env_name are used in the AWS console.

## Database diagram

Class Parcel has an aggregation relationship with respect to class Farmer, with a cardinality of one to many. It means that a Farmer can have several Parcels, but a parcel can have just one Farmer. 

![db_diagram](https://user-images.githubusercontent.com/8535984/200481823-2aa2663d-0b57-46e0-a666-dba05e43ae6f.png)

## Application launched

![app_screenshot](https://user-images.githubusercontent.com/8535984/200483155-ff81df12-534c-4b70-8f17-bd746e536a39.png)

Let's see the application already launched at:

http://shm-env.eba-drfyvdui.us-west-2.elasticbeanstalk.com/

## References

- [1]Pande, S., and Savenije, H. H. G. (2016), A sociohydrological model for smallholder farmers in Maharashtra, India, Water Resour. Res., 52, 1923– 1947, doi:10.1002/2015WR017841.

