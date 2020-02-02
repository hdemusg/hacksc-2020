from flask import Flask, render_template, request, session
import flask_restful
import flask_cors
#from flask_socketio import SocketIO
#import os
#import firebase_admin
#from firebase_admin import credentials

#cred = credentials.Certificate('C:/Users/sumed/documents/github/hacksc-2020/key/hacksc-2020-266907-firebase-adminsdk-zhk3f-994e6fa697.json')
#firebase_admin.initialize_app(cred, {'databaseURL': 'https://hacksc-2020-266907.firebaseio.com'})
#import requests
import nlp
app = Flask(__name__)
flask_cors.CORS(app)
api = flask_restful.Api(app)
#app.config['SECRET_KEY'] = 'ioemoidvnuoi3980'
#socketio = SocketIO(app)

'''
@app.route("/")
def home():
    return render_template('home.html')
'''
'''
@app.route("/talk", methods=['POST'])
def chat(u):
    body = request.get_json()
    return render_template('talk.html', uid=u)
    '''


@app.route("/", methods=['GET'])
def talk():
    return render_template('talk.html')

@app.route("/analyze", methods=['POST'])
def analyze():
    

'''
def messageReceived(methods=['GET, POST']):
    print('message received')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    '''

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    #socketio.run(app, debug=True)

#@app.route("/", methods=['POST'])
#def login():
#    return "login"

'''
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['username']
    processed_text = text.upper()
    return processed_text
'''