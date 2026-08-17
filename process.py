from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# قراءة البيانات مباشرة من المتغيرات المنفصلة
client_email = os.environ.get("YOUTUBE_CLIENT_EMAIL")
private_key = os.environ.get("YOUTUBE_PRIVATE_KEY")

# التأكد من صحة استبدال الأسطر الجديدة في المفتاح
if private_key:
    private_key = private_key.replace("\\n", "\n")

# بناء هيكل الاعتماديات لحساب الخدمة
creds_dict = {
    "type": "service_account",
    "project_id": "auto-uploader-505816",
    "private_key_id": "c00e41659499d9c8cc49b54e3ce696734ebc4424",
    "private_key": private_key,
    "client_email": client_email,
    "token_uri": "https://oauth2.googleapis.com/token",
}

credentials = service_account.Credentials.from_service_account_info(
    creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

# بناء اتصال يوتيوب
youtube = build("youtube", "v3", credentials=credentials)
print("تم الاتصال بيوتيوب بنجاح تام عبر حساب الخدمة!")
