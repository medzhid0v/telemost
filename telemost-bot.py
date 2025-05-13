import os
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from client.manager import TelemostManager
from client.config import BASE_URL, CLIENT_ID, CLIENT_SECRET, OAUTH_TOKEN
from client.shemas import AccessLevel


def skip(quantity: int = 1):
    for i in range(quantity):
        time.sleep(1)
        pyautogui.press('esc')


def start_recording(wait: WebDriverWait):
    more_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'button[title="Ещё"]')
    ))
    more_button.click()

    # Теперь ждём появления и кликаем на "Записать на компьютер"
    start_record_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[title="Записать на компьютер"]')
    ))
    start_record_button.click()


def stop_recording(wait: WebDriverWait):
    more_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'button[title="Ещё"]')
    ))
    more_button.click()

    # Теперь ждём появления и кликаем на "Остановить запись на компьютер"
    stop_record_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[title="Остановить запись на компьютер"]')
    ))
    stop_record_button.click()


def bot_start(meet_url, downloads_path: str, final_path: str):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    driver.get(meet_url)
    skip()

    # Жмем подключиться
    button = driver.find_element("css selector", '[data-testid="orb-button"]')
    button.click()
    skip(3)

    button = driver.find_element("css selector", '[data-test-id="enter-conference-button"]')
    button.click()

    skip(2)

    # --- НА КОНФЕРЕНЦИИ ---
    start_recording(wait)
    time.sleep(10)  # x секунд ведем запись встречи
    stop_recording(wait)
    # --- НА КОНФЕРЕНЦИИ ---

    time.sleep(5)

    os.makedirs(final_path, exist_ok=True)

    for webm in os.listdir(downloads_path):
        if webm.endswith('запись.webm') or webm.startswith('Запись встречи'):
            print(f'Downloading {webm}')
            os.replace(os.path.join(downloads_path, webm), os.path.join(final_path, webm))


if __name__ == '__main__':
    tm = TelemostManager(
        url=BASE_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        oauth=OAUTH_TOKEN,
    )
    response = tm.create_conference(
        waiting_room_level=AccessLevel.PUBLIC,
    )

    bot_start(
        meet_url=response['join_url'],
        downloads_path=r'~\Downloads',  # Ваш путь до Downloads
        final_path=r'~\Desktop\telemost_records'  # Ваш путь до любой финальной папки
    )
