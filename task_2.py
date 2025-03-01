# Задача:
# Напишите программу с графическим интерфейсом, где пользователь может нажимать кнопку, и на экране будет 
# появляться новое число, которое увеличивается на 1 с каждым нажатием.

import flet as ft

def main(page: ft.Page):
    page.title = "Счётчик"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Переменная для хранения текущего счёта
    counter = 0

    # Текст, показывающий текущий счёт
    counter_text = ft.Text(f"Счёт: {counter}")

    # Функция для увеличения числа
    def increase_counter(e):
        nonlocal counter  # Обновление переменной counter
        counter += 1
        counter_text.value = f"Счёт: {counter}"
        page.update()

    # Кнопка для увеличения счёта
    increase_button = ft.ElevatedButton("Увеличить", on_click=increase_counter)

    # Размещение всех элементов на странице
    page.add(counter_text, increase_button)

ft.app(target=main)