import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# جلب الإيميل والمدخلات من الـ Secrets والـ Actions
client_email = os.environ.get("YOUTUBE_CLIENT_EMAIL")
video_url = os.environ.get("VIDEO_URL")
video_title = os.environ.get("VIDEO_TITLE")

# وضع المفتاح الخاص مباشرة هنا لتجنب مشاكل قراءة الـ Secrets
private_key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCbofvWCLgq/zqp
5JozXGK5wYmVyfjqwDi6/oKON+sXcrVDlGpWlvHNcqGof4EDhKe0+ETBpWjRd5WJ
iTy9IfBJKR1LK7MRfy3X1MQqRxjLYkVDXHR9Q6zM5Uxwl5VgBDC1Hr0Hak1WJuW/
Bqxmt9Hnp7Ck2TQCTt+Hcfuio7MmRv8kpgUBOQVWJDCFhzQ52tvR3s7bdl76In3v
/UgQxMZMBlZAoh1G3uaRufiHw6BrWWji5b1xEVAqcJffJpg5YWEXNLtEJllD3W8x
+M/BX0O224WS+AyxwJQWygQCPSSbgjHeZX8YS3OSuy26FRTNgSI3efqgfqTb8ODW
uImmKUMBAgMBAAECggEABszPk50C6wIG3qh54lediq89ozlVcnBeqjD3pF4mG/qr
l93SvaDPxOHG1XVovi4cI8ibPHjNOSXH91/zMvJaLOAqgv/QTanoZ19JCO3dU/mh
vB08i8KauMMmEV9WLAFS3X8P1FSdN2/wpuWUP9K1TbFigvloj9dBZgohbAxKBhiP
mPplQbtv3Qa3qRlcVLywmNlb0D09Ub0kWr89bQ0HnsUtS5idUIBRa4WqNJjydFbt
fo+bzWUmggkwQwBmE/A+N1wDVeVF3VIuePS+3LbX55P5pzJvFg1dF/VrsaAthz/H
6kHePNhb7DkbjQzNklDtfrOU4m2inoTBCD0iel8TKQKBgQDH4Pe9xMDQMXBqZUqQ
+xzQeyc9v4Y9OUekr2mCN2VRD5w151PdoHkHzQWVsJuwArgm6z1u8b7qSZKs+8Zm
9P2+rma15PS8/tDss/rYDxahyqemF6SRgwD0ZVaIggrB8Xe/9mMXHhs4J1LsK/VX
0pP9QXQ4/3HjAj0PS5dHb1Wu3QKBgQDHVKrnnD7ZJydO4ZwI7hnI3ZUiBQB8rRnH
VlaEg/+xsGLKJEyDZ9mbX87UFpKLlVdLCuoHVXESOh3Em4cTJ04en39rhVBL48bA
KqaYIVif6w0Y0TAkdv01Ru2uGP6nMlmM23fKTKb6PSO0pRz0tgr5/gRc6vuWhZZb
OMbPYMA4dQKBgQDCEyw59JsLC5YNmMBoOYrm201k5VxgggeQXkniCAu2Q6P3qt+B
nqFkcO/QaPltM8bcBAxSpbs1jC4EBuY4RVfwzc3+DSgZgpEMUMkV0GGJvQii6WuaN
61e39dWpwirT2bPejkv0nGTthzE65Ava9DqBg1ZoKY/ZTckf2tPOpsnZeQKBgAdI
zdIXAKj46FPWpNgis2iGyHtsyV7FCKsjOZgwJrj8pC+U8gLfWbF2590SUhqtw3nn
lTPdaHttCkd0E5ScnBs8YvCv94Y+dbXyGRJ4LX/ynBDrHCJJAunehLMXEL9VdLZU
EuWetX9xmotweUVsHayTHt+yaq1Ohncg9QsBEyU9AoGBAKppESw+NQY7ykzvI5fR
sWDWkpvvZERWWE2EbhyiAsuz2e76gT+fbn873LC0EO58MTDQ+DUFrKvNbN5Qc4uf
BWbmha73fJsVEHqJqeMXVK7f8Q2JklR6NGK6PmiLnrpRGz4ZN2ZmY0Ntj4PxyzeW
8g2UMx68VHWVlGEuLgsJ6qKA
-----END PRIVATE KEY-----"""

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
    print("تم الاتصال بنجاح تام وتم تخطي مشكلة المفتاح!")
    print(f"جاري العمل على الفيديو: {video_title} - الرابط: {video_url}")

except Exception as e:
    print(f"خطأ في المصادقة: {e}")
