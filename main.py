import flet as ft
# задание 2: добавить любимые имена
# задание 4: добавить ограничение по длине истории
def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.DARK
    greeting_text = ft.Text(value='Hello world')
    greeting_history = []
    history_text = ft.Text(value='История приветствий')
    favorite_names = []
    favorites_text = ft.Text(value='Избранные имена:')
    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()
        if name:
            greeting_text.value = f'Hello {name}'
            greeting_text.color = None
            name_input.value = ""
            greeting_history.append(name)
            greeting_history[:] = greeting_history[-5:]
            history_text.value = "История приветствий: \n" + "\n".join(greeting_history)

        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
            
        page.update()
    
    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()
    def add_to_favorites(_):
        name = name_input.value.strip()
        if name: 
            favorite_names.append(name)
            favorites_text.value = "Избранные имена:\n" + "\n".join(favorite_names)
            page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)
    send_button = ft.ElevatedButton(
        text = "Отправить",
        on_click = on_button_click,
        icon = ft.Icons.SEND,
        color = ft.Colors.GREEN,
        icon_color = ft.Colors.BLUE
    )

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    favorite_button = ft.ElevatedButton(text="В избранное", on_click=add_to_favorites, color=ft.Colors.YELLOW)
    page.add(greeting_text, ft.Row([name_input, send_button, clear_button]), history_text, ft.Row([favorite_button]), favorites_text)

ft.app(target=main)
