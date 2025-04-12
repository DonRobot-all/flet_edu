import flet as ft

def main(page):
    # Выпадающий список с языками
    language_dropdown = ft.Dropdown(
        label="Выберите язык",
        options=[
            ft.dropdown.Option("Русский"),
            ft.dropdown.Option("Английский"),
            ft.dropdown.Option("Французский"),
            ft.dropdown.Option("Испанский")
        ],
        on_change=lambda e: page.add(ft.Text(f"Выбран язык: {e.control.value}"))
    )

    # Размещение на странице
    page.add(language_dropdown)

ft.app(target=main)
