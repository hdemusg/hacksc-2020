from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)