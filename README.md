# Property history

## Introduction

- Create a property_history database with three tables which are owners, properties, agents.
- Generate a seed.py to seed data.
- Build a CLI to show the owner and agent id when a property id is given

## Directory structure

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    |   └── debug.py
    |   └── alembic.ini
    |   └── migrations
    |   └── property_history.db
    └── helpers.py
```

***

## CLI

Navigate to lib directory and run `python cli.py`, it will ask for input about 
an property id. 

If this input is not an integer, message `Please enter an integer: `
will be printed out to ask for an integer input. 

If the input is an integer but not 
between 1 and 500, essage `Please enter an integer between 1 and 500: ` wil be printed
out to ask for an integer input between 1 and 500. 

When an input is between 1 and 500 
which is a valid property id, a message will show this property's owner_id and agent_id.

When input equals null, CLI is terminated.

***

## property_history database

This database is set up when running Alembic migrations. All files are connected to this database which is stored in lib/db/property.db. In this database, there are three tables which are owners, properties and agents.

***

## models


