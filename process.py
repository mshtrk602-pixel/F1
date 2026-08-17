import os
import json
import subprocess
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# 1. تنزيل الفيديو
video_url = os.environ.get("VIDEO_URL")
video_title = os.environ.get("VIDEO_TITLE", "Uploaded Video")
output_file = "downloaded_video.mp4"

print(f"جاري تنزيل الفيديو من: {video_url}")
subprocess.run(["yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", "-o", output_file, video_url], check=True)

# 2. إعداد الاتصال بـ YouTube API
creds_raw = os.environ.get("YOUTUBE_CREDENTIALS")
creds_json = json.loads(creds_raw)
creds = Credentials.from_authorized_user_info(creds_json)
youtube = build("youtube", "v3", credentials=creds)

# 3. رفع الفيديو إلى القناة
body = {
    "snippet": {
        "title": video_title,
        "description": "تم الرفع تلقائياً بواسطة نظام الأتمتة.",
        "categoryId": "20"
    },
    "status": {
        "privacyStatus": "public"
    }
}

media = MediaFileUpload(output_file, chunksize=-1, resumable=True)
print("جاري رفع الفيديو إلى يوتيوب...")
request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
response = request.execute()

print(f"تم الرفع بنجاح! معرف الفيديو: {response.get('id')}")

