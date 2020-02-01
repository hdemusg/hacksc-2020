from flask import Flask, render_template
import flask restful
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

