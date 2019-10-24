from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO

from main.damas import Damas

SIZE = 10
con_count = 0

def create_app():


    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)
    damas = Damas()


    @socketio.on('handle click')
    def handle_message(message):
        data = message["data"]
        i = data['i']
        j = data['j']
        events = damas.handle_click(i, j)
        for e in events:
            socketio.emit(e.type, e.data)

    @socketio.on('connect')
    def handle_connect():
        global con_count
        con_count += 1
        if con_count == 2:
            socketio.emit('mostra tabuleiro');

    @app.route('/')
    def home():
        return render_template('index.html')

    return app