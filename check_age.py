import flet as ft

def main(page):
    # Текстовое поле для ввода возраста
    age_field = ft.TextField(label="Введите ваш возраст")

    # Результат
    age_message = ft.TextField(label="Сообщение")

    # Функция обработки нажатия кнопки
    def on_click(e):
        try:
            age = int(age_field.value)
            if age >= 18:
                age_message.value = "Вы совершеннолетний!"
            else:
                age_message.value = "Вы несовершеннолетний."
        except ValueError:
            age_message.value = "Пожалуйста, введите число."
        page.update()

    # Кнопка для проверки возраста
    check_button = ft.ElevatedButton(text="Проверить возраст", on_click=on_click)

    # Размещение на странице
    page.add(age_field, check_button, age_message)

ft.app(target=main)
