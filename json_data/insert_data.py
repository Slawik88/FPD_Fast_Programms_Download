import json
import sqlite3


with open(r'json_data\browser.json', 'r') as f:
    data = json.load(f)


conn = sqlite3.connect('data_app.db')
c = conn.cursor()

for browser in data:
    app_image_path = data[browser]['app_image_path']
    app_name = data[browser]['app_name']
    app_developer = data[browser]['app_developer']
    app_size = data[browser]['app_size']
    app_url_website = data[browser]['app_url_website']
    app_favorites = data[browser]['app_favorites']

    c.execute("INSERT INTO browser_app (app_image_path, app_name, app_developer, app_size, app_url_website, app_favorites) VALUES (?, ?, ?, ?, ?, ?)", (app_image_path, app_name, app_developer, app_size, app_url_website, app_favorites))

conn.commit()
conn.close()