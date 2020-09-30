import ast
import click
import functools
import json

from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from joke_generator import db, SeedExample

bp = Blueprint('examples', __name__, url_prefix='/examples')

@bp.route('', methods=['GET'])
def index():

  return render_template('examples/index.html')

@bp.route('', methods=['POST'])
def create():
  new_example = SeedExample(
    context='This happened.',
    question='What happened next?',
    answer_a='Something',
    answer_b='Nothing',
    answer_c='Everything',
    correct_answer='a',
  )
  db.session.add(new_example)
  db.session.commit()

  return redirect(url_for('examples.index'))

@bp.cli.command('replace')
@click.argument('input_file')
def replace(input_file):
    db.session.query(SeedExample).delete(synchronize_session=False)
    with open(input_file) as f:
      for line in f:
        # new_example_data = json.loads(line.strip())
        new_example_data = ast.literal_eval(line.strip())
        new_example = SeedExample(
          context = new_example_data["context"],
          question = new_example_data["question"],
          answer_a = new_example_data["answerA"],
          answer_b = new_example_data["answerB"],
          answer_c = new_example_data["answerC"],
          correct_answer_index = new_example_data["correct"]
        )
        db.session.add(new_example)
    db.session.commit()
