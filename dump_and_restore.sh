#!/bin/bash

pg_dump -d nabucco -h localhost -p 5433 -U  nabucco -c -f nabucco_dump.sql
psql -U postgres -d nabucco < nabucco_dump.sql
