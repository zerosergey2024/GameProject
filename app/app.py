from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/gamecat')
def change_name():
    return render_template('gamecat.html')

@app.route('/game')
def change_email():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)