from glob import glob
import os
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.utils import mediainfo

load_dotenv()

files_dir = os.getenv('VIDEO_DESTINATION') # Path where the videos are located
extension_list = '*.opus'
# playlist_songs = [AudioSegment.from_file(opus_files) for opus_files in glob(os.path.join("temp", extension_list))]

for path_song in  glob(os.path.join("temp", extension_list)):
    song = AudioSegment.from_file(path_song)
    mp3_filename = os.path.splitext(os.path.basename(path_song))[0] + '.mp3'
    song.export(files_dir+mp3_filename, format="mp3")
    print(f"Exported {mp3_filename} successfully!")