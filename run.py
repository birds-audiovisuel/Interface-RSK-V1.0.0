from src.soccer_sim import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask

# Ajout du préfixe "/outils/maths"
#app_with_prefix = DispatcherMiddleware(Flask('dummy_app'), {
 #   '/outils/maths': app
#})

if __name__ == "__main__":
    #from werkzeug.serving import run_simple
    #run_simple("127.0.0.1", 7050, app_with_prefix)
    app.run(host='127.0.0.1', port=7050, debug=True)