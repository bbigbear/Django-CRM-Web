[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Peagah-Vieira/Django-CRM/blob/main/README_BR.md)
[![Python 3.11](https://img.shields.io/badge/python-3.11-yellow.svg)](https://www.python.org/downloads/release/python-360/)
![Django 4.2](https://img.shields.io/badge/Django-4.2-green.svg)
# Django Customer Relationship Management

A customer relationship management web application built using Django and Tailwind. 

[Django-CRM-API](https://github.com/Peagah-Vieira/Django-CRM-API)

## Functionalities

- Custom login and register authentication
- Password reset with email 
- Dashboard with navbar and sidebar
- Custom tables
- Custom pagination
- Custom search
- Custom empty state
- Custom Django-Admin
- Excel export
- Flash messages
- Tailwind CSS
- Light and dark theme
- Responsive
- Unit testing, integration testing and functional testing(Selenium)
- Create, read, update, delete(CRUD)

## Screenshots

<details>
  <summary>Register and login</summary>

  ![Register_Login](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/d81ff8de-c579-4546-889b-d5b63afec74d)

</details>

<details>
  <summary>Create</summary>

  ![Create](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/6b9a2a65-4046-4dde-9734-079c536675b1)

</details>

<details>
  <summary>Update</summary>

  ![Update](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/03135f00-a153-45de-8f2d-40541bd2372b)

</details>

<details>
  <summary>Delete confirmation</summary>

  ![Delete](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/5406f43a-888c-4a9a-90ca-bd53eda2c632)

</details>

<details>
  <summary>Custom pagination</summary>

  ![Pagination](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/a832c505-0748-409d-8d41-ad810542d55f)

</details>

<details>
  <summary>Dark and light theme</summary>

  ![Theme_Switch](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/263b1a74-1293-4249-a97a-6b3a106ac56d)

</details>

<details>
  <summary>Search and empty state</summary>

  ![Search_Empty_State](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/63e186ff-de33-4597-8eac-6bb500ba506a)

</details>

<details>
  <summary>Excel Export</summary>

  ![Export](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/d3a645d4-493a-4981-a5b3-db82667f9a68)

</details>

<details>
  <summary>Responsive</summary>

  ![Responsive](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/3ea69c94-75a5-4f8e-a916-3487b101a0e1)

</details>

<details>
  <summary>Django Custom Admin</summary>

  ![Django-Admin](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/944a29ab-8c9e-4f3e-b31b-b259cc772046)

</details>

## Running locally

Clone the project

```bash
git clone https://github.com/bbigbear/Django-CRM-Web.git
```

Create a virtual environment

```bash
# Linux
sudo apt-get install python3-venv    
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```

Update the pip

```bash
py -m pip install --upgrade pip
```

Install the dependencies

```bash
pip install -r requirements.txt
npm install
```

Copy the example env file and make the required configuration changes in the .env file

```bash
cp .env-example .env
```

Configure settings.py

```bash
# Local Configuration
DATABASES = {
  'default': {
      'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
      'NAME': os.getenv('POSTGRES_DB', BASE_DIR / './db.sqlite3'),
      'USER': os.getenv('POSTGRES_USER', ''),
      'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
      'HOST': os.getenv('POSTGRES_HOST', ''),
      'PORT': os.getenv('POSTGRES_PORT', ''),
  }
}

# Deploy - Render Configuration
# DATABASE_URL = os.getenv('DATABASE_URL')
# DATABASES = {
#    'default': dj_database_url.config(),
# }
```

Compile the Tailwind CSS

```bash
npm run build 
```

Perform the migrations

```bash
py manage.py migrate
```

Seed leads app

```bash
py manage.py seed leads --number=50
```

Start the server

```bash
py manage.py runserver
```

## Running the tests

To run the tests, run the following command

```bash
coverage run -m pytest 
```

Test percentage table (htmlcov/index.html)

```bash
coverage html
```

## Learnings

Good practice concepts:

(https://learndjango.com/tutorials/django-best-practices-projects-vs-apps).

Python requirements file:

(https://learnpython.com/blog/python-requirements-file/)

Write and run tests:

(https://docs.djangoproject.com/en/4.2/topics/testing/overview/)

Test-Driven Development:

(https://www.browserstack.com/guide/what-is-test-driven-development)

Selenium:

(https://django-selenium.readthedocs.io/en/latest/)

Class Based Views:

(https://docs.djangoproject.com/en/4.2/topics/class-based-views/)

PostgreSQL - Naming Conventions:

(https://www.geeksforgeeks.org/postgresql-naming-conventions/)

## Documentation

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Tailwind + Flowbite](https://flowbite.com/docs/getting-started/django/)

[Django Custom Taiwind](https://github.com/Aleksi44/django-admin-tailwind)
