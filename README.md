# YouTube to HLS Converter 🎬

A simple Python script that downloads a YouTube video and automatically converts it into an HLS stream (`.m3u8` playlist and `.ts` segments).

Perfect for personal media servers, video streaming projects, or learning how HLS works.

## Features

* Downloads videos from YouTube using `yt-dlp`
* Creates a separate folder for each video
* Uses safe filenames to avoid FFmpeg and filesystem issues
* Converts videos to HLS format (`.m3u8` + `.ts`)
* Automatically removes the temporary MP4 file after conversion

## Project Structure

```text
core/
├── config.py      # Project configuration
├── downloader.py  # YouTube downloader
└── converter.py   # HLS converter

main.py            # Entry point
```

## Requirements

Install FFmpeg:

```bash
sudo apt update
sudo apt install ffmpeg -y
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -U "yt-dlp[default]" curl-cffi websockets
```

## Usage

Open `main.py` and set your video URL:

```python
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"
```

Run the script:

```bash
python3 main.py
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
