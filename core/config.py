import os

# Путь к FFmpeg
FFMPEG_EXE = "ffmpeg"

# Папка для всех скачанных видео
BASE_OUTPUT_DIR = "./Videos"

# Создаём папку,если она ещё не существует.
os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)