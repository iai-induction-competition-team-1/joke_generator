import functools

from flask import (
  Blueprint, render_template, url_for
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('', methods=['GET'])
def index():

  return render_template('home/index.html')
