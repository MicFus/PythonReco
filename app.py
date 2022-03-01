from flask import Flask, request
from flask.json import jsonify
from loader import load_lightfm_hybrid_100k
from generator import LightFMGenerator
import logging
import sys

app = Flask(__name__)
model = load_lightfm_hybrid_100k()
generator = LightFMGenerator(model)


@app.route("/predict")
def predictEndpoint():
    #app.logger.debug('Handling predict request')
    print('predict endpoint run', file=sys.stdout)

    try:
        user = int(request.args.get('userId'))
        count = int(request.args.get('count'))
        result = generator.predict(user, count)
        return jsonify(result.tolist())

    except:
        return "please provide userId and count in query string"


if __name__ == '__main__':
    print('Starting application', file=sys.stdout)
    app.run(debug=True)
