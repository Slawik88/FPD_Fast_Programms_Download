import json
import customtkinter
from config import height




















def render_frame_for_settings(app):
    # Создание фрейма для кнопки settings
    frame_for_settings = customtkinter.CTkFrame(
        master=app,                   # родительский виджет
        width=500,                    # ширина фрейма
        height=height,                # высота фрейма
        border_width=2,               # ширина границы фрейма
        border_color="green",         # цвет границы фрейма
    )



    # Содержимое фрейма для settings
    label2 = customtkinter.CTkLabel(
        master=frame_for_settings,     # родительский виджет
        text="Dark Mod",                # текст метки
    )
    label2.grid(row=1, column=1, pady=20, padx=15)  # размещение метки в фрейме

    # Определяем функцию для обновления значения мода в JSON-файле при выборе из выпадающего меню


    def select_mod(choice):
        # Выводим выбранную опцию в консоль
        print("optionmenu dropdown clicked:", choice)
        # Открываем JSON-файл на чтение
        with open(r'json_data\settings_data\settings.json', 'r') as f:
            # Загружаем содержимое файла в объект Python
            data = json.load(f)
            # Обновляем значение ключа 'Mod' в зависимости от выбора пользователя
            if choice == "Dark":
                data['Global_Value']['Mod'] = choice
            elif choice == "White":
                data['Global_Value']['Mod'] = choice
        # Открываем JSON-файл на запись
        with open(r'json_data\settings_data\settings.json', 'w') as f:
            # Записываем обновленные данные в файл
            json.dump(data, f)



    select_mod_var = customtkinter.StringVar(value="Select")
    optionmenu_select_mod = customtkinter.CTkOptionMenu(frame_for_settings, values=["Dark", "White"],
                                                        command=select_mod,
                                                        variable=select_mod_var)
    optionmenu_select_mod.grid(row=1, column=2, pady=20, padx=15)
    return frame_for_settings