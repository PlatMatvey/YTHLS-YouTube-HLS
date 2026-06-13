import os
from downloader import download_video
from converter import convert_to_hls

def main():
    # Целевая ссылка на YouTube
    video_url = 'https://youtube.com'
    
    try:
        # 1. Вызываем функцию скачивания из модуля downloader
        downloaded_file, video_folder = download_video(video_url)
        
        # Переименовываем файл в простое имя "temp_video.mp4"
        # Это защищает FFmpeg от падения из-за спецсимволов и пробелов в названии видео
        safe_mp4_path = os.path.join(video_folder, "temp_video.mp4")
        if os.path.exists(downloaded_file):
            os.rename(downloaded_file, safe_mp4_path)
        
        # 2. Вызываем функцию нарезки из модуля converter
        success = convert_to_hls(input_path=safe_mp4_path, output_dir=video_folder)
        
        # 3. Авто-очистка: удаляем временный MP4 файл, если HLS готов
        if success and os.path.exists(safe_mp4_path):
            print("-> Очистка: удаляем исходный MP4 файл для экономии места...")
            os.remove(safe_mp4_path)
            print("-> Исходный MP4 успешно удален. Алгоритм выполнен на 100%!")
            
    except Exception as e:
        print(f"\n[Критическая ошибка в работе алгоритма]: {e}")

if __name__ == "__main__":
    main()