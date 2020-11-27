from flask import (
    Blueprint, flash, render_template, request
)

bp = Blueprint('greetings', __name__)


@bp.route('/', methods=('GET', ))
def checkin():
    # render the checkin form
    return render_template('greetings/checkin.html')

@bp.route('/', methods=('POST', ))
def say_hello():

    # get the name from the form
    name = request.form['name']

    # if the name is missing
    if not name:
        # render the checkin page with an error message
        flash("Please, introduce yourself.")
        return render_template('greetings/checkin.html')

    # render the greetings page
    return render_template('greetings/say_hello.html', name=name)
