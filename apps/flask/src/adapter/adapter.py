from dotenv import load_dotenv
import os

load_dotenv()

def serveApp(app):
    default_port = 3001
    port = int(os.environ.get('PORT', default_port))
    app.run(host='0.0.0.0', port=port, debug=True)
    