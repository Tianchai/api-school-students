# API School-Student application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Tianchai/api-school-students.git
$ cd api-school-students
```

Install `pipenv` and activate it:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
(api-school-students)$ pipenv install
```
Note the `(api-school-students)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv`.

Once finished downloading the dependencies:
```sh
(api-school-students)$ python manage.py makemigrations
(api-school-students)$ python manage.py migrate
(api-school-students)$ python manage.py runserver
```
And navigate to `http://localhost:8000/`.

`SQLite` is used by default. In order to use `PostgreSQL`, change the database in `config/settings/local.py`.
