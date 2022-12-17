#imports
from pytube import YouTube
import pyttsx3

#Print a welcome message
print("🔴Youtube Video Downloader🔴")
print("")

#Initialize the text-to-speech engine
engine = pyttsx3.init ('sapi5')
#Get the available voices
voices = engine.getProperty('voices')
#Set the voice to the second available voice
VoiceGender = engine.setProperty('voice', voices[1].id)

#Function to speak the given text
def speak(texttospeech):
    engine.say(texttospeech)
    engine.runAndWait()

#Function to download the YouTube video
def yt():
    
#Loop indefinitely
 while True:
    
    try:
        #Get the YouTube URL from the user
        url = input("YouTube URL: ")
        #Create a YouTube object using the URL
        youtube_video = YouTube(url)
        #Get the highest resolution stream available
        youtube_video = youtube_video.streams.get_highest_resolution()
        #Download the video
        youtube_video.download()
        print("Download Success!")
        speak("download sucess!")
    #If an error occurs  
    except:
        print("Error!")
        speak("error!")

#Call the yt function to start the program
yt()