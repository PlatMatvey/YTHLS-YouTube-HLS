import os
import subprocess
from config import FFMPEG_EXE

def convert_to_hls(input_path: str, output_dir: str):
    """
    Конвертирует видеофайл в HLS-поток.

    Args:
        input_path: Путь к исходному видеофайлу.
        output_dir: Папка для сохранения HLS-файлов.

    Returns:
        True, если конвертация завершилась успешно,
        иначе False.
    """

    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"Файл для конвертации не найден: {input_path}"
        )
    output_playlist = os.path.join(output_dir, "index.m3u8")

    # Создаём HLS-поток с кодеками H.264 и AAC
    # для максимальной совместимости с браузерами.
    command = [
        FFMPEG_EXE,
        "-i", input_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-strict", "-2",
        "-hls_time", "10",
        "-hls_list_size", "0",
        "-f", "hls",
        output_playlist,
    ]
    print("\n[Шаг 2/2] Конвертация видео в HLS...")

    # Запускаем FFmpeg и ожидаем завершения процесса.
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("✓ Конвертация завершена успешно.")
        print(f"✓ Плейлист создан: {output_playlist}")
        return True

    print("✗ Ошибка FFmpeg:")
    print(result.stderr)
    return False