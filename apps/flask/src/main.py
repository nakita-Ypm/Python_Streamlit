import sys
import os

def import_path(path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    handler_dir = os.path.abspath(os.path.join(current_dir, path))
    sys.path.append(handler_dir)

import_path('adapter')

import adapter
import app

app = app.init()

if __name__ == "__main__":
    adapter.serveApp(app)