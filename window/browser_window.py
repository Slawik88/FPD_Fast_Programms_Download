import tkinter
from PIL import ImageTk, Image  # Импортирование модулей для работы с изображениями
from config import app_title  # Импортирование переменной заголовка приложения из файла config.py
import io  # Импортирование модуля io для работы с потоками данных
import webbrowser  # Импортирование модуля для открытия ссылок в браузере
from PIL import Image  # Импортирование модуля для работы с изображениями
from config import app_title  # Импортирование переменной заголовка приложения из файла config.py
import sqlite3  # Импортирование модуля для работы с базами данных SQLite
import customtkinter  # Импортирование модуля customtkinter для создания пользовательского интерфейса



# Создание окна браузеров
def create_browser_window():  
    def open_website(url):
        webbrowser.open(url)
    check_var = tkinter.StringVar(value="off")
    def checkbox_event():
        print("checkbox toggled, current value:", check_var.get())
    browsers_window = customtkinter.CTkToplevel()  # Создание верхнего уровня окна
    browsers_window.geometry(f"{1200}x{700}")  # Задание размеров окна
    browsers_window.title(f"{app_title} -- Browsers")  # Задание заголовка окна



    browsers_window.grid_rowconfigure(0, weight=1)
    browsers_window.grid_columnconfigure((0, 1), weight=1)

    # Создание прокручиваемого фрейма для браузеров
    browser_scrollable_frame = customtkinter.CTkScrollableFrame(master=browsers_window, width=1200, height=1000, label_text="Browser_apps", orientation="vertical")
    browser_scrollable_frame.grid(row=0, column=0, padx=20, pady=20)  # Размещение фрейма в окне




    # Подключение к базе данных и выбор всех записей из таблицы browser_app
    conn = sqlite3.connect('data_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM browser_app')

    # Создание элементов интерфейса для каждой записи в таблице
    for row in cursor.fetchall():
        # Создание элемента для изображения
        # cursor.execute(f'SELECT image FROM browser_app WHERE id = {row[0]}')
        # image_data = cursor.fetchone()[0]
        # image = customtkinter.CTkImage(dark_image=Image.open(io.BytesIO(image_data)).convert('RGBA'))
        app_id = row[0]
        app_image_path = row[1]
        app_name = row[2]
        app_developer = row[3]
        app_size = row[4]
        app_url_website = row[5]
        app_favorites = row[6]

        # Создание элемента для отображения ID браузера
        label_id_product = customtkinter.CTkLabel(master=browser_scrollable_frame,
                                                  text=app_id,  # текст для отображения - ID продукта из базы данных
                                                  font=("Monaco", 15, "roman"),  # выбор шрифта и размера текста
                                                  )
        label_id_product.grid(row=app_id, column=0, padx=15, pady=15)  # установка позиции элемента на сетке


        image_init_icon_product = customtkinter.CTkImage(dark_image=Image.open(app_image_path), size=(35, 35))
        label_image_icon_product = customtkinter.CTkLabel(master=browser_scrollable_frame, text=None, image=image_init_icon_product)
        label_image_icon_product.grid(row=app_id, column=1, padx=15, pady=15)


        # Создание элемента для отображения названия браузера
        label_name_product = customtkinter.CTkLabel(master=browser_scrollable_frame, 
                                                    text=app_name,  # текст для отображения - название продукта из базы данных
                                                    font=('Nunito', 15, 'bold'),  # выбор шрифта, размера и жирности текста
                                                    )
        label_name_product.grid(row=app_id, column=2, padx=15, pady=15)  # установка позиции элемента на сетке

        # Создание элемента для отображения названия компании-разработчика браузера
        label_name_company = customtkinter.CTkLabel(master=browser_scrollable_frame, 
                                                    text=app_developer,  # текст для отображения - название компании из базы данных
                                                    font=('Lobster', 14),  # выбор шрифта и размера текста
                                                    )
        label_name_company.grid(row=app_id, column=3, padx=15, pady=15)  # установка позиции элемента на сетке
        label_name_company.configure(wraplength=200)
        
        # Создание элемента для отображения розмера браузера
        label_size_product = customtkinter.CTkLabel(master=browser_scrollable_frame, 
                                                    text=f"{app_size}  mb",  # текст для отображения - размер продукта из базы данных
                                                    font=('Viner Hand', 14, "roman"),  # выбор шрифта и размера текста
                                                    width=10,
                                                    )
        label_size_product.grid(row=app_id, column=4, padx=15, pady=15)  # установка позиции элемента на сетке

        # Создание элемента для отображения ссылки на оффициальный сайт браузера
        button_link_site_product = customtkinter.CTkButton(master=browser_scrollable_frame, 
                                                           text="Download",  # текст на кнопке
                                                           font=('Roboto', 14),  # выбор шрифта и размера текста на кнопке
                                                           command=lambda u=app_url_website: open_website(u)) # функция, которая будет вызвана при нажатии на кнопку
        button_link_site_product.grid(row=app_id, column=5, padx=15, pady=15)  # установка позиции элемента на сетке

        checkbox_check_favorite_status = customtkinter.CTkCheckBox(master=browser_scrollable_frame, text="favorite_app", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
        checkbox_check_favorite_status.grid(row=app_id, column=6)

        
        



