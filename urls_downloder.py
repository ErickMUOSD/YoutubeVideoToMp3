import os
from dotenv import load_dotenv
from yt_dlp import YoutubeDL
from utils import MyLogger, my_hook

load_dotenv()
print(os.getenv('FILE_DESTINATION'))
with open(os.getenv('FILE_DESTINATION', 'clipboard.txt')) as f:
    lines = f.readlines()
ydl_options = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'noplaylist': True,
    'format': 'bestaudio',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
    }],
    'paths': {
        'home': os.getenv('AUDIO_DESTINATION')
    }
}
with YoutubeDL(ydl_options) as ydl:
    ydl.download(lines)
