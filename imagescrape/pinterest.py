import os
import time
import json
import random
import urllib.request
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.crop_utils import crop_with_yolo_or_face
from utils.telegram_updater import update_telegram_pfp

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
HISTORY_PATH = "history.json"
ARCHIVE_DIR = "archive"
LOG_FILE = "log.txt"

os.makedirs(ARCHIVE_DIR, exist_ok=True)

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")

def load_history():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)

def pinterest_login_and_scrape(save_dir="pinterest_images", limit=15):
    os.makedirs(save_dir, exist_ok=True)
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.pinterest.com/login/")
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "id")))
    password_input = driver.find_element(By.NAME, "password")
    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)
    password_input.submit()
    time.sleep(5)

    driver.get("https://www.pinterest.com/")
    time.sleep(5)

    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    imgs = driver.find_elements(By.TAG_NAME, "img")
    downloaded = 0
    paths = []
    for img in imgs:
        src = img.get_attribute("src")
        if src and "236x" in src:
            try:
                path = f"{save_dir}/img_{downloaded}.jpg"
                urllib.request.urlretrieve(src, path)
                paths.append(path)
                downloaded += 1
                if downloaded >= limit:
                    break
            except:
                continue

    driver.quit()
    return paths

if __name__ == "__main__":
    scraped = pinterest_login_and_scrape()
    random.shuffle(scraped)

    history = load_history()
    used = set(entry["src"] for entry in history)
    chosen = None

    for path in scraped:
        if path not in used:
            chosen = path
            break

    if chosen:
        update_telegram_pfp(chosen)
        ts = datetime.now().isoformat()
        cropped = crop_with_yolo_or_face([path])
        if cropped:
            chosen = cropped[0]
        log(f"Updated PFP with {chosen}")
        history.append({"timestamp": ts, "src": path, "pfp": chosen})
        save_history(history)
        os.rename(chosen, os.path.join(ARCHIVE_DIR, os.path.basename(chosen)))
    else:
        log("No valid image found for PFP update.")
