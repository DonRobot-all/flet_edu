import flet as ft

def main(page):
    # Ввод чисел
    num1 = ft.TextField(label="Число 1", autofocus=True)
    num2 = ft.TextField(label="Число 2")

    # Результат
    result = ft.TextField(label="Результат")

    # Функция обработки нажатия кнопки
    def on_click(e):
        try:
            val1 = float(num1.value)
            val2 = float(num2.value)
            res = val1 + val2  # Пример сложения
            result.value = str(res)
        except ValueError:
            result.value = "Ошибка ввода"
        page.update()

    # Кнопка для вычисления
    calc_button = ft.ElevatedButton(text="Вычислить", on_click=on_click)

    # Размещение на странице
    page.add(num1, num2, calc_button, result)

ft.app(target=main)