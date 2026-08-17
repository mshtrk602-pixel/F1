from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

# قراءة الـ Secret وتحويله إلى قاموس
creds_json = os.environ.get("YOUTUBE_CREDENTIALS")
creds_dict = json.loads(creds_json)

# إصلاح الأسطر الخاصة بالمفتاح الخاص لضمان عدم حدوث خطأ Invalid private key
private_key = creds_dict.get("private_key", "")
if "\\n" in private_key and "\n" not in private_key:
    private_key = private_key.replace("\\n", "\n")
creds_dict["private_key"] = private_key

# إنشاء الاعتماد باستخدام حساب الخدمة
credentials = service_account.Credentials.from_service_account_info(
    creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

# بناء اتصال يوتيوب
youtube = build("youtube", "v3", credentials=credentials)
print("تم الاتصال بيوتيوب بنجاح عبر حساب الخدمة!")
