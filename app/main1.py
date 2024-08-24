# Импорт необходимых библиотек
from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import time

app = Flask(__name__)

# Список вопросов и ответов
questions = [
    {"question": "Столица Франции?", "options": ["Париж", "Лондон", "Рим"], "answer": 0},
    {"question": "Столица Германии?", "options": ["Берлин", "Мадрид", "Рим"], "answer": 0},
]

score = 0
current_question = 0

@app.route('/')
def index():
    global current_question, score
    current_question = 0
    score = 0
    return render_template('index1.html', question=questions[current_question], score=score)

@app.route('/answer', methods=['POST'])
def answer():
    global score, current_question
    selected_option = int(request.form['option'])
    if selected_option == questions[current_question]['answer']:
        score += 1
    current_question += 1
    if current_question >= len(questions):
        return jsonify(score=score)
    return jsonify(question=questions[current_question], score=score)

if __name__ == '__main__':
    app.run(debug=True)

