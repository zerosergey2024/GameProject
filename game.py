import tkinter as tk

from tkinter import messagebox

import sqlite3

import random

import time

# Настройка базы данных

def setup_database():

    conn = sqlite3.connect('quiz_game.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (

                        id INTEGER PRIMARY KEY, 

                        username TEXT, 

                        email TEXT, 

                        avatar TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (

                        id INTEGER PRIMARY KEY, 

                        category TEXT, 

                        question TEXT, 

                        answer TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS stats (

                        user_id INTEGER, 

                        games_played INTEGER, 

                        wins INTEGER, 

                        losses INTEGER)''')

    conn.commit()

    conn.close()

# Основной класс игры

class QuizGame:

    def __init__(self, master):

        self.master = master

        master.title("Викторина")

        self.username = "Пользователь"

        self.score = 0

        self.setup_ui()

    def setup_ui(self):

        # Настройка интерфейса

        tk.Button(self.master, text="Начать игру", command=self.start_game).pack()

        tk.Button(self.master, text="Статистика", command=self.show_stats).pack()

    def start_game(self):

        # Логика старта игры

        category = random.choice(['история', 'наука', 'культура', 'спорт'])

        self.ask_question(category)

    def ask_question(self, category):

        # Логика задавания вопроса и проверки ответа

        # Здесь будет реализован таймер и подсчет очков

        question = f"Что такое {category}?"

        answer = "Ответ"  # Это пример, должен быть реальный вопрос

        # Таймер и логика проверки ответа

        messagebox.showinfo("Вопрос", question)

    def show_stats(self):

        messagebox.showinfo("Статистика", "Количество игр: ...")  # Вывод статистики

# Запуск игры

if __name__ == "__main__":

    setup_database()

    root = tk.Tk()

    game = QuizGame(root)

    root.mainloop()

