from flask import Flask
from src.api import api
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


if __name__ == '__main__':
    app = Flask(__name__)
    api.init_app(app)
    port = 9779
    app.run(debug=False, port=port, host='0.0.0.0')
