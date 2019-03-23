from app.home import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/')
@login_required
def index():
    return render_template('index.html')