from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

# قراءة الـ Credentials من الـ Environment Variable (GitHub Secret)
creds_json = os.environ.get("YOUTUBE_CREDENTIALS")
creds_dict = json.loads(creds_json)

# استخدام حساب الخدمة (Service Account)
credentials = service_account.Credentials.from_service_account_info(
    creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

# بناء اتصال يوتيوب
youtube = build("youtube", "v3", credentials=credentials)
