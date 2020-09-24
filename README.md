# basic-example-gathering
Basic webapp for gathering adversial examples

## Setup

### Dependencies

* Python 3
* Eventually a database (probably PostgreSQL or SQLite)

Assuming *nix like OS (e.g. Mac or Linux), can add Windows instructions if needed.

1. Recommend using a virtual environment venv - `python3 -m venv venv` as a one-off to create then `. venv/bin/activate` to activate each time you work on project
2. `pip install -r requirements.txt`

## Usage

### Server

`FLASK_APP=adverserial FLAST_ENV=development flask run`

App will be available at http://localhost:5000
