from pytube import YouTube
import pyttsx3


print("🔴Youtube Video Downloader🔴")
print("")


engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
VoiceGender = engine.setProperty('voice', voices[1].id)

def speak(texttospeech):
    engine.say(texttospeech)
    engine.runAndWait()


def I_wish_to_have_a_female_friend():
    
 while True:
    
    try:
        url = input("YouTube URL: ")
        youtube_video = YouTube(url)
        youtube_video = youtube_video.streams.get_highest_resolution()
        youtube_video.download()
        print("Download Success!")
        speak("download sucess!")
        
    except:
        print("Error!")
        speak("error!")


I_wish_to_have_a_female_friend()