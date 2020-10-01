import ast
import click
import functools
import json
import random

from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from joke_generator import db, SeedExample, NewAnswerExample

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

@bp.cli.command('export')
def export():
    for new_example in NewAnswerExample.query.all():
      new_answer = new_example.answer

      correct_answer = new_example.seed_example.correct_answer()

      other_seed_example_answers = ['A', 'B', 'C']
      other_seed_example_answers.remove(new_example.seed_example.correct_answer_index)
      for another_answer_index in other_seed_example_answers:
        if another_answer_index.lower() == 'a':
          another_answer = new_example.seed_example.answer_a
        elif another_answer_index.lower() == 'b':
          another_answer = new_example.seed_example.answer_b
        elif another_answer_index.lower() == 'c':
          another_answer = new_example.seed_example.answer_c

        answer_list = [new_answer, correct_answer, another_answer]
        random.shuffle(answer_list)
        correct_answer_index = answer_list.index(correct_answer)
        correct_answer_letter = ['A', 'B', 'C'][correct_answer_index] # conver 0,1,2 to A,B,C

        new_example_data = {'context': new_example.seed_example.context,
          'question': new_example.seed_example.question,
          'answerA': answer_list[0],
          'answerB': answer_list[1],
          'answerC': answer_list[2],
          'correct': correct_answer_letter
        }
        print(json.dumps(new_example_data))
