import os
from core.downloader import download_video
from core.converter import convert_to_hls

def main():
    # Получаем ссылку от пользователя
    video_url = input("Введите ссылку на YouTube: ").strip()

    print("Скачивание видео...")
    # Скачиваем видео
    video_file, video_dir = download_video(video_url)

    if not video_file:
        print("Не удалось скачать видео.")
        return

    print(f"Видео сохранено: {video_file}")
    # Конвертируем в HLS
    if convert_to_hls(video_file, video_dir):
        # Удаляем исходный MP4
        os.remove(video_file)
        print("MP4 удалён.")
        print(f"HLS готов: {video_dir}/index.m3u8")

if __name__ == "__main__":
    main()