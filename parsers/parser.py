import time
import cv2
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import base64
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import os
from colorama import Fore, Style


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def scrape_icon(query):
    # создание объекта опций браузера и запуск браузера
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(f'https://www.google.com/search?q={query}&tbm=isch')

    # скроллинг страницы для загрузки большего количества изображений
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

    # нахождение первого изображения
    image = None
    image_url = None
    for element in driver.find_elements_by_css_selector('img.rg_i'):
        try:
            image_url = element.get_attribute('src')
            if image_url.startswith('http') and not image_url.endswith('svg'):
                image = requests.get(image_url).content
                break
        except:
            pass

    # если изображение не найдено
    if image is None:
        driver.quit()
        return None

    # сохранение изображения
    if not os.path.exists('img\\temp_icon'):
        os.makedirs('img\\temp_icon')

    with open(f'img\\temp_icon\\icon_{query}.png', 'wb') as f:
        f.write(image)

    driver.quit()

    # обработка изображения и удаление заднего фона
    image_path = f"img\\temp_icon\\icon_{query}.png"
    image = cv2.imread(image_path)

    # удаление фона
    fgbg = cv2.createBackgroundSubtractorMOG2()
    fgmask = fgbg.apply(image)
    fg = cv2.bitwise_and(image, image, mask=fgmask)

    if not os.path.exists('img\\temp_icon_not_bg'):
        os.makedirs('img\\temp_icon_not_bg')
    cv2.imwrite(f'img\\temp_icon_not_bg\\icon_{query}.png', fg)

    return f'img\\temp_icon_not_bg\\icon_{query}.png'





if __name__ == '__main__':
    requests_input_list = input(f"{Fore.LIGHTCYAN_EX} 🚩 Введите список программ через запятую: {Style.RESET_ALL}").split(",")
    requests_input_max_workers = int(input(f"{Fore.LIGHTCYAN_EX} 🚩 Введите макс потоков: {Style.RESET_ALL}"))
    clear_console()
    print(f"Запросы: {requests_input_list}")
    print(f"Потоки: {requests_input_max_workers}")
    print(f"{Fore.YELLOW}  Начинаем загрузку иконок...  {Style.RESET_ALL}")
    total_queries = len(requests_input_list)
    with ThreadPoolExecutor(max_workers=requests_input_max_workers) as executor:
        futures = [executor.submit(process_query, query.replace(" ", "_")) for query in requests_input_list]
        progress_bar = tqdm(total=total_queries)
        for future, query in zip(futures, requests_input_list):
            future.result()
            progress_bar.update(1)
            tqdm.write(f"{Fore.GREEN }😉 Загрузка завершена для {query}!  {Style.RESET_ALL}")
    print(f"\n{Fore.GREEN} ✔ Загрузка завершена! {Style.RESET_ALL}") 