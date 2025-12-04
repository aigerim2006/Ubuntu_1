# from datetime import date
# from flet import Text, TextField

import flet as ft
import datetime as dt


def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')
    
    # greeting_text.value = 'Привет мир'
    # greeting_text.color = ft.Colors.GREEN

    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()
        
        time_now = dt.datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{time_now} Hello {name}'
            greeting_text.color = None
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
        page.update()
    def theme_dark_or_light(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    # elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    # text_button = ft.TextButton(text='send', on_click=on_button_click, icon=ft.Icons.SEND)

    # icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=on_button_click)

    send_button = ft.ElevatedButton(
        text = "Отправить",
        on_click = on_button_click,
        icon = ft.Icons.SEND,
        color = ft.Colors.GREEN,
        icon_color = ft.Colors.BLUE
    )

    theme_button = ft.IconButton(
        icon = ft.Icons.BRIGHTNESS_7,
        on_click = theme_dark_or_light
    )

    page.add(greeting_text, name_input, send_button, theme_button)

ft.app(target=main)
