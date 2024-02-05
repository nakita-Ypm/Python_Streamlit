import app

import import_path as imp

imp.import_path("adapter")

import adapter

app = app.init()

if __name__ == "__main__":
    adapter.serveApp(app)
