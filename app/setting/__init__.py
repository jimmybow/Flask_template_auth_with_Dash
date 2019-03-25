from flask import Blueprint

blueprint = Blueprint(
    'setting_blueprint',
    __name__,
    url_prefix='/setting',
    template_folder='templates',
    static_folder='static'
)
