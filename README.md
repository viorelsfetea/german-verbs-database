# german-verbs-database
Downloadable database of german verbs and conjugations as found on wiktionary.org


## install the requirements

Use a virtual environment, `python3 -m venv venv && source /venv/bin/activate`

```
pip install -r requirements.txt
```

## explore the data

### convert csv to sqlitedb

```
pip install csvs-to-sqlite
csvs-to-sqlite output/verbs.csv output/verbs.db
```

### explore the data in the browser

```
pip install datasette
datasette output/verbs.db
```

View and run SQL queries in the browser: [http://127.0.0.1:8001/verbs/verbs](http://127.0.0.1:8001/verbs/verbs)