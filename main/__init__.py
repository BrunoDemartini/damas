from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)

    @socketio.on('my event')
    def handle_message(message):
        print('received message: ' + message["data"])

    @socketio.on('my event', namespace='/test')
    def handle_my_custom_namespace_event(json):
        print('received json: ' + str(json))

    @app.route('/')
    def home():
        return render_template('home.html')

    return app