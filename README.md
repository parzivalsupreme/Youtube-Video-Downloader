# Youtube-Video-Downloader

This is a simple Python program that allows users to download YouTube videos by entering the URL of the video. The program also includes a text-to-speech feature that speaks messages to the user.

### Prerequisites
- Python 3.x
- pytube library: ```pip install pytube```
- pyttsx3 library: ```pip install pyttsx3```

### How to Use

1. Run the program using ```python yt_downloader.py```
2. Enter the URL of the YouTube video you want to download when prompted.
3. The video will begin downloading, and a message will be spoken to confirm the download.

### Troubleshooting

If an error occurs during the download process, an error message will be printed and spoken to the user. Make sure that you have entered a valid URL and that you have an active internet connection.

### Notes

- The program will automatically download the highest resolution version of the video available.
- The text-to-speech feature uses the default voice of your system. If you want to change the voice, you can modify the ```voices[1].id``` in the code to use a different available voice.
