import tkinter
import customtkinter  # импортируем модуль customtkinter

from config import width, height, app_title  # импортируем переменные из модуля config
from data_def import on_click_list_of_categories_marks_callback  # импортируем функцию из модуля data_def

from PIL import ImageTk, Image  # импортируем две библиотеки из модуля PIL
app = customtkinter.CTk()  # создаем объект приложения с помощью класса CTk из модуля customtkinter


# узнаем размеры экрана
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


# вычисляем координаты центра экрана
center_x = int(screen_width / 2 - width / 2)
center_y = int(screen_height / 2 - height / 2)


# устанавливаем окно по центру экрана
app.geometry(f"{width}x{height}+{center_x}+{center_y}")
app.title(f"{app_title}")  # устанавливаем заголовок окна

# определяем функции для скрытия/отображения различных фреймов
def on_clear_all_frame_for_home():
    frame_for_home.grid(row=0, column=1)  # показываем фрейм для домашней страницы
    frame_for_applications.grid_forget()  # скрываем фрейм для приложений
    frame_for_settings.grid_forget()  # скрываем фрейм для настроек

def on_clear_all_frame_for_applications():
    frame_for_applications.grid(row=0, column=2)  # показываем фрейм для приложений
    frame_for_home.grid_forget()  # скрываем фрейм для домашней страницы
    frame_for_settings.grid_forget()  # скрываем фрейм для настроек

def on_clear_all_frame_for_settings():
    frame_for_settings.grid(row=0, column=3)  # показываем фрейм для настроек
    frame_for_home.grid_forget()  # скрываем фрейм для домашней страницы
    frame_for_applications.grid_forget()  # скрываем фрейм для приложений
# создаем функцию для создания изображения кнопки
def image_menu(path):
    button_image = customtkinter.CTkImage(light_image=Image.open(path),
                                  dark_image=Image.open(path),
                                  size=(30, 30))
    return button_image

# Создание фрейма для меню
frame_menu = customtkinter.CTkFrame(
    master=app, width=500, height=100, border_width=2, border_color="green")
frame_menu.grid(row=0, column=0, rowspan=10, sticky="nw")

# создание кнопок для меню
button_home = customtkinter.CTkButton(master=frame_menu,
                               text="Home",
                               width=200,
                               height=60,
                               corner_radius=15,
                               font=('sistem', 20, 'bold'),
                               image=image_menu(path=r"img\main_menu_icon\home.png"),
                               command=on_clear_all_frame_for_home)
button_home.grid(row=1, column=1, pady=20, padx=15)

button_applications = customtkinter.CTkButton(master=frame_menu, 
                                       text="Applications", 
                                       width=200, 
                                       height=60,
                                       corner_radius=15,
                                       image=image_menu(path=r"img\main_menu_icon\applications.png"),
                                       font=('sistem', 20, 'bold'),
                                       command=on_clear_all_frame_for_applications)
button_applications.grid(row=2, column=1, pady=20, padx=15)
                                       
button_settings = customtkinter.CTkButton(master=frame_menu, 
                                   text="Settings", 
                                   width=200, 
                                   height=60,
                                   corner_radius=15, 
                                   image=image_menu(path=r"img\main_menu_icon\settings.png"),
                                   font=('sistem', 20, 'bold'),
                                   command=on_clear_all_frame_for_settings)
button_settings.grid(row=3, column=1, pady=20, padx=15)
                                   
button_0 = customtkinter.CTkButton(master=frame_menu, 
                                   width=200, 
                                   height=60, 
                                   corner_radius=15,
                                   image=image_menu(path=r"img\main_menu_icon\zero.png"),
                                   font=('sistem', 20, 'bold'),
                                   )
button_0.grid(row=4, column=1, pady=20, padx=15)                                   
                                   
                                
button_1 = customtkinter.CTkButton(master=frame_menu, 
                                   width=200, 
                                   height=60, 
                                   corner_radius=15,
                                   image=image_menu(path=r"img\main_menu_icon\zero.png"),
                                   font=('sistem', 20, 'bold'),
                                   )
button_1.grid(row=5, column=1, pady=20, padx=15)
                                   
button_2 = customtkinter.CTkButton(master=frame_menu, 
                                   width=200, 
                                   height=60, 
                                   corner_radius=15,
                                   image=image_menu(path=r"img\main_menu_icon\zero.png"),
                                   font=('sistem', 20, 'bold'),
                                   )
button_2.grid(row=6, column=1, pady=20, padx=15)
                                   
button_3 = customtkinter.CTkButton(master=frame_menu, 
                                   width=200, 
                                   height=60, 
                                   corner_radius=15,
                                   image=image_menu(path=r"img\main_menu_icon\zero.png"),
                                   font=('sistem', 20, 'bold'),
                                   )
button_3.grid(row=7, column=1, pady=20, padx=15)                                   
                                   

# Создание фрейма для кнопки home
frame_for_home = customtkinter.CTkFrame(
    master=app,                   # родительский виджет
    width=500,                    # ширина фрейма
    height=height,                # высота фрейма
    border_width=2,               # ширина границы фрейма
    border_color="green"          # цвет границы фрейма
)

# Содержимое фрейма для home
label1 = customtkinter.CTkLabel(
    master=frame_for_home,        # родительский виджет
    text="frame_home"             # текст метки
)
label1.grid(row=1, column=1, pady=20, padx=15)  # размещение метки в фрейме

# Создание фрейма для кнопки applications
frame_for_applications = customtkinter.CTkFrame(
    master=app,                   # родительский виджет
    width=500,                    # ширина фрейма
    height=height,                # высота фрейма
    border_width=2,               # ширина границы фрейма
    border_color="green"          # цвет границы фрейма
)

# Содержимое фрейма для кнопки applications

label_help_text = customtkinter.CTkLabel(master=frame_for_applications,
                                         text="Select an application rosel that interests you",
                                         )
label_help_text.grid(row=0, column=1, pady=20, padx=15)

list_of_categories_marks = customtkinter.CTkSegmentedButton(
    master=frame_for_applications,            # родительский виджет
    values=["Browsers", "Messages", "Games", "Music", "Programming", "Tweaks", "Antivirus", "Installation", "Favorites"],  # значения кнопок
    command=on_click_list_of_categories_marks_callback,  # функция, которая вызывается при нажатии на кнопку
    font=("Arial", 15)
)
list_of_categories_marks.grid(row=1, column=0, columnspan=3, pady=20, padx=15)  # размещение виджета в фрейме


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
    text="frame_settings",         # текст метки
)
label2.grid(row=1, column=1, pady=20, padx=15)  # размещение метки в фрейме

