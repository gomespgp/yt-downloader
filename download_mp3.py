import os
import sys
from pathlib import Path
import static_ffmpeg
import yt_dlp

# Automatically add ffmpeg to PATH from within the project virtual environment
static_ffmpeg.add_paths()

# User's personal Downloads folder (e.g. C:\Users\<Username>\Downloads)
USER_DOWNLOADS_DIR = str(Path.home() / "Downloads")

def parse_urls(input_str: str, separator: str = ",") -> list[str]:
    """
    Splits an input string by the specified separator and returns a list of non-empty URLs.
    """
    return [url.strip() for url in input_str.split(separator) if url.strip()]

def download_audio(urls: list[str], output_dir: str = USER_DOWNLOADS_DIR) -> None:
    """
    Downloads audio from a list of YouTube URLs one by one and converts each to MP3.
    Saves directly into the specified output directory.
    """
    if not urls:
        print("No valid URLs to process.")
        return

    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    total = len(urls)
    print(f"\nTarget folder: {output_dir}")
    print(f"Total videos to download: {total}\n" + "=" * 50)

    for index, url in enumerate(urls, start=1):
        print(f"\n[{index}/{total}] Processing: {url}")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"[{index}/{total}] Done!")
        except Exception as e:
            print(f"[{index}/{total}] Failed to download {url}. Error: {e}")

    print("\n" + "=" * 50)
    print(f"All downloads finished! Files saved in: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Check if arguments are passed as separate args or a comma-separated string
        raw_input = " ".join(sys.argv[1:])
        # Support both comma-separated and space-separated if no comma exists
        if "," in raw_input:
            urls = parse_urls(raw_input, separator=",")
        else:
            urls = [arg.strip() for arg in sys.argv[1:] if arg.strip()]
    else:
        raw_input = input("Enter YouTube URL(s) [separated by comma ',']: ").strip()
        urls = parse_urls(raw_input, separator=",")

    if urls:
        download_audio(urls)
    else:
        print("No URLs provided. Exiting.")
