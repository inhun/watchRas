from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

from app.api import build_api
build_api(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8091)