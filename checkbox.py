# import flet as ft

# def main(page):
#     # Переключатель для включения/выключения
#     switch = ft.Switch(
#         label="Включить режим темной темы",
#         value=False,  # начальное значение
#         on_change=lambda e: page.add(ft.Text(f"Темная тема: {'Включена' if e.control.value else 'Выключена'}"))
#     )

#     # Размещение на странице
#     page.add(switch)

# ft.app(target=main)

import flet as ft

def main(page):
    # Флажки для выбора интересов
    music_checkbox = ft.Checkbox(label="Музыка", value=True)
    sports_checkbox = ft.Checkbox(label="Спорт", value=False)
    travel_checkbox = ft.Checkbox(label="Путешествия", value=False)

    # Функция для обновления состояния
    def on_change(e):
        selected_interests = []
        if music_checkbox.value:
            selected_interests.append("Музыка")
        if sports_checkbox.value:
            selected_interests.append("Спорт")
        if travel_checkbox.value:
            selected_interests.append("Путешествия")
        page.add(ft.Text(f"Вы выбрали: {', '.join(selected_interests)}"))

    # Обработчики изменения состояния
    music_checkbox.on_change = on_change
    sports_checkbox.on_change = on_change
    travel_checkbox.on_change = on_change

    # Размещение на странице
    page.add(music_checkbox, sports_checkbox, travel_checkbox)

ft.app(target=main)
