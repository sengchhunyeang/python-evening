import yt_dlp
#pip install yt-dlp

url = input("Enter YouTube URL: ")
ydl_opts = {"outtmpl": "%(title)s.%(ext)s"}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


# # Import the yt_dlp library (must be installed with: pip install yt-dlp)
# import yt_dlp
#
# # Ask the user to enter a YouTube video URL
# url = input("Enter YouTube URL: ")
#
# # Options for yt_dlp
# # "outtmpl" defines the output file name format.
# # "%(title)s" → will use the video title as the file name
# # "%(ext)s" → will use the proper extension (e.g. .mp4, .webm)
# ydl_opts = {"outtmpl": "%(title)s.%(ext)s"}
#
# # Create a YouTubeDL object with the given options
# # 'with' ensures resources are properly managed
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     # Download the video from the provided URL
#     # The URL must be passed as a list (so multiple links could be downloaded)
#     ydl.download([url])
