# YouTube to HLS Converter 🎬

A lightweight Python application that downloads YouTube videos and converts them into HLS streams (`.m3u8` playlists and `.ts` segments) using FFmpeg.

Perfect for personal media servers, streaming projects, or learning how HLS works.

## Features

* Download videos from YouTube using `yt-dlp`
* Create a separate folder for each video
* Generate safe filenames to avoid filesystem issues
* Convert videos to HLS format (`.m3u8` + `.ts`)
* Automatically remove temporary MP4 files after conversion
* Simple and clean project structure

## Project Structure

```text
project/
│
├── main.py
│
└── core/
    ├── config.py
    ├── downloader.py
    └── converter.py
```

## Requirements

* Python 3.10+
* FFmpeg

### Install FFmpeg (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg -y
```

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -U "yt-dlp[default]" curl-cffi websockets
```

## Usage

Run the application:

```bash
python3 main.py
```

Paste a YouTube URL when prompted:

```text
Enter YouTube URL:
```

## Output

After processing, the generated files will be stored in:

```text
Videos/
└── Video Title/
    ├── index.m3u8
    ├── index0.ts
    ├── index1.ts
    └── ...
```

## Technologies

* Python
* yt-dlp
* FFmpeg
* HLS (HTTP Live Streaming)

## Disclaimer

This project is intended for educational purposes only.

Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws.