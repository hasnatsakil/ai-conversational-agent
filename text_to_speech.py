
from gtts import gTTS
import os

def text_to_speech(text):
    bot_audio_path = "static/audios/bot/bot_audio.mp3"
    # with open(text, 'r') as f:
    #     text = f.read()
    #     f.close()
    myobj = gTTS(text=text, lang='en-in', slow=False)
    myobj.save(bot_audio_path)
    os.system("mpg123 "+bot_audio_path)


# # urser_text_path = "static/texts/audio.txt"
# text = "Hello! Welcome to artificial intelligence reception of the AIMS lab. If you have any query please click on the microphone icon and tell me. I'd love to assist you."
# text_to_speech(text)