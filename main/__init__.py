from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)

    @app.route('/')
    def home():
        return render_template('home.html')

    @socketio.on('my event')
    def handle_message(message):
        print('received message: ' + message["data"])

    return app