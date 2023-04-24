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
def create_tweaks_window():  
    conn = sqlite3.connect('data_app.db')
    # создаем курсор
    cursor = conn.cursor()
    def open_website(url):
        webbrowser.open(url)
    check_var = tkinter.StringVar(value="off")
    def checkbox_event(app_id, app_image_path, app_name, app_developer, app_size, app_url_website):
        # print(f"\n id: {app_id}\n iamge_path: {app_image_path}\n app_name: {app_name}\n app_developer: {app_developer}\n app_size: {app_size}\n app_url: {app_url_website}")
        # создаем соединение с базой данных
        # выполняем SQL-запрос на добавление записи в таблицу
        cursor.execute('''INSERT INTO favorite_app (app_image_path, app_name, app_developer, app_size, app_url_website)
                          VALUES (?, ?, ?, ?, ?)''', (app_image_path, app_name, app_developer, app_size, app_url_website))
        # сохраняем изменения в базе данных
        conn.commit()
        print("Запись добавлена!")
        
    tweaks_window = customtkinter.CTkToplevel()  # Создание верхнего уровня окна
    tweaks_window.geometry(f"{1200}x{700}")  # Задание размеров окна
    tweaks_window.title(f"{app_title} -- Tweaks")  # Задание заголовка окна


    tweaks_window.grid_rowconfigure(0, weight=1)
    tweaks_window.grid_columnconfigure((0, 1), weight=1)

    # Создание прокручиваемого фрейма для браузеров
    tweaks_scrollable_frame = customtkinter.CTkScrollableFrame(master=tweaks_window, width=1200, height=1000, label_text="Browser_apps", orientation="vertical")
    tweaks_scrollable_frame.grid(row=0, column=0, padx=20, pady=20)  # Размещение фрейма в окне




    # Подключение к базе данных и выбор всех записей из таблицы browser_app
    conn = sqlite3.connect('data_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tweaks_app')

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
        label_id_product = customtkinter.CTkLabel(master=tweaks_scrollable_frame,
                                                  text=app_id,  # текст для отображения - ID продукта из базы данных
                                                  font=("Monaco", 15, "roman"),  # выбор шрифта и размера текста
                                                  )
        label_id_product.grid(row=app_id, column=0, padx=15, pady=15)  # установка позиции элемента на сетке


        image_init_icon_product = customtkinter.CTkImage(dark_image=Image.open(app_image_path), size=(35, 35))
        label_image_icon_product = customtkinter.CTkLabel(master=tweaks_scrollable_frame, text=None, image=image_init_icon_product)
        label_image_icon_product.grid(row=app_id, column=1, padx=15, pady=15)


        # Создание элемента для отображения названия браузера
        label_name_product = customtkinter.CTkLabel(master=tweaks_scrollable_frame, 
                                                    text=app_name,  # текст для отображения - название продукта из базы данных
                                                    font=('Nunito', 15, 'bold'),  # выбор шрифта, размера и жирности текста
                                                    )
        label_name_product.grid(row=app_id, column=2, padx=15, pady=15)  # установка позиции элемента на сетке

        # Создание элемента для отображения названия компании-разработчика браузера
        label_name_company = customtkinter.CTkLabel(master=tweaks_scrollable_frame, 
                                                    text=app_developer,  # текст для отображения - название компании из базы данных
                                                    font=('Lobster', 14),  # выбор шрифта и размера текста
                                                    )
        label_name_company.grid(row=app_id, column=3, padx=15, pady=15)  # установка позиции элемента на сетке
        label_name_company.configure(wraplength=200)
        
        # Создание элемента для отображения розмера браузера
        label_size_product = customtkinter.CTkLabel(master=tweaks_scrollable_frame, 
                                                    text=f"{app_size}  mb",  # текст для отображения - размер продукта из базы данных
                                                    font=('Viner Hand', 14, "roman"),  # выбор шрифта и размера текста
                                                    width=10,
                                                    )
        label_size_product.grid(row=app_id, column=4, padx=15, pady=15)  # установка позиции элемента на сетке

        # Создание элемента для отображения ссылки на оффициальный сайт браузера
        button_link_site_product = customtkinter.CTkButton(master=tweaks_scrollable_frame, 
                                                           text="Download",  # текст на кнопке
                                                           font=('Roboto', 14),  # выбор шрифта и размера текста на кнопке
                                                           command=lambda u=app_url_website: open_website(u)) # функция, которая будет вызвана при нажатии на кнопку
        button_link_site_product.grid(row=app_id, column=5, padx=15, pady=15)  # установка позиции элемента на сетке



        # Создание элемента для добовления продукта в "Избранное"
        button_add_favorites = customtkinter.CTkButton(master=tweaks_scrollable_frame,
                                              text="Add Favorite",
                                              font=("Monaco", 12, "bold"),
                                              width=50,
                                              height=20,
                                              command=lambda app_id=app_id, app_image_path=app_image_path, app_name=app_name, app_developer=app_developer, app_size=app_size, app_url_website=app_url_website: checkbox_event(app_id, app_image_path, app_name, app_developer, app_size,app_url_website))  # передача app_id в качестве аргумента
        button_add_favorites.grid(row=app_id, column=6, padx=15, pady=15)




        
        



