import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "23147459"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "7ea3e357441507277e33bd1f7c6d8847")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "6574945123"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "6574945123").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://ryme786:ryme@786@cluster0.ugx0zos.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002871886693"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002753598393")  # Optional here you'll get all logs
