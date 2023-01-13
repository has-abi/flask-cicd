# FLASK CI/CD

## Installation

First, you need to clone this repository:

```bash
$ git clone https://gitlab.com/has-abi/flask-cicd.git
```

Then change into the `flask-cicd` folder:

```bash
$ cd flask-cicd
```

Now install pipenv with pip

```bash
$ pip install pipenv
```

Now, we will need to create a virtual environment and install all the dependencies:

```bash
$ pipenv shell
$ pipenv install
```

## Runs

**Before run the application, make sure you have activated the virtual enviroment.**

Activate the virtual enviroment

```bash
$ pipenv shell
```

To start the application browse to project root where manage.py is

```bash
$ python3 manage.py run
```

### Run tests

```bash
$ python manage.py test
```

### Run tests with coverage

```bash
$ python manage.py cov
```

## Application menu

- GET (`/process?text=your_text`): Simple GET endpoint to process text.

