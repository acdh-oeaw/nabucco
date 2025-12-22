#!/usr/bin/env bash
# create_fixtures.sh

echo "create fixtures_tablet"
uv run manage.py dump_object archiv.tablet 6 860 772 623 > fixtures_tablet.json

echo "create fixtures_glossary"
uv run manage.py dump_object archiv.glossary 6 45 > fixtures_glossary.json

echo "create fixtures_archiv"
uv run manage.py dump_object archiv.archiv 52 119 > fixtures_archiv.json

echo "merging fixturs"
uv run manage.py merge_fixtures fixtures_tablet.json fixtures_glossary.json fixtures_archiv.json > archiv/fixtures/dump.json

echo "delete fixtures"
rm fixtures_tablet.json
rm fixtures_glossary.json
rm fixtures_archiv.json

echo "done"