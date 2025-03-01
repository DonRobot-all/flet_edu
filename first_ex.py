# Flet — библиотека Python для создания пользовательских интерфейсов
# Flet — это библиотека Python, которая позволяет разрабатывать мультплатформенные приложения с графическим интерфейсом (GUI) и веб-приложения без необходимости писать HTML, CSS и JavaScript. Flet использует Flutter в качестве движка рендеринга, но позволяет писать код исключительно на Python.

# Основные особенности Flet
# Простота — не требует знаний веб-технологий, все пишется на Python.
# Кроссплатформенность — поддерживает Windows, macOS, Linux, iOS, Android и Web.
# Реактивный UI — интерфейс обновляется автоматически при изменении состояния.
# Встроенный сервер — можно запускать приложение локально или развертывать как веб-приложение.
# Легкий деплой — можно упаковывать в исполняемые файлы (exe, dmg) или запускать в облаке.


import flet as ft
import time 
# def main(page: ft.Page):
#     t = ft.Text(value="Hello, world!", color="green")
#     page.controls.append(t)
#     page.update()

def main(page: ft.Page):
    t = ft.Text()
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)

ft.app(target=main)