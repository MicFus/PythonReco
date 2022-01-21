from flask import Flask, request
from flask.json import jsonify
from modelLoader import load

app = Flask(__name__)


@app.route("/train")
def testEndpoint():

    return "Hello, this is test endpoint"


@app.route("/predict")
def predictEndpoint():
    user = request.args.get('userId')
    if not model:
        return "model is not instantiated yet"

    return jsonify(model)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    model = load()
