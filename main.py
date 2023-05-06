from __future__ import unicode_literals
import youtube_dl
import sys

link = sys.argv[1]

ydl_options = {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]}
with youtube_dl.YoutubeDL(ydl_options) as ydl:
    try:
        ydl.download([link])
    except:
        print("error. Try again")