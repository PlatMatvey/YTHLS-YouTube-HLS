import os

# На Linux FFmpeg вызывается глобальной системной командой
FFMPEG_EXE = "ffmpeg"

# Корневая папка для хранения твоей медиатеки
BASE_OUTPUT_DIR = "./Videos"

# Создаём папку,если она ещё не существует.
os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)