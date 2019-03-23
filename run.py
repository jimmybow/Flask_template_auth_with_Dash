from flask_migrate import Migrate
from os import environ
from sys import exit
import string, random
from flask_caching import Cache
from configs.config import config_dict
from app import create_app, db

get_config_mode = environ.get('GENTELELLA_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid GENTELELLA_CONFIG_MODE environment variable entry.')

app = create_app(config_mode)
Migrate(app, db)

if __name__ == "__main__":
    app.run(debug = True)