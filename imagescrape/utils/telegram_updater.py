import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest

load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")

def update_telegram_pfp(image_path):
    with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        client(UploadProfilePhotoRequest(
            file=client.upload_file(image_path)
        ))
