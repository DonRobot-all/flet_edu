import flet as ft

def main(page):
    # Выпадающий список для выбора языка
    language_dropdown = ft.Dropdown(
        label="Выберите язык",
        options=[
            ft.dropdown.Option("Русский"),
            ft.dropdown.Option("Английский"),
            ft.dropdown.Option("Французский")
        ]
    )

    # Флажки для дополнительных настроек
    notifications_checkbox = ft.Checkbox(label="Уведомления", value=True)
    theme_checkbox = ft.Checkbox(label="Тема светлая", value=False)
    autosave_checkbox = ft.Checkbox(label="Автосохранение", value=True)

    # Кнопка для применения настроек
    def on_apply_click(e):
        language = language_dropdown.value
        notifications = "Да" if notifications_checkbox.value else "Нет"
        theme = "Светлая" if theme_checkbox.value else "Темная"
        autosave = "Включено" if autosave_checkbox.value else "Отключено"
        page.add(ft.Text(f"Настройки сохранены:\nЯзык: {language}\nУведомления: {notifications}\nТема: {theme}\nАвтосохранение: {autosave}"))

    apply_button = ft.ElevatedButton(text="Применить", on_click=on_apply_click)

    page.add(language_dropdown, notifications_checkbox, theme_checkbox, autosave_checkbox, apply_button)

ft.app(target=main)


import flet as ft

def main(page):
    # Переключатель для включения/выключения режима темной темы
    dark_mode_switch = ft.Switch(
        label="Темная тема",
        value=False,
        on_change=lambda e: page.add(ft.Text(f"Темная тема {'включена' if e.control.value else 'выключена'}"))
    )

    page.add(dark_mode_switch)

ft.app(target=main)


import flet as ft

def main(page):
    # Флажки для выбора интересов
    music_checkbox = ft.Checkbox(label="Музыка")
    sports_checkbox = ft.Checkbox(label="Спорт")
    travel_checkbox = ft.Checkbox(label="Путешествия")
    cooking_checkbox = ft.Checkbox(label="Кулинария")

    # Текстовое поле для отображения выбранных интересов
    selected_interests = ft.TextField(label="Выбранные интересы", readonly=True)

    # Обработчик для обновления текста при изменении флажков
    def on_change(e):
        interests = []
        if music_checkbox.value:
            interests.append("Музыка")
        if sports_checkbox.value:
            interests.append("Спорт")
        if travel_checkbox.value:
            interests.append("Путешествия")
        if cooking_checkbox.value:
            interests.append("Кулинария")
        selected_interests.value = ", ".join(interests)
        page.update()

    music_checkbox.on_change = on_change
    sports_checkbox.on_change = on_change
    travel_checkbox.on_change = on_change
    cooking_checkbox.on_change = on_change

    page.add(music_checkbox, sports_checkbox, travel_checkbox, cooking_checkbox, selected_interests)

ft.app(target=main)


import flet as ft

def main(page):
    # Выпадающий список для выбора темы
    theme_dropdown = ft.Dropdown(
        label="Выберите тему",
        options=[
            ft.dropdown.Option("Светлая"),
            ft.dropdown.Option("Темная"),
            ft.dropdown.Option("Яркая")
        ]
    )

    # Переключатель для включения уведомлений
    notifications_switch = ft.Switch(
        label="Уведомления",
        value=False
    )

    # Кнопка для подтверждения выбора
    def on_apply_click(e):
        theme = theme_dropdown.value
        notifications = "Включены" if notifications_switch.value else "Выключены"
        page.add(ft.Text(f"Выбрана тема: {theme}\nУведомления: {notifications}"))

    apply_button = ft.ElevatedButton(text="Применить", on_click=on_apply_click)

    page.add(theme_dropdown, notifications_switch, apply_button)

ft.app(target=main)


import flet as ft

def main(page):
    # Выпадающий список для выбора возраста
    age_dropdown = ft.Dropdown(
        label="Выберите ваш возраст",
        options=[ft.dropdown.Option(str(i)) for i in range(18, 61)]
    )

    # Флажок для подтверждения активности
    active_checkbox = ft.Checkbox(label="Я активен")

    # Кнопка для подтверждения выбора
    def on_apply_click(e):
        age = age_dropdown.value
        activity_status = "Да" if active_checkbox.value else "Нет"
        page.add(ft.Text(f"Возраст: {age}\nУчастие в мероприятиях: {activity_status}"))

    apply_button = ft.ElevatedButton(text="Применить", on_click=on_apply_click)

    page.add(age_dropdown, active_checkbox, apply_button)

ft.app(target=main)
