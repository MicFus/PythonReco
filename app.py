from flask import Flask, request

app = Flask(__name__)


@app.route("/train")
def testEndpoint():

    return "Hello, this is test endpoint"


@app.route("/predict")
def predictEndpoint():
    user = request.args.get('userId')
    return f"Hello, this is predict endpoint with {user} id"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
