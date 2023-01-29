from pytube import YouTube
import os
from pytube import Playlist


def playlist_downloader(link):
    """
    Downloads a playlist from YouTube or YouTube Music
    :param link: link of the playlist
    :return: None, only downloads the playlist in ./music directory and printing confirmation message
    """
    playlist = Playlist(link)

    for video in playlist.videos:
        stream = video.streams.filter(only_audio=True).first()


        out_file = stream.download('./music')


        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


        print(stream.title + " has been downloaded successfully")


def song_downloader(link):
    """
    Downloads a single song from YouTube or YouTube Music
    :param link: link of the song
    :return: None, only downloads the song in ./music directory and printing confirmation message
    """
    video = link.streams.filter(only_audio=True).first()
    
    
    out_file = video.download("./music")
    
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    
    print(link.title + " has been downloaded successfully.")






if __name__ == "__main__":
    """
    Checks if user wants to download a playlist or a single song and evokes right function
    """
    check = str(input("Do you want to download a playlist or one song? (p/o) "))
    if check == "p":
        playlist_downloader(str(input("Enter the playlist link: ")))
    elif check == "o":
        song_downloader(str(input("Enter the song link: ")))
    else:
        print("Invalid input")