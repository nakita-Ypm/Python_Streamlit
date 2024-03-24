import app
from adapter import adapter

app = app.init()

if __name__ == "__main__":
    adapter.serveApp(app)