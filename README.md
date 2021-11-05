[![flake8 Lint](https://github.com/acdh-oeaw/nabucco/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/nabucco/actions/workflows/lint.yml) [![Build and push to DockerHub](https://github.com/acdh-oeaw/nabucco/actions/workflows/build.yml/badge.svg)](https://github.com/acdh-oeaw/nabucco/actions/workflows/build.yml)

# nabucco
* repo to process nabucco xml-data (taken from [orig-repo](https://github.com/DigitalPasts/nabucco/tree/master/nabucco-xml)) into something more usabel (csv); be aware, to ease the parsing, I manually removed the namespaces from the original files
* evolved to application repo for generic nabucco app

## install

* clone the repo `git clone https://github.com/acdh-oeaw/nabucco.git`
* change into repo-folder `cd nabucco`
* create a virtualenv, e.g. `virtualenv env` and activate it `source env/bin/activate`
* install required packages `pip install -r requirements.txt`
* create a postgres-db `nabucco` with user and pw `postgres` - or modify `settings.py` or set propper environment variables
    --> note that with Windows, PostgreSQL13 seems not to work: use version 12
* run `python manage.py makemigrations` then `python manage.py migrate` and  `python manage.py runserver` to migrate database and start the dev server
* (in another window) run `python manage.py import_data` to, well, to import the data

optional:

* run `xml_to_csv.py` (parses xmls in `data/xml` and writes data into `data/csv`, for each class one csv) and rename `data/csv/Archive.csv` to `data/csv/Archiv.csv`

## Docker

### building the image

* `docker build -t nabucco:latest .`
* `docker build -t nabucco:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see `nabucco/settings.py` for possible varibles:

`docker run -it -p 8020:8020 --rm --env-file .env_dev nabucco:latest`

### or use published image:

`docker run -it -p 8020:8020 --rm --env-file .env_dev acdhch/nabucco:latest`
