from flask import Blueprint

blueprint = Blueprint(
    'DashExample_blueprint',
    __name__,
    url_prefix='/DashExample',
    template_folder='templates',
    static_folder='static'
)
