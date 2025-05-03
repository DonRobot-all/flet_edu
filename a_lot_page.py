import flet as ft

def main(page):
    def p(_):
        return page.go("/page2")


    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View("/", [
                ft.Text("Главная страница"),
                ft.ElevatedButton("Перейти на страницу 2", on_click=p)
            ])
        )

        if page.route == "/page2":
            page.views.append(
                ft.View("/page2", [
                    ft.Text("Страница 2"),
                    ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
                    ft.ElevatedButton("Вперёд", on_click=lambda _: page.go("/page3"))
                ])
            )

        if page.route == "/page3":
            page.views.append(
                ft.View("/page3", [
                    ft.Text("Страница 3"),
                    ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"))
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)