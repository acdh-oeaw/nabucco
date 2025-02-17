[![flake8 Lint](https://github.com/acdh-oeaw/nabucco/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/nabucco/actions/workflows/lint.yml) [![Build and push to DockerHub](https://github.com/acdh-oeaw/nabucco/actions/workflows/build.yml/badge.svg)](https://github.com/acdh-oeaw/nabucco/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/nabucco/branch/master/graph/badge.svg?token=K3J7L8V6WB)](https://codecov.io/gh/acdh-oeaw/nabucco)

# nabucco
* repo to process nabucco xml-data (taken from [orig-repo](https://github.com/DigitalPasts/nabucco/tree/master/nabucco-xml)) into something more usabel (csv); be aware, to ease the parsing, I manually removed the namespaces from the original files
* evolved to application repo for generic nabucco app

## install

* clone the repo `git clone https://github.com/acdh-oeaw/nabucco.git`
* change into repo-folder `cd nabucco`
* create a virtualenv, e.g. `python -m venv venv` and activate it `source venv/bin/activate`
* install required packages `pip install -r requirements.txt`
* create a postgres-db `nabucco` with user and pw `postgres` - or modify `settings.py` or set propper environment variables
    --> note that with Windows, PostgreSQL13 seems not to work: use version 12
* run `python manage.py makemigrations` then `python manage.py migrate` and  `python manage.py runserver` to migrate database and start the dev server

> [!IMPORTANT]  
> The instructions of how to import data have been removed because the data as well as the related code are no longer part of this code base. The data import routine was only needed in the early stages of the application development.  

## Docker

### building the image

* `docker build -t nabucco:latest .`
* `docker build -t nabucco:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see `nabucco/settings.py` for possible varibles:

`docker run -it --network="host" --rm --env-file .env nabucco:latest`