# nabucco-process

* quick and dirty repo to process nabucco xml-data (taken from [orig-repo](https://github.com/DigitalPasts/nabucco/tree/master/nabucco-xml)) into something more usabel (csv); be aware, to ease the parsing, I manually removed the namespaces from the original files
* evolved to application repo for generic nabucco app

## install [under construction]

* install required packages `pip install -r requirements.txt`
* run `python manage.py migrate && python manage.py runserver` to migrate database and start the dev server

optional:

* run `xml_to_csv.py` (parses xmls in `data/xml` and writes data into `data/csv`, for each class one csv) and rename `data/csv/Archive.csv` to `data/csv/Archiv.csv`


## Docker

### building the image

* `docker build -t nabucco:latest .`
* `docker build -t nabucco:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

```
DB_NAME=nabucco
DB_USER=postgres
DB_PASSWORD=postgres
PROJECT_NAME=nabucco
VOCABS_DEFAULT_PEFIX=nabucco
VOCABS_DEFAULT_PEFIX=en
SECRET_KEY=hanna4ever
DEBUG=True
REDMINE_ID=19546
DB_ENGINE=django.contrib.gis.db.backends.postgis
```

`docker run -it -p 8020:8020 --rm --env-file .env_dev nabucco:latest`

### or use published image:

`docker run -it -p 8020:8020 --rm --env-file .env_dev acdhch/nabucco:latest`