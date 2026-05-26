from flask import Flask, request
from Model import predict_word

app = Flask(__name__)

@app.route("/")

def home():

    text = request.args.get("text")

    result = predict_word(text)

    return result

if __name__ == "__main__":
    app.run()