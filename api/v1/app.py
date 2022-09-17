#!/usr/bin/python3
"""Flask app"""


from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.vi.views import app_views
from apiflask import abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_bleuprint(app_views)
cors = CORS(app, resources={'*': {'origins': '0.0.0.0'}})


@app.teardown_appcontext
def close_db(error):
    """close storage"""
    storage.close()

@app.route('/')
def hello():
    abort(400, message='"error": "Not found"')
    return 'Hello, world!'  # this line will never be reached


if __name__ == "__main__":
    """Main Func"""
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = "5000"
    app.run(host=host, port=port, threaded=True)
