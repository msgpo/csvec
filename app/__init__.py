#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
Usage:
$ export FLASK_APP=app:create_app
$ export FLASK_ENV=development
$ flask run
'''

import os
from flask import Flask

def create_app(env=os.getenv('FLASK_ENV', 'production')):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=b'change-me'
    )
    register_blueprints(app)
    return app

def register_blueprints(app):
    from .main import create_module as main_create_module
    from .stocks import create_module as stocks_create_module
    main_create_module(app)
    stocks_create_module(app)
