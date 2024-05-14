from app import app
from routes import *

if __name__ == "__main__":
    app.run("127.0.0.1", 9090, debug=True)
