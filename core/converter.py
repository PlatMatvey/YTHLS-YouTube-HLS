import os
import subprocess
from .config import FFMPEG_EXE

def convert_to_hls(input_path, output_dir):
    if not os.path.exists(input_path):
        print("Файл не найден.")
        return False

    playlist = os.path.join(output_dir, "index.m3u8")

    command = [
        FFMPEG_EXE,
        "-i", input_path,           # Входной MP4-файл
        "-c:v", "libx264",          # Кодек видео H.264
        "-c:a", "aac",              # Кодек аудио AAC
        "-hls_time", "10",          # Длина сегмента
        "-hls_list_size", "0",      # Все сегменты в плейлисте
        "-f", "hls",                # Формат HLS
        playlist,
    ]

    print("Начинается конвертация в HLS...")
    
    result = subprocess.run(command)

    if result.returncode == 0:
        print("Конвертация завершена.")
        return True

    print("Ошибка конвертации.")
    return False