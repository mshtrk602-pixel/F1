from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

# قراءة الـ Secret وإصلاح صيغة المفتاح الخاص تلقائياً
creds_json = os.environ.get("YOUTUBE_CREDENTIALS")
creds_dict = json.loads(creds_json)

# التأكد من تحويل الـ \n النصية إلى أسطر حقيقية للمفتاح
if "private_key" in creds_dict:
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")

credentials = service_account.Credentials.from_service_account_info(
    creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

youtube = build("youtube", "v3", credentials=credentials)
