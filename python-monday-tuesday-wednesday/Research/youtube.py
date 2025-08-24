import yt_dlp
#pip install yt-dlp

url = input("Enter YouTube URL: ")
ydl_opts = {"outtmpl": "%(title)s.%(ext)s"}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
