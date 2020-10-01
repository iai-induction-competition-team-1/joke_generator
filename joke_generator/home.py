import functools

from flask import (
  Blueprint, render_template, url_for
)

from joke_generator import db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('', methods=['GET'])
def index():

  top_jokes = db.session.connection().execute("""
    SELECT context, question, answer, count(*) as num_votes
    FROM new_answer_example
    join seed_example on seed_example.id = new_answer_example.seed_example_id
    JOIN vote on vote.new_answer_example_id = new_answer_example.id
    GROUP BY new_answer_example.id, seed_example.id
    ORDER BY count(*) DESC
    LIMIT 3
  """)

  return render_template('home/index.html', top_jokes=top_jokes)
