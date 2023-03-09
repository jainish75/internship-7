from gtts import gTTS
import os

text = "hello everyone"
language = 'en'
output = gTTS(text = text, lang = language, slow = False)
output.save("voice.mp3")



os.system("start voice3.mp3")


