import flet as ft

def main(page: ft.Page):
    page.title = "Простые примеры Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Простой текст
    text_example = ft.Text("Привет, Flet!")
    
    # Кнопка с обработчиком
    def button_click(e):
        text_example.value = "Кнопка нажата!"
        page.update()
    
    button_example = ft.ElevatedButton("Нажми меня", on_click=button_click)
    
    # Поле ввода с кнопкой
    input_field = ft.TextField(hint_text="Введите что-то")
    
    def show_input(e):
        page.add(ft.Text(f"Вы ввели: {input_field.value}"))
    
    input_button = ft.ElevatedButton("Показать", on_click=show_input)
    
    # Счетчик
    counter = ft.Text("0")
    count = 0
    
    def increment_counter(e):
        nonlocal count
        count += 1
        counter.value = str(count)
        page.update()
    
    counter_button = ft.ElevatedButton("+1", on_click=increment_counter)
    
    # Интерфейс приложения
    page.add(
        text_example,
        button_example,
        ft.Row([input_field, input_button]),
        ft.Row([counter, counter_button])
    )
    
# Запуск приложения
ft.app(target=main)
