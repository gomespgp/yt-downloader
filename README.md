# YouTube to MP3 Downloader

A simple Python tool to download YouTube videos and convert them into `.mp3` audio files. Supports single video downloads as well as comma-separated batch downloads.

The converted files are automatically saved to your system's personal **Downloads** folder (`~/Downloads`).

---

## Features

- 🎵 **High Quality Audio Extraction**: Extracts the best available audio stream and converts it to MP3 (192 kbps).
- 📦 **Self-Contained FFmpeg**: Automatically sets up `ffmpeg` binaries within the virtual environment, without requiring manual system installation.
- ⚡ **Batch Downloading**: Accepts multiple URLs separated by commas and downloads them sequentially.
- 📂 **Direct to Downloads**: Automatically places `.mp3` files directly into your operating system's `Downloads` directory.

---

## Prerequisites

- **Python 3.10+** installed on your system.
- **Git** (optional, for cloning).

---

## Setup & Installation

1. **Clone the repository** (or download the project files):
   ```bash
   git clone <YOUR_REPO_URL>
   cd yt-download
   ```

2. **Create and activate a virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate.bat
     ```
   - **Linux / macOS / Git Bash**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

You can run the script interactively or pass URLs directly via command-line arguments.

### 1. Interactive Mode
Run the script without arguments:
```bash
python download_mp3.py
```
You will be prompted to enter URL(s):
- **Single URL:**
  ```text
  Enter YouTube URL(s) [separated by comma ',']: https://www.youtube.com/watch?v=dQw4w9WgXcQ
  ```
- **Multiple URLs (comma-separated):**
  ```text
  Enter YouTube URL(s) [separated by comma ',']: https://youtu.be/video1, https://youtu.be/video2, https://youtu.be/video3
  ```

---

### 2. Command Line Arguments

- **Single URL:**
  ```bash
  python download_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  ```

- **Multiple URLs (comma-separated string):**
  ```bash
  python download_mp3.py "https://youtu.be/video1, https://youtu.be/video2"
  ```

- **Multiple URLs (space-separated arguments):**
  ```bash
  python download_mp3.py "https://youtu.be/video1" "https://youtu.be/video2"
  ```

---

## Output Location

All completed MP3 files will be stored in your user's **Downloads** folder:
- **Windows**: `C:\Users\<YourUsername>\Downloads\`
- **macOS / Linux**: `~/Downloads/`
