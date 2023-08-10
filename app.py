from flask import Flask, request, jsonify, Response, json
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

services = Services()

@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("doc.html", "r") as f:
        return f.read()

@app.route("/get_dialect", methods=["GET"])
def get_dialect():
    try:
        character = request.args.get("character")
        dialect = request.args.get("dialect")
        if not character or not dialect:
            response_content = '{"error": "Both character and dialect must be provided"}'
            return Response(response_content, status=400, content_type="application/json; charset=utf-8")

        result = services.get_dialect(character, dialect)
        response_content = f'{{"result": "{result}"}}'
        return Response(response_content, content_type="application/json; charset=utf-8")

    except Exception as e:
        response_content = f'{{"error": "{str(e)}"}}'
        return Response(response_content, status=500, content_type="application/json; charset=utf-8")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
