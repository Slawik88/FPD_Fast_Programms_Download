import json
import customtkinter

# Главная цветовая схема
with open(r'json_data\settings_data\settings.json') as f:
    # Загружаем содержимое файла в объект Python
    data = json.load(f)

    mod = data['Global_Value']['Mod']
    style = data['Global_Value']['Style']
    
    customtkinter.set_appearance_mode(mod)  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme(style)  # Themes: blue (default), dark-blue, green

# Розмеры окна
width = 1000 # ширина 
height = 700 # высота

#Заголовок окна
app_title = "Win_HP"

# розмеры приложения

customtkinter.deactivate_automatic_dpi_awareness()