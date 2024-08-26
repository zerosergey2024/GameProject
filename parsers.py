from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# Открываем страницу
url = "https://ahaslides.com/ru/blog/funny-pub-quiz-questions/"
driver.get(url)

# Ожидаем загрузки страницы
time.sleep(10)

# Ищем элементы с вопросами
questions = driver.find_elements(By.CLASS_NAME, 'question-class-name')  # Замените 'question-class-name' на нужный класс

# Список для хранения данных
parsed_data = []

if not questions:
    print("Нет найденных вопросов")

for question in questions:
    try:
        # Извлекаем текст вопроса
        question_text = question.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text

        # Извлекаем возможные ответы
        answers = question.find_elements(By.CSS_SELECTOR, 'span.answer-class-name')  # Замените 'answer-class-name' на нужный класс

        # Проверяем, что у нас есть ровно 4 ответа
        if len(answers) == 4:
            answer1 = answers[0].text
            answer2 = answers[1].text
            answer3 = answers[2].text
            answer4 = answers[3].text

            # Предположим, что правильный ответ помечен определенным классом
            true_answer = question.find_element(By.CSS_SELECTOR, 'span.correct-answer-class-name').text  # Замените 'correct-answer-class-name' на нужный класс

            # Добавляем данные в список
            parsed_data.append([question_text, answer1, answer2, answer3, answer4, true_answer])
        else:
            print(f"Вопрос '{question_text}' не содержит 4 ответов, пропускаем его.")

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

# Закрываем браузер
driver.quit()

# Записываем данные в CSV
with open('questions_and_answers.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Вопрос', 'Ответ1', 'Ответ2', 'Ответ3', 'Ответ4', 'Правильный ответ'])
    writer.writerows(parsed_data)

print("Данные успешно сохранены в файл 'questions_and_answers.csv'")