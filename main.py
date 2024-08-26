import tkinter as tk
from tkinter import messagebox
import random
import time


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


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        # Инициализация переменных
        self.category = None
        self.question_index = 0
        self.score = 0
        self.timer = None
        self.time_left = 30

        # Создание главного интерфейса
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Выберите категорию:", font=("Arial", 14)).pack(pady=10)

        # Кнопки для выбора категории
        for category in questions.keys():
            tk.Button(self.root, text=category.capitalize(), width=20, height=2,
                      command=lambda c=category: self.start_quiz(c)).pack(pady=5)

    def start_quiz(self, category):
        self.category = category
        self.question_index = 0
        self.score = 0
        self.next_question()

    def next_question(self):
        if self.question_index < len(questions[self.category]):
            self.clear_window()
            question, _ = questions[self.category][self.question_index]

            tk.Label(self.root, text=question, font=("Arial", 14)).pack(pady=20)
            self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
            self.answer_entry.pack(pady=10)
            tk.Button(self.root, text="Ответить", command=self.check_answer).pack(pady=10)

            # Таймер
            self.time_left = 30
            self.timer_label = tk.Label(self.root, text=f"Время: {self.time_left} сек", font=("Arial", 12))
            self.timer_label.pack(pady=5)
            self.update_timer()
        else:
            self.show_results()

    def check_answer(self):
        _, correct_answer = questions[self.category][self.question_index]
        if self.answer_entry.get().strip().lower() == correct_answer.lower():
            self.score += 1
        self.question_index += 1
        self.next_question()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Время: {self.time_left} сек")
            self.timer = self.root.after(1000, self.update_timer)
        else:
            self.question_index += 1
            self.next_question()

    def show_results(self):
        self.clear_window()
        tk.Label(self.root, text=f"Игра окончена! Ваш результат: {self.score} из {len(questions[self.category])}",
                 font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="На главную", command=self.create_main_menu).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
