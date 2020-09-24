# basic-example-gathering
Basic webapp for gathering adversial examples

## Setup

### Dependencies

* Python 3
* Eventually a database (probably PostgreSQL)

Assuming *nix like OS (e.g. Mac or Linux), can add Windows instructions if needed.

0. Clone this repo
1. Recommend using a virtual environment venv - `python3 -m venv venv` as a one-off to create then `. venv/bin/activate` to activate each time you work on project
2. `pip install -r requirements.txt`
3. Create a database
4. Create your own `.env` file (base it off `.env.example` but you'll need to adapt it to your own machine)
5. Run any database migrations: `FLASK_APP=adverserial FLAST_ENV=development flask db upgrade`

## Usage

### Server

`FLASK_APP=adverserial FLAST_ENV=development flask run`

App will be available at http://localhost:5000

### Run database migrations

`FLASK_APP=adverserial FLAST_ENV=development flask db upgrade`
