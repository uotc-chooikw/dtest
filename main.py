import sys
import os
from flask import Flask, request
from flask_cors import CORS
from flasgger import Swagger
import yaml

SERVICE_VERSION = 'v1.0'
app = Flask(__name__)


# Cors configs
CORS(app, supports_credentials=True)

# Swagger Configs
app.config['SWAGGER'] = {
    'title': 'Yo ',
    'uiversion': 2
}

swagger = Swagger(app)


@app.route('/version')
def version():
    """
        Returns service version
    ---
    tags:
      - Service
    :return:
    """
    return response("123")

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', debug=True)
