# Задача:
# Напишите программу с графическим интерфейсом, где отображается список чисел. Пользователь может добавить число в 
# список, и оно будет отображаться на экране. После добавления число должно быть отображено в списке.

import flet as ft

# Список чисел
numbers = []

def main(page: ft.Page):
    page.title = "Список чисел"
    # page.vertical_alignment = ft.MainAxisAlignment.START

    # Функция для обновления списка чисел на экране
    def update_numbers():
        number_list.controls.clear()  # Очищаем текущий список на экране
        for number in numbers:
            number_list.controls.append(ft.Text(f"Число: {number}"))
        page.update()  # Обновляем страницу

    # Функция для добавления нового числа
    def add_number(e):
        try:
            num = int(number_input.value)  # Преобразуем введённое значение в число
            numbers.append(num)  # Добавляем число в список
            number_input.value = ""  # Очищаем поле ввода
            update_numbers()  # Обновляем список
        except ValueError:
            pass  # Если введено не число, ничего не делаем

    # Поле для ввода числа
    number_input = ft.TextField(label="Введите число", autofocus=True)

    # Кнопка для добавления числа в список
    add_button = ft.ElevatedButton("Добавить число", on_click=add_number)

    # Список чисел
    number_list = ft.Column()

    # Размещение всех элементов на странице
    page.add(number_input, add_button, number_list)

ft.app(target=main)