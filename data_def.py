# Импорт модуля customtkinter и функции create_browser_window из модуля window.browser_window
import customtkinter
from window.browser_window import create_browser_window

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
        messages_window = customtkinter.CTkToplevel()
    # Если нажата кнопка Games, создание нового окна
    elif value == "Games":
        games_window = customtkinter.CTkToplevel()
    # Если нажата кнопка Music, создание нового окна
    elif value == "Music":
        music_window = customtkinter.CTkToplevel()
    # Если нажата кнопка Programming, создание нового окна
    elif value == "Programming":
        programming_window = customtkinter.CTkToplevel()
    elif value == "Tweaks":
        tweak_window = customtkinter.CTkToplevel()
    elif value == "Antivirus":
        antivirus_window = customtkinter.CTkToplevel()
    elif value == "Installation":
        installation_window = customtkinter.CTkToplevel()
    elif value == "Favorites":
        favorites_window = customtkinter.CTkToplevel()