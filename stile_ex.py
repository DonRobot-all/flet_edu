import flet as ft
from flet import Colors


def main(page: ft.Page):
    page.title = "Темы в Flet"
    
    # Установка темы
    page.theme_mode = ft.ThemeMode.DARK  # LIGHT, DARK, SYSTEM

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=Colors.BLUE,
            secondary=Colors.AMBER,
            background=Colors.GREY_900,
            surface=Colors.GREY_800,
            error=Colors.RED
        )
    )
    
    page.add(ft.Text("Привет, Flet!"))
    # page.add(ft.Text("Пример темы", color=Colors.WHITE))

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        )
        page.update()

    page.add(ft.ElevatedButton("Переключить тему", on_click=toggle_theme))

    
ft.app(target=main)


# import flet as ft
# from flet import Colors

# def main(page: ft.Page):
#     card = ft.Card(
#         content=ft.Container(
#             content=ft.Column([
#                 ft.Text("Карточка", size=18, weight="bold"),
#                 ft.Text("Описание", size=14)
#             ]),
#             padding=20,
#             bgcolor=Colors.WHITE,
#             border_radius=15,
#             width=300
#         )
#     )

#     page.add(ft.Row([card])) 

# ft.app(target=main)


# import flet as ft

# def main(page: ft.Page):
#     info_text = ft.Text("Нажмите на карточку")

#     def on_card_click(e):
#         info_text.value = "Карточка нажата!"
#         page.update()

#     card = ft.Card(
#         content=ft.Container(
#             content=ft.Column([
#                 ft.Text("Карточка", size=18, weight="bold"),
#                 ft.Text("Кликни сюда", size=14)
#             ]),
#             padding=20,
#             bgcolor=ft.Colors.WHITE,
#             border_radius=15,
#             width=300,
#             on_click=on_card_click,
#             ink=True
#         )
#     )

#     page.add(info_text, ft.Row([card]))

# ft.app(target=main)


# import flet as ft
# import random
# import time

# def main(page: ft.Page):
#     symbols = ["🍎", "🍌", "🍎", "🍌"]  # Пары
#     random.shuffle(symbols)

#     opened = []
#     buttons = []

#     def on_card_click(e):
#         idx = int(e.control.data)
#         card = buttons[idx]

#         if card.content.value != "❓" or len(opened) >= 2:
#             return  # уже открыта или 2 уже открыты

#         # открыть карточку
#         card.content.value = symbols[idx]
#         card.update()
#         opened.append((idx, symbols[idx]))

#         if len(opened) == 2:
#             page.update()
#             page.timer = ft.Timer(1000, lambda _: check_match())  # подождём чуть

#     def check_match():
#         a, val_a = opened[0]
#         b, val_b = opened[1]

#         if val_a != val_b:
#             # не совпали — закрываем
#             buttons[a].content.value = "❓"
#             buttons[b].content.value = "❓"
#             buttons[a].update()
#             buttons[b].update()

#         # иначе — пара остаётся открытой
#         opened.clear()
#         page.update()

#     # Создание карточек
#     for i in range(4):
#         btn = ft.Container(
#             content=ft.Text("❓", size=30),
#             width=100,
#             height=100,
#             bgcolor=ft.colors.BLUE_100,
#             alignment=ft.alignment.center,
#             border_radius=10,
#             ink=True,
#             on_click=on_card_click,
#             data=str(i)  # передаём индекс
#         )
#         buttons.append(btn)

#     page.add(
#         ft.Row([
#             buttons[0], buttons[1]
#         ], spacing=10),
#         ft.Row([
#             buttons[2], buttons[3]
#         ], spacing=10)
#     )

# ft.app(target=main)
