import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
  )

  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  db.init_app(app)
  migrate.init_app(app, db)

  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  return app

class Example(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  context = db.Column(db.String)
  question = db.Column(db.String)
  answer_a = db.Column(db.String)
  answer_b = db.Column(db.String)
  answer_c = db.Column(db.String)
  correct_answer = db.Column(db.String)
