# Django Polls Application

## About

The Django sample polls application, from [Writing your first Django app](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) for Django version 2.2.

## Getting Started

Create a Python 3 virtual environment, and activate it.

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Install requirements.
```bash
(env)$ python -m pip install -r requirements.txt
```

Run migrations, and load initial data from fixtures.

```bash
(env)$ python manage.py migrate
(env)$ python manage.py loaddata polls/fixtures/initial_data.json
```

**Note: the admin username is admin, password is admin@example.com**

## Configuration

Settings are automatically picked up from a `.env` file in the root directory if one is present.

Otherwise, the `DATABASE_URL` environment variable will be used to configure the database to connect to.