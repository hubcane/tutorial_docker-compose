from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye_world():
    return 'Bye World!'

if __name__ == "__main__":
    # app.run(debug=False, host= '127.0.0.1', port = 80)
    app.run(debug=False, host= '0.0.0.0', port = 80)