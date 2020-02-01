from flask import Flask, render_template
import flask_restful
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)
api = flask_restful.Api(app)

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/talk", methods=['GET'])
def talk():
    return "let's talk."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)