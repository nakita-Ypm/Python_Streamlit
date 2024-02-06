from flask import Flask
import sys
import os

def import_path(path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    handler_dir = os.path.abspath(os.path.join(current_dir, path))
    sys.path.append(handler_dir)

import_path('handler')

from handler import ping_handler

def init():
    app = Flask(__name__)
    apply_handlers(app)
    return app

def apply_handlers(app):
    ping_handler.apply(app)
    return app