import flet as ft
from datetime import datetime

def main(page: ft.Page):
    # Настройки страницы
    page.title = "Дневник настроения"
    page.theme_mode = "light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 30

    # Данные пользователя
    user_name = ft.Ref[ft.TextField]()
    mood_level = ft.Ref[ft.Slider]()
    daily_note = ft.Ref[ft.TextField]()
    stats_text = ft.Ref[ft.Text]()

    # Иконки для настроения
    mood_icons = {
        1: ft.Icon(ft.icons.MOOD_BAD, color="red"),
        2: ft.Icon(ft.icons.SENTIMENT_DISSATISFIED, color="orange"),
        3: ft.Icon(ft.icons.SENTIMENT_NEUTRAL, color="yellow"),
        4: ft.Icon(ft.icons.SENTIMENT_SATISFIED, color="lightgreen"),
        5: ft.Icon(ft.icons.MOOD, color="green")
    }

    # Сохранённые записи
    entries = []

    # Обработчик сохранения записи
    def save_entry(e):
        if not user_name.current.value:
            user_name.current.error_text = "Введите имя"
            page.update()
            return

        entries.append({
            "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "name": user_name.current.value,
            "mood": int(mood_level.current.value),
            "note": daily_note.current.value
        })

        update_stats()
        daily_note.current.value = ""
        page.snack_bar = ft.SnackBar(ft.Text("Запись сохранена!"), open=True)
        page.update()

    # Обновление статистики
    def update_stats():
        if not entries:
            stats_text.current.value = "Нет записей"
            return

        happy_days = sum(1 for entry in entries if entry["mood"] >= 4)
        stats_text.current.value = (
            f"Всего записей: {len(entries)}\n"
            f"Хороших дней: {happy_days}\n"
            f"Последняя запись: {entries[-1]['date']}"
        )
        page.update()

    # Переключение темы
    def toggle_theme(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        theme_button.current.icon = (
            ft.icons.DARK_MODE if page.theme_mode == "light" else ft.icons.LIGHT_MODE
        )
        page.update()

    theme_button = ft.Ref[ft.IconButton]()

    # Интерфейс
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Дневник настроения", size=24, weight="bold"),
                        ft.IconButton(
                            icon=ft.icons.DARK_MODE,
                            on_click=toggle_theme,
                            ref=theme_button
                        )
                    ],
                    alignment="spaceBetween"
                ),
                ft.TextField(label="Ваше имя", ref=user_name, width=300),
                ft.Text("Оцените настроение (1-5):"),
                ft.Slider(
                    min=1, max=5, divisions=4,
                    label="{value}", ref=mood_level
                ),
                ft.Row(
                    [mood_icons[int(mood_level.current.value if mood_level.current else 3)]],
                    alignment="center"
                ),
                ft.TextField(
                    label="Заметка за сегодня",
                    multiline=True, max_lines=4,
                    ref=daily_note, width=300
                ),
                ft.ElevatedButton("Сохранить", on_click=save_entry),
                ft.Divider(),
                ft.Text("Статистика:", weight="bold"),
                ft.Text(ref=stats_text)
            ],
            spacing=20
        )
    )

    # Инициализация статистики
    update_stats()

ft.app(target=main)