import os
from PIL import Image

def remove_background(path):
    for filename in os.listdir(path):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = Image.open(os.path.join(path, filename))
            img = img.convert("RGBA")
            datas = img.getdata()

            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)

            img.putdata(newData)

            # Сохраняем обработанный файл в той же папке
            img.save(os.path.join(path, filename), "PNG")
remove_background(path=r"img\temp_icon")