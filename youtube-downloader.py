
from yt_dlp import YoutubeDL
import time

print("--- Download Youtube Videos ---")
print()

while True:
    type = int(input("Enter the format of the video you want to download (1. mp3 2. mp4 3. exit): "))

    if type == 1:
        url = input("Enter The Video URL: ")
        opts = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        } 
        with YoutubeDL(opts) as ydl:
            ydl.download([url])
            print("Download Completed")
    elif type == 2:
        url = input("Enter The Video URL: ")
        opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "outtmpl": "%(title)s.%(ext)s",
            "merge_output_format": "mp4",
        }
        with YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("Download Completed")
    elif type == 3:
        print("Exiting...")
        time.sleep(1)
        exit()
    else:
        print("Invalid Input")
