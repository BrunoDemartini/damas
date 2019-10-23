from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO

def create_app():
    
    jogador = ("x", "o")
    vez = 1;

    matriz_jogadores = [['-', 'x', '-', 'x', '-', 'x', '-', 'x', '-', 'x'],
                        ['x', '-', 'x', '-', 'x', '-', 'x', '-', 'x', '-'],
                        ['-', 'x', '-', 'x', '-', 'x', '-', 'x', '-', 'x'],
                        ['x', '-', 'x', '-', 'x', '-', 'x', '-', 'x', '-'],
                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', 'o', '-', 'o', '-', 'o', '-', 'o', '-', 'o'],
                        ['o', '-', 'o', '-', 'o', '-', 'o', '-', 'o', '-'],
                        ['-', 'o', '-', 'o', '-', 'o', '-', 'o', '-', 'o'],
                        ['o', '-', 'o', '-', 'o', '-', 'o', '-', 'o', '-']]

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)


    @socketio.on('handle click')
    def handle_message(message):
        data = message["data"]
        # cedula_selecionada = (data['i'], data['j'])
        print (matriz_jogadores [data['j']][data['i']])
        # socketio.emit('seleciona peca', {"data": data})
        @socketio.on('handle click')
        def handle_message(message):
            data = message["data"]
            i = data['i']
            j = data['j']
            # cedula_selecionada = (data['i'], data['j'])
            print (matriz_jogadores [j][i])           
            # socketio.emit('seleciona peca', {"data": data})
            if matriz_jogadores[j][i] != '-':
                socketio.emit('seleciona peca', {"data": data})

    # @socketio.on('connect')
    # def handle_connect():
    #     global jogadores
    #     jogadores += 1
    #     print(jogadores)
    #     if jogadores == 2:
    #         socketio.emit('mostra tabuleiro');

    @app.route('/')
    def home():
        return render_template('index.html')

    return app