import time
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


def process_query(query):
    # замена пробела на нижнее подчёркивание
    query = query.replace(" ", "_")

    # опции для Firefox
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.privatebrowsing.autostart", True)
    options.set_preference("network.cookie.cookieBehavior", 1)
    options.set_preference("browser.cookies.lifetimePolicy", 2)
    options.set_preference("browser.cache.disk.enable", False)
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    # запуск браузера и открытие страницы Google Images
    driver = webdriver.Firefox(options=options)
    driver.get("https://images.google.com/")

    wait = WebDriverWait(driver, 10)

    try:
        # нажатие на кнопку "Принять" для согласия с использованием cookies
        accept_cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div')))
        accept_cookie_button.click()
    except TimeoutException:
        pass

    # поиск поля ввода и ввод запроса
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(f"{query} messager logo, transparent background")
    search_box.submit()

    # ожидание загрузки изображений
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="islrg"]//img')))

    # получение первого изображения и сохранение его в файл
    first_image = driver.find_element(By.XPATH, '//div[@id="islrg"]//img')
    image_base64 = first_image.get_attribute('src').split(',')[1]
    image_data = base64.b64decode(image_base64)

    if not os.path.exists('img\\temp_icon'):
        os.makedirs('img\\temp_icon')

    with open(f'img\\temp_icon\\icon_{query}.png', 'wb') as f:
        f.write(image_data)

    driver.quit()


if __name__ == '__main__':
    requests_input_list = input(f"{Fore.LIGHTCYAN_EX} 🚩 Введите список программ через запятую: {Style.RESET_ALL}").split(",")
    requests_input_max_workers = int(input(f"{Fore.LIGHTCYAN_EX} 🚩 Введите макс потоков: {Style.RESET_ALL}"))
    clear_console()
    print(f"Запросы: {requests_input_list}")
    print(f"Потоки: {requests_input_max_workers}")
    print(f"{Fore.YELLOW}  Начинаем загрузку иконок...  {Style.RESET_ALL}")
    with ThreadPoolExecutor(max_workers=requests_input_max_workers) as executor:
        futures = [executor.submit(process_query, query.replace(" ", "_")) for query in requests_input_list]
        for future, query in tqdm(zip(futures, requests_input_list), total=len(requests_input_list)):
            future.result()
            tqdm.write(f"{Fore.GREEN }😉 Загрузка завершена для {query}!  {Style.RESET_ALL}")
    print(f"\n{Fore.GREEN} ✔ Загрузка завершена! {Style.RESET_ALL}")


