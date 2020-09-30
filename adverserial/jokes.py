import functools

from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from  sqlalchemy.sql.expression import func

from adverserial import db, SeedExample, NewAnswerExample, NewQuestionExample, NewContextExample, Vote

bp = Blueprint('jokes', __name__, url_prefix='/jokes')

@bp.route('/answer', methods=['GET'])
def answer():
  return render_template('jokes/answer.html', seed_example=SeedExample.query.order_by(func.random()).first())

@bp.route('/answer', methods=['POST'])
def record_answer():
  new_example = NewAnswerExample(
    seed_example_id = request.form['seed_example_id'],
    answer = request.form['answer']
  )
  db.session.add(new_example)
  db.session.commit()

  return redirect(url_for('home.index'))

@bp.route('/question', methods=['GET'])
def question():
  return render_template('jokes/question.html', seed_example=SeedExample.query.order_by(func.random()).first())

@bp.route('/question', methods=['POST'])
def record_question():
  new_example = NewQuestionExample(
    seed_example_id = request.form['seed_example_id'],
    question = request.form['question']
  )
  db.session.add(new_example)
  db.session.commit()

  return redirect(url_for('jokes.context'))

@bp.route('/context', methods=['GET'])
def context():
  return render_template('jokes/context.html', seed_example=SeedExample.query.order_by(func.random()).first())

@bp.route('/context', methods=['POST'])
def record_context():
  new_example = NewContextExample(
    seed_example_id = request.form['seed_example_id'],
    context = request.form['context']
  )
  db.session.add(new_example)
  db.session.commit()

  return redirect(url_for('home.index'))


@bp.route('/vote', methods=['GET'])
def vote():
  jokes = NewAnswerExample.query.order_by(func.random()).limit(3)
  return render_template('jokes/vote.html', jokes=jokes)

@bp.route('/vote', methods=['POST'])
def record_vote():
  new_vote = Vote(
    new_answer_example_id = request.form['joke_id'],
  )
  db.session.add(new_vote)
  db.session.commit()

  return redirect(url_for('home.index'))
