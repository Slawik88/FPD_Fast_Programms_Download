# Импорт модуля customtkinter и функции create_browser_window из модуля window.browser_window
import customtkinter
from window.browser_window import create_browser_window
from window.message_window import create_message_window
from window.game_window import create_game_window
from window.music_window import create_music_window
from window.programming_window import create_programming_window
from window.tweaks_window import create_tweaks_window
from window.antivirus_window import create_antivirus_window
from window.installations_window import create_installations_window
from window.favorite_window import create_favorite_window

# Создание функции create_ctkframe, которая создает кастомный фрейм
def create_ctkframe(master, row, column, sticky=None, rowspan=None, width=100, height=100, border_width=2, border_color="green"):
    # Создание экземпляра CTkFrame и размещение его на master, используя сеточную компоновку
    customtkinter.CTkFrame(master=master, width=width, height=height, border_width=border_width, border_color=border_color
    ).grid(row=row, column=column, rowspan=rowspan, sticky=sticky)

# Создание обратного вызова функции on_click_list_of_categories_marks_callback
def on_click_list_of_categories_marks_callback(value):
    # Вывод сообщения о нажатии на кнопку
    print("segmented button clicked:", value)
    # Если нажата кнопка Browsers, вызов функции create_browser_window
    if value == "Browsers":
        create_browser_window()
    # Если нажата кнопка Messages, создание нового окна
    elif value == "Messages":
        create_message_window()
    # Если нажата кнопка Games, создание нового окна
    elif value == "Games":
        create_game_window()
    # Если нажата кнопка Music, создание нового окна
    elif value == "Music":
        create_music_window()
    # Если нажата кнопка Programming, создание нового окна
    elif value == "Programming":
        create_programming_window()
    elif value == "Tweaks":
        create_tweaks_window()
    elif value == "Antivirus":
        create_antivirus_window()
    elif value == "Installation":
        create_installations_window()
    elif value == "Favorites":
        create_favorite_window()