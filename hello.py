import flet as ft

def main(page):
    # Текстовое поле для ввода имени
    name_field = ft.TextField(label="Введите ваше имя")

    # Результат
    greeting = ft.TextField(label="Приветствие")

    # Функция обработки нажатия кнопки
    def on_click(e):
        name = name_field.value
        greeting.value = f"Привет, {name}!"
        page.update()

    # Кнопка для приветствия
    greet_button = ft.ElevatedButton(text="Приветствовать", on_click=on_click)

    # Размещение на странице
    page.add(name_field, greet_button, greeting)

ft.app(target=main)
