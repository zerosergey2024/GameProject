from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send
import eventlet
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Данные викторины: вопросы и ответы
questions = {
    "history": [
        ("Кто был первым президентом США?", "Джордж Вашингтон"),
        ("В каком году закончилась Вторая мировая война?", "1945"),
    ],
    "science": [
        ("Что является самой маленькой частицей материи?", "Атом"),
        ("Как называется самая близкая к Земле звезда?", "Солнце"),
    ],
    "culture": [
        ("Кто написал 'Гамлета'?", "Шекспир"),
        ("Какая страна является родиной балета?", "Россия"),
    ],
    "sport": [
        ("В каком виде спорта используется ракетка?", "Теннис"),
        ("Сколько игроков в команде по футболу?", "11"),
    ],
}

players = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    players[username] = {'room': room, 'score': 0, 'question_index': 0}
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)

@socketio.on('start_quiz')
def start_quiz(data):
    username = data['username']
    room = data['room']
    category = data['category']
    players[username]['category'] = category
    players[username]['question_index'] = 0
    players[username]['score'] = 0
    next_question(username, room)

@socketio.on('answer')
def check_answer(data):
    username = data['username']
    room = data['room']
    answer = data['answer']
    category = players[username]['category']
    question_index = players[username]['question_index']
    _, correct_answer = questions[category][question_index]
    if answer.strip().lower() == correct_answer.lower():
        players[username]['score'] += 1
    players[username]['question_index'] += 1
    next_question(username, room)

def next_question(username, room):
    category = players[username]['category']
    question_index = players[username]['question_index']
    if question_index < len(questions[category]):
        question, _ = questions[category][question_index]
        socketio.emit('next_question', {'question': question}, to=room)
    else:
        score = players[username]['score']
        socketio.emit('show_results', {'score': score, 'total': len(questions[category])}, to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)