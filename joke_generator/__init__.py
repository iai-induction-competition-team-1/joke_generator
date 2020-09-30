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
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
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

  from . import home
  app.register_blueprint(home.bp)

  from . import jokes
  app.register_blueprint(jokes.bp)

  from . import examples
  app.register_blueprint(examples.bp)

  return app

class SeedExample(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  context = db.Column(db.String)
  question = db.Column(db.String)
  answer_a = db.Column(db.String)
  answer_b = db.Column(db.String)
  answer_c = db.Column(db.String)
  correct_answer_index = db.Column(db.String)

  def correct_answer(self):
    if self.correct_answer_index.lower() == "a":
      return self.answer_a
    elif self.correct_answer_index.lower() == "b":
      return self.answer_b
    elif self.correct_answer_index.lower() == "c":
      return self.answer_c

class NewAnswerExample(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  seed_example_id = db.Column(db.Integer, db.ForeignKey('seed_example.id'), nullable=False)
  seed_example = db.relationship('SeedExample',
        backref=db.backref('new_answer_examples', lazy=True))
  answer = db.Column(db.String)

class NewQuestionExample(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  seed_example_id = db.Column(db.Integer, db.ForeignKey('seed_example.id'), nullable=False)
  seed_example = db.relationship('SeedExample',
        backref=db.backref('new_question_examples', lazy=True))
  question = db.Column(db.String)

class NewContextExample(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  seed_example_id = db.Column(db.Integer, db.ForeignKey('seed_example.id'), nullable=False)
  seed_example = db.relationship('SeedExample',
        backref=db.backref('new_context_examples', lazy=True))
  context = db.Column(db.String)

class Vote(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  new_answer_example_id = db.Column(db.Integer, db.ForeignKey('new_answer_example.id'), nullable=False)
  new_answer_example = db.relationship('NewAnswerExample',
        backref=db.backref('votes', lazy=True))
