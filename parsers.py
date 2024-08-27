from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу
url = "https://ahaslides.com/ru/blog/funny-pub-quiz-questions/"
driver.get(url)

# Ожидаем загрузки страницы
time.sleep(10)

# Ищем элементы списка с вопросами и ответами
questions = driver.find_elements(By.CSS_SELECTOR, 'ol.more-spacing > li')

# Список для хранения данных
parsed_data = []

if not questions:
    print("Нет найденных вопросов")

for question in questions:
    try:
        # Извлекаем текст вопроса
        question_text = question.text.split("\n")[0].strip()

        # Извлекаем возможные ответы
        answers_elements = question.find_elements(By.CSS_SELECTOR, 'em')
        answers_text = []
        correct_answer = ""

        for em_element in answers_elements:
            # Проверяем, если элемент содержит <strong>, это правильный ответ
            strong_element = em_element.find_elements(By.TAG_NAME, 'strong')
            if strong_element:
                correct_answer = strong_element[0].text.strip()
                # Извлекаем остальные ответы
                answers_text.extend(em_element.text.replace(correct_answer, "").strip().split(" // "))
            else:
                answers_text.extend(em_element.text.strip().split(" // "))

        # Добавляем правильный ответ в список ответов
        if correct_answer:
            answers_text.append(correct_answer)

        # Проверяем, что у нас ровно 4 ответа и правильный ответ найден
        if len(answers_text) == 4:
            parsed_data.append([question_text] + answers_text)
        else:
            print(f"Вопрос '{question_text}' не содержит 4 ответа или правильный ответ не найден, пропускаем его.")

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