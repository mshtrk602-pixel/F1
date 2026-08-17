import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1. جلب البيانات من Secrets والمدخلات
client_email = os.environ.get("YOUTUBE_CLIENT_EMAIL")
private_key = os.environ.get("YOUTUBE_PRIVATE_KEY")
video_url = os.environ.get("VIDEO_URL")
video_title = os.environ.get("VIDEO_TITLE")

# 2. معالجة المفتاح ليكون بتنسيق صحيح (مهم جداً)
if private_key:
    private_key = private_key.replace("\\n", "\n")

# 3. بناء الاعتمادات
creds_dict = {
    "type": "service_account",
    "project_id": "auto-uploader-505816",
    "private_key_id": "c00e41659499d9c8cc49b54e3ce696734ebc4424",
    "private_key": private_key,
    "client_email": client_email,
    "token_uri": "https://oauth2.googleapis.com/token",
}

try:
    credentials = service_account.Credentials.from_service_account_info(
        creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    youtube = build("youtube", "v3", credentials=credentials)
    
    print(f"تم الاتصال بنجاح!")
    print(f"جاري معالجة الفيديو: {video_title}")
    print(f"الرابط: {video_url}")
    
    # هنا سيأتي لاحقاً كود yt-dlp للتحميل وكود youtube للرفع

except Exception as e:
    print(f"خطأ في المصادقة: {e}")
