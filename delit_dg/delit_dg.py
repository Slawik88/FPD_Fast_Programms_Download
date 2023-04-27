import requests
import os

# Замените API_KEY на ваш ключ от сервиса Background Removal API
API_KEY = "64482fc31569a7.46325918"

# Путь к папке с изображениями
path = "img/messenger_icon"

# Перебор всех файлов в папке
for filename in os.listdir(path):
    # Проверяем, что файл является изображением с расширением .jpg или .png
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Открываем текущий файл для чтения в двоичном режиме
        with open(os.path.join(path, filename), 'rb') as image_file:
            # Отправляем запрос на удаление фона с помощью API
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': image_file},
                data={'size': 'auto'},
                headers={'X-Api-Key': API_KEY},
            )
            # Сохраняем результат в новый файл с префиксом "no-bg-"
            with open(os.path.join(path, filename), 'wb') as out_file:
                out_file.write(response.content)
