import os
import re
from yt_dlp import YoutubeDL
from .config import BASE_OUTPUT_DIR

def safe_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_video(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": False,
    }
    # Получаем информацию о видео
    with YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(url, download=False)

    title = safe_filename(info["title"])

    video_dir = os.path.join(BASE_OUTPUT_DIR, title)
    os.makedirs(video_dir, exist_ok=True)

    ydl_opts["outtmpl"] = os.path.join(video_dir, "%(title)s.%(ext)s")

    # Скачиваем видео
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Ищем скачанный mp4
    for file in os.listdir(video_dir):
        if file.endswith(".mp4"):
            return os.path.join(video_dir, file), video_dir
        
    return None, None