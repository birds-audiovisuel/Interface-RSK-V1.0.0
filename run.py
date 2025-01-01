from src.soccer_sim import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')