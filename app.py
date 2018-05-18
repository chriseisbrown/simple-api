from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello numpty!"


# endpoint to perform a tokenisation
@app.route("/tokenise", methods=["POST"])
def tokenise():
    value = request.form['value']
    return value


if __name__ == '__main__':
    app.run(debug=True)