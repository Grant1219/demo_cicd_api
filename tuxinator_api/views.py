from flask import jsonify

from tuxinator_api import app

@app.route('/')
def index():
    return jsonify({'status': 'ok'})
