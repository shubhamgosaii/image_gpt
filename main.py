import os
import subprocess
from datetime import datetime
from PIL import Image

from wish.wish import speak, wish
from voiceinp.voiceinp import voiceinp
from ai.ai import imgai

def print_image_in_terminal():
    if os.path.exists("image.png"):
        subprocess.run(["catimg", "image.png"])   # prints the image
        os.remove("image.png")

if __name__ == '__main__':

    wish()  # greet once

    while True:
        x = datetime.now()
        t = x.strftime('%I:%M:%p')
        y = x.year
        d = x.strftime('%A')

        print(t, y)
        print(d)

        query = voiceinp().lower()

        if query == "":
            continue

        if "exit" in query or "stop" in query:
            speak("Okay sir, shutting down")
            break

        if "generate" in query or "image" in query or "photo" in query:
            speak("Generating image sir")

            imgai(query)          # generate image
            print_image_in_terminal()  # print in terminal

        else:
            speak("You said")
            speak(query)
