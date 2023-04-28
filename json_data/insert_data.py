import json
import sqlite3

# открыть json файл и загрузить данные в переменную data
with open('json_data\\game.json', 'r') as f:
    data = json.load(f)

# установить соединение с базой данных
conn = sqlite3.connect('data_app.db')
c = conn.cursor()

# проитерироваться по данным и добавить каждую запись в таблицу
for app_name, app_data in data.items():
    app_image_path = app_data['app_image_path']
    app_developer = app_data['app_developer']
    app_size = app_data['app_size']
    app_url_website = app_data['app_url_website']
    app_favorites = app_data['app_favorites']
    c.execute("INSERT INTO game_app (app_image_path, app_name, app_developer, app_size, app_url_website, app_favorites) VALUES (?, ?, ?, ?, ?, ?)",
              (app_image_path, app_name, app_developer, app_size, app_url_website, app_favorites))

# сохранить изменения и закрыть соединение с базой данных
conn.commit()
conn.close()