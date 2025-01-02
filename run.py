from src.soccer_sim import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask

app_with_prefix = DispatcherMiddleware(Flask('dummy_app'), {
    '/outils/maths': app
})

if __name__ == "__main__":
    
    from werkzeug.serving import run_simple
    run_simple("127.0.0.1", 8080, app_with_prefix)