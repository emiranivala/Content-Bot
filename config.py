# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "22642292")
API_HASH = os.getenv("API_HASH", "4502d35191a2fcb02c8467f54789f0ea")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB = os.getenv("MONGO_DB", "")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "922270982").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002493565037")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002329264016")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", None) # for session encryption
IV_KEY = os.getenv("IV_KEY", None) # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", None)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", None)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "50000000000000000000000000000000000"))
