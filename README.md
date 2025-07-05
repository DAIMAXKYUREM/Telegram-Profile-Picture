# Pinterest to Telegram PFP Automation 🔄🖼️

Automatically scrapes anime profile pictures from Pinterest, processes them with YOLOv5 for cropping, and updates your Telegram profile picture.

---

## 🚀 Features

- Scrapes Pinterest for anime-themed profile pictures
- Uses custom-trained YOLOv5 to crop faces
- Falls back to face detection if YOLO fails
- Automatically updates Telegram PFP every 12 hours
- Saves logs and history of updates

---

## 📁 Project Structure
imagescrape/
│
├── pinterest.py # Scraper for Pinterest images
├── gen_session.py # Generates Telegram session
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

3. Run the Scraper and Updater:
python imagescrape/pinterest.py

🔁 Automate with Cron (Linux):
To run every 12 hours:
0 */12 * * * /usr/bin/python /path/to/pinterest.py

🧠 Model Info
Custom YOLOv11n model trained to detect anime PFPs





