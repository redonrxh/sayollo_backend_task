from flask_sqlalchemy import SQLAlchemy
from flask import Flask, url_for, g
from flask_cors import CORS
from flask_restx import Api, Namespace
from importlib import import_module
import json
from config import getConfig
from app.src.db.driver import init_db

config = getConfig()

app = Flask(__name__)
CORS(app)
app.config.from_object(config)

db = SQLAlchemy(app)
init_db(db)


class Custom_API(Api):
    # override specs url to be relative not absolute
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)


api = Custom_API(
    app,
    version=app.config['VERSION'],
    title='Sayollo',
    description='Sayollo SwaggerUI',
    doc='/api/',
    validate=True
)

order = [
    'getAd', 'impression'
]
for name in order:
    endpoint = import_module(f'app.src.endpoints.{name}')

    for name in dir(endpoint):
        if name.endswith('_api'):
            attribute = getattr(endpoint, name)
            if isinstance(attribute, Namespace):
                api.add_namespace(attribute)
