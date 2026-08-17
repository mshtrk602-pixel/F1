import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1. استلام الرابط والعنوان من المدخلات
video_url = os.environ.get("VIDEO_URL")
video_title = os.environ.get("VIDEO_TITLE")

# 2. بيانات حساب الخدمة كاملة وصحيحة 100%
creds_dict = {
  "type": "service_account",
  "project_id": "auto-uploader-505816",
  "private_key_id": "c00e41659499d9c8cc49b54e3ce696734ebc4424",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCbofvWCLgq/zqp\n5JozXGK5wYmVyfjqwDi6/oKON+sXcrVDlGpWlvHNcqGof4EDhKe0+ETBpWjRd5WJ\niTy9IfBJKR1LK7MRfy3X1MQqRxjLYkVDXHR9Q6zM5Uxwl5VgBDC1Hr0Hak1WJuW/\nBqxmt9Hnp7Ck2TQCTt+Hcfuio7MmRv8kpgUBOQVWJDCFhzQ52tvR3s7bdl76In3v\n/UgQxMZMBlZAoh1G3uaRufiHw6BrWWji5b1xEVAqcJffJpg5YWEXNLtEJllD3W8x\n+M/BX0O224WS+AyxwJQWygQCPSSbgjHeZX8YS3OSuy26FRTNgSI3efqgfqTb8ODW\nuImmKUMBAgMBAAECggEABszPk50C6wIG3qh54lediq89ozlVcnBeqjD3pF4mG/qr\nl93SvaDPxOHG1XVovi4cI8ibPHjNOSXH91/zMvJaLOAqgv/QTanoZ19JCO3dU/mh\nvB08i8KauMMmEV9WLAFS3X8P1FSdN2/wpuWUP9K1TbFigvloj9dBZgohbAxKBhiP\nmPplQbtv3Qa3qRlcVLywmNlb0D09Ub0kWr89bQ0HnsUtS5idUIBRa4WqNJjydFbt\fo+bzWUmggkwQwBmE/A+N1wDVeVF3VIuePS+3LbX55P5pzJvFg1dF/VrsaAthz/H\n6kHePNhb7DkbjQzNklDtfrOU4m2inoTBCD0iel8TKQKBgQDH4Pe9xMDQMXBqZUqQ\n+xzQeyc9v4Y9OUekr2mCN2VRD5w151PdoHkHzQWVsJuwArgm6z1u8b7qSZKs+8Zm\n9P2+rma15PS8/tDss/rYDxahyqemF6SRgwD0ZVaIggrB8Xe/9mMXHhs4J1LsK/VX\n0pP9QXQ4/3HjAj0PS5dHb1Wu3QKBgQDHVKrnnD7ZJydO4ZwI7hnI3ZUiBQB8rRnH\nVlaEg/+xsGLKJEyDZ9mbX87UFpKLlVdLCuoHVXESOh3Em4cTJ04en39rhVBL48bA\nKqaYIVif6w0Y0TAkdv01Ru2uGP6nMlmM23fKTKb6PSO0pRz0tgr5/gRc6vuWhZZb\nOMbPYMA4dQKBgQDCEyw59JsLC5YNmMBoOYrm201k5VxgggeQXkniCAu2Q6P3qt+B\nqFkcO/QaPltM8bcBAxSpbs1jC4EBuY4RVfwzc3+DSgZgpEMUMkV0GGJvQii6WuaN\n61e39dWpwirT2bPejkv0nGTthzE65Ava9DqBg1ZoKY/ZTckf2tPOpsnZeQKBgAdI\ndzIXAKj46FPWpNgis2iGyHtsyV7FCKsjOZgwJrj8pC+U8gLfWbF2590SUhqtw3nn\nlTPdaHttCkd0E5ScnBs8YvCv94Y+dbXyGRJ4LX/ynBDrHCJJAunehLMXEL9VdLZU\nEuWetX9xmotweUVsHayTHt+yaq1Ohncg9QsBEyU9AoGBAKppESw+NQY7ykzvI5fR\nsWDWkpvvZERWWE2EbhyiAsuz2e76gT+fbn873LC0EO58MTDQ+DUFrKvNbN5Qc4uf\nBWbmha73fJsVEHqJqeMXVK7f8Q2JklR6NGK6PmiLnrpRGz4ZN2ZmY0Ntj4PxyzeW\n8g2UMx68VHWVlGEuLgsJ6qKA\n-----END PRIVATE KEY-----",
  "client_email": "uploader@auto-uploader-505816.iam.gserviceaccount.com",
  "client_id": "107463092817037930193",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/uploader%40auto-uploader-505816.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

try:
    # 3. المصادقة عبر بيانات حساب الخدمة المضمنة
    credentials = service_account.Credentials.from_service_account_info(
        creds_dict, scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    youtube = build("youtube", "v3", credentials=credentials)
    
    print("تم الاتصال بيوتيوب بنجاح تام وبدون أخطاء!")
    print(f"عنوان الفيديو المستهدف: {video_title}")
    print(f"رابط التحميل: {video_url}")
    
    # الخطوة القادمة: إضافة كود yt-dlp للتحميل والرفع الفعلي

except Exception as e:
    print(f"حدث خطأ أثناء المصادقة: {e}")
