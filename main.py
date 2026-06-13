import os
from core.converter import convert_to_hls
from core.downloader import download_video


def main() -> None:
    """Основной сценарий загрузки и конвертации видео."""
    # Ваша ссылка на YouTube
    video_url = "https://youtube.com"

    try:
        # Скачиваем видео и получаем путь к рабочей папке.
        downloaded_file, video_folder = download_video(video_url)

        # Используем простое имя файла, чтобы избежать проблем
        # со спецсимволами в названиях видео.
        safe_mp4_path = os.path.join(video_folder, "temp_video.mp4")

        if os.path.exists(downloaded_file):
            os.rename(downloaded_file, safe_mp4_path)

        # Конвертируем MP4 в HLS.
        success = convert_to_hls(
            input_path=safe_mp4_path,
            output_dir=video_folder,
        )

        # После успешной конвертации удаляем исходный файл.
        if success and os.path.exists(safe_mp4_path):
            print("-> Удаление временного MP4 файла...")
            os.remove(safe_mp4_path)
            print("✓ Обработка завершена успешно.")

    except Exception as error:
        print(f"\n[Критическая ошибка]: {error}")

if __name__ == "__main__":
    main()