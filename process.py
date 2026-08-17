import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1. جلب البيانات من متغيرات البيئة التي حددناها في الـ GitHub Secrets
client_email = os.environ.get("YOUTUBE_CLIENT_EMAIL")
private_key = os.environ.get("YOUTUBE_PRIVATE_KEY")

# 2. تصحيح تنسيق المفتاح (استبدال الرموز الخاصة وإضافة السطور)
if private_key:
    # إزالة أي علامات اقتباس إضافية وتصحيح الـ newline
    private_key = private_key.replace("\\n", "\n").strip('"')

# 3. بناء قاموس الاعتمادات (Credentials)
creds_dict = {
    "type": "service_account",
    "project_id": "auto-uploader-505816",
    "private_key_id": "c00e41659499d9c8cc49b54e3ce696734ebc4424",
    "private_key": private_key,
    "client_email": client_email,
    "token_uri": "https://oauth2.googleapis.com/token",
}

# 4. المصادقة والاتصال بخدمة يوتيوب
try:
    credentials = service_account.Credentials.from_service_account_info(
        creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    youtube = build("youtube", "v3", credentials=credentials)
    print("تم الاتصال بنجاح بواسطة حساب الخدمة!")
    
    # هنا ضع الكود الخاص بك لرفع الفيديو أو العمليات التي تريد تنفيذها
    # مثال: youtube.videos().insert(...).execute()

except Exception as e:
    print(f"حدث خطأ أثناء المصادقة: {e}")
