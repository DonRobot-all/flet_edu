import flet as ft

def main(page: ft.Page):
    page.title = "Пример ListView"

    # Создаём список
    my_list = ft.ListView(
        expand=True,            # занимает всё доступное пространство
        spacing=10,             # расстояние между элементами
        padding=20,             # внутренние отступы
        auto_scroll=True        # прокручивается автоматически к новым элементам
    )

    # Добавляем несколько элементов
    for i in range(20):
        my_list.controls.append(
            ft.Text(f"Элемент {i+1}", size=20)
        )

    page.add(my_list)

ft.app(target=main)
