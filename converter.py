import os
import subprocess
from config import FFMPEG_EXE

def convert_to_hls(input_path: str, output_dir: str) -> bool:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Файл для конвертации не найден: {input_path}")
        
    output_playlist = os.path.join(output_dir, "index.m3u8")
    
    # Команда для FFmpeg на создание HLS-стрима
    command = [
        FFMPEG_EXE,
        "-i", input_path,
        "-c:v", "libx264",        # Видеокодек H.264 (максимальная совместимость в web)
        "-c:a", "aac",            # Аудиокодек AAC
        "-strict", "-2",
        "-hls_time", "10",        # Длина одного сегмента видео (10 секунд)
        "-hls_list_size", "0",     # Индексировать абсолютно все сегменты в один m3u8
        "-f", "hls",              # Целевой формат HLS
        output_playlist
    ]
    
    print('\n[Шаг 2/2] Нарезка в HLS началась...')
    # Запускаем фоновый процесс FFmpeg и ждем его завершения
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print('-> Успешная конвертация! Плейлист index.m3u8 создан.')
        return True
    else:
        print("-> Ошибка FFmpeg:")
        print(result.stderr)
        return False