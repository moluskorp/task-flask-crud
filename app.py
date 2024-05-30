from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/about")
def abou():
    return 'Página sobre'

if __name__ == '__main__':
    app.run(debug=True)
else:
    app.run()