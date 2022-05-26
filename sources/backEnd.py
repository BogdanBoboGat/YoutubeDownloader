from pytube import YouTube
import requests

def checkNetwork():
    url = "http://google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

# get title and length
def videoInfo(URL):
    ytb = YouTube(URL)
    return ytb.title, ytb.length

# check URL
def checkVideoURL(URL):
    return 'youtube' in URL or 'youtu.be' in URL 

# download URL
def downloadURL(URL, audio, video):
    yt_video = YouTube(URL)

    if video and not audio:
        videoURL = yt_video.streams.get_highest_resolution()
        videoURL.download('../Downloads/')
    
    elif audio and not video:
        audioURL = yt_video.streams.filter(only_audio=True)
        audioURL[0].download('../Downloads/')
