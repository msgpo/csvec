from flask import (
    Blueprint,
    render_template,
)

blueprint = Blueprint(
    'main',
    __name__,
)

@blueprint.route('/')
def index():
    message = 'Welcome to this page!'
    return render_template('main/index.html', **locals())
