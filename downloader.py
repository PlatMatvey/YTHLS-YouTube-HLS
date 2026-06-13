import os
from yt_dlp import YoutubeDL
from config import BASE_OUTPUT_DIR

def download_video(url: str) -> tuple[str, str]:
    print(f"\n[Шаг 1/2] Подключение к YouTube -> {url}")
    
    # Исключаем ТВ-клиенты, чтобы YouTube не присылал потоки с DRM защитой (Widevine)
    youtube_bypass_args = {
        'youtube': {
            'player_client': ['web', 'android', 'ios'],
            'skip': ['webpage']
        }
    }
    
    # Настройки для предварительного анализа видео
    ydl_opts_info = {
        'noplaylist': True,
        'force_ipv4': True,
        'extractor_args': youtube_bypass_args,
        'load_pages': True,
        # Динамически загружаем рабочий JS-компонент с GitHub для решения n-challenge
        'remote_components': 'ejs:github',
    }
    
    # Считываем метаданные видео без скачивания, чтобы узнать оригинальное название
    with YoutubeDL(ydl_opts_info) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = info.get('title', 'Untitled_Video')
        # Очищаем название от запрещенных символов файловой системы Linux
        safe_title = "".join([c for c in video_title if c.isalpha() or c.isdigit() or c in ' ._-']).rstrip()

    # Создаем уникальную изолированную папку для конкретно этого видео
    video_dir = os.path.join(BASE_OUTPUT_DIR, safe_title)
    os.makedirs(video_dir, exist_ok=True)
    
    # Настройки для реального скачивания аудио и видео потоков
    ydl_opts = {
        # Запрашиваем раздельные потоки FullHD видео и лучшего аудио для стабильности обхода
        'format': 'bestvideo[height<=1080]+bestaudio/best', 
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'outtmpl': os.path.join(video_dir, '%(title)s [%(id)s].%(ext)s'),
        'force_ipv4': True,
        'extractor_args': youtube_bypass_args,
        'remote_components': 'ejs:github',
    }
    
    # Скачиваем потоки и автоматически склеиваем их через системный FFmpeg в MP4
    with YoutubeDL(ydl_opts) as ydl:
        real_info = ydl.extract_info(url, download=True)
        downloaded_mp4 = ydl.prepare_filename(real_info)
        
    print(f"-> Video успешно скачано в: {downloaded_mp4}")
    return downloaded_mp4, video_dir