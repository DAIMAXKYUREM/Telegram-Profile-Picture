# Pinterest to Telegram PFP Automation 🔄🖼️

Automatically profile pictures from ur Pinterest feed, processes them with YOLOv11n for cropping, and updates your Telegram profile picture.

---

## 🚀 Features

- Scrapes Pinterest for profile pictures
- Uses custom-trained YOLOv11n to crop faces
- Falls back to face detection if YOLO fails
- Auto-generates the required Telegram session on first run.
- Saves logs and history of updates

---

## 📁 Project Structure
imagescrape/

│

├── pinterest.py # Scraper for Pinterest images

├── model.pt # Main image filtering model

├── log.txt # Log of PFP update activity

├── history.json # History of updated images

├── myprofile.session # Telegram session file (DO NOT SHARE)

│
├── pinterest_images/ # Folder where scraped images are saved

│ ├── img_0.jpg

│ └── ...

│

├── utils/

│ ├── crop_utils.py # YOLOv5 + face detection logic

│ └── telegram_updater.py # Updates Telegram profile picture

│

└── requirements.txt


---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DAIMAXKYUREM/Telegram-Profile-Picture.git
cd Telegram-Profile-Picture

2. Install Dependencies:
pip install -r requirements.txt

3.Set your Telegram credentials in .env:
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=+1234567890

4. Run the Scraper and Updater:
python imagescrape/pinterest.py

🔁 Automate with Cron (Linux):
To run every 12 hours:
0 */12 * * * /usr/bin/python /path/to/pinterest.py

🧠 Model Info
Custom YOLOv11n model trained to detect anime PFPs





