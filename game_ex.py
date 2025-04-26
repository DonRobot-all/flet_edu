import flet as ft

def main(page):
    page.title = "Мини-викторина"

    # Вопрос викторины
    question_text = ft.Text("Какой язык программирования используется в Flet?")
    
    # Переменная для хранения правильного ответа
    correct_answer = "Python"

    # Выпадающий список с вариантами ответов
    answer_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Java"),
            ft.dropdown.Option("Python"),
            ft.dropdown.Option("C++")
        ],
        label="Выберите ответ"
    )

    # Место для вывода результата
    result_text = ft.Text()

    # Кнопка для проверки ответа
    def check_answer(e):
        if answer_dropdown.value == correct_answer:
            result_text.value = "✅ Правильно!"
            result_text.color = "green"
        else:
            result_text.value = "❌ Неправильно. Попробуйте ещё раз."
            result_text.color = "red"
        page.update()

    check_button = ft.ElevatedButton(text="Проверить ответ", on_click=check_answer)

    # Выводим всё на страницу
    page.add(
        question_text,
        answer_dropdown,
        check_button,
        result_text
    )

ft.app(target=main)
