from pytube import YouTube
from pydub import AudioSegment
import os
import requests
from pytube.request import get

# class MyRequest(Request):
#     def __init__(self):
#         super().__init__()
#         self.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#        })

def download_video(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    yt = YouTube(url, on_progress_callback=None)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path='./', filename='temp_audio')
    return 'temp_audio'

def convert_to_mp3(input_file):
    audio = AudioSegment.from_file(input_file)
    mp3_filename = input_file.split('.')[0] + '.mp3'
    audio.export(mp3_filename, format='mp3')
    return mp3_filename

def main():
    url = input("[!] Enter YouTube video URL: ")
    print("[-] Downloading video...")
    downloaded_file = download_video(url)
    print(f"[V] Downloaded temporarily to {downloaded_file}")
    print(f"[-] Converting to MP3...")
    mp3_file = convert_to_mp3(downloaded_file)
    print(f"[V] MP3 file succesfully saved as {mp3_file}")
    print(f"[-] Removing temp file: {downloaded_file}")
    os.remove(downloaded_file)

if __name__ == "__main__":
    main()