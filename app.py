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

    user = int(request.args.get('userId'))
    count = int(request.args.get('count'))

    logging.info("Handling predict request")

    # light_fm_predict(model, int(user), 10)
    result = generator.predict(user, count)
    print(result, file=sys.stdout)

    return jsonify(result.tolist())


if __name__ == '__main__':
    print('Starting application', file=sys.stdout)
    app.run(host='127.0.0.1', port=5001, debug=True)
