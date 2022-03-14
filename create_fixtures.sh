#!/usr/bin/env bash
# create_fixtures.sh

# make sure you ran `pip install django-fixture-magic` and added `'fixture_magic'` to INSTALLED_APPS
source env/bin/activate

echo "create fixtures_tablet"
python manage.py dump_object archiv.tablet 6 860 772 > fixtures_tablet.json

echo "create fixtures_glossary"
python manage.py dump_object archiv.glossary 6 45 > fixtures_glossary.json

echo "create fixtures_archiv"
python manage.py dump_object archiv.archiv 52 > fixtures_archiv.json

echo "merging fixturs"
python manage.py merge_fixtures fixtures_tablet.json fixtures_glossary.json fixtures_archiv.json > archiv/fixtures/dump.json

echo "delete fixtures"
rm fixtures_tablet.json
rm fixtures_glossary.json
rm fixtures_archiv.json

echo "done"