import json

# Открываем JSON файл и загружаем его содержимое
with open('json_data\game.json', 'r') as f:
    data = json.load(f)

# Проходим по всем элементам в JSON и заменяем пробелы на нижнее подчеркивание
for key, value in data.items():
    if key == 'app_image_path' and isinstance(value, str):
        data[key] = value.replace(' ', '_')

# Сохраняем измененный JSON обратно в файл
with open('json_data\mew_game.json', 'w') as f:
    json.dump(data, f)
