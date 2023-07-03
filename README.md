# Temporary Name

Project carried out to put into practice the knowledge learned.

## Running locally

Clone the project

```bash
git clone  https://github.com/Peagah-Vieira/Django-Dashboard.git
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

Compile the Tailwind CSS

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Perform the migrations

```bash
py manage.py migrate
```

Start the server

```bash
py manage.py runserver
```
## Learnings

Good practice concepts:

(https://learndjango.com/tutorials/django-best-practices-projects-vs-apps).


Python requirements file:

(https://learnpython.com/blog/python-requirements-file/)

Test-Driven Development:

(https://www.browserstack.com/guide/what-is-test-driven-development)

## Documentation

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Tailwind + Flowbite](https://flowbite.com/docs/getting-started/django/)





