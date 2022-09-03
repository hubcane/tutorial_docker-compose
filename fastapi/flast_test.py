from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/hello", methods=['GET'])
def hello():
  return "hello world"

@app.route("/world", methods=['GET'])
def world():
  return "bye bye world"


if __name__ == "__main__":
  app.run()