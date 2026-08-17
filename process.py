from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

# قراءة بيانات الـ Secret من بيئة العمل
creds_json = os.environ.get("YOUTUBE_CREDENTIALS")
creds_dict = json.loads(creds_json)

# اعتماد حساب الخدمة بالشكل الصحيح
credentials = service_account.Credentials.from_service_account_info(
    creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

# بناء اتصال يوتيوب
youtube = build("youtube", "v3", credentials=credentials)
