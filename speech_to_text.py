import speech_recognition as sr


def speech_to_text():
    urser_audio_path = "static/audios/user/audio.wav"
    urser_text_path = "static/texts/audio.txt"

    r = sr.Recognizer()
    with sr.Microphone() as source:
    # with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        r.adjust_for_ambient_noise(source)
        
        try:
            print("Please say your query...")
            audio = r.listen(source = source, timeout=3,phrase_time_limit=10)
            print("Recognizing Now .... ")
            text  = r.recognize_google(audio_data = audio,language='en', with_confidence= True, show_all=False)
            # print(text)
            # print("Audio Recorded Successfully \n ")

            # write audio
            with open(urser_audio_path, "wb") as f:
                f.write(audio.get_wav_data())

            #Write text
            with open(urser_text_path, "w") as f:
                f.write(text[0])
                f.close()
            return text[0]

        except:
            # print("Error :  " + str(e))
            # "static/audios/exception/tell_me_again.txt"
            exception_text = "I could not hear you perfectly. Could you please tell me your query again?"
            #Write text
            with open(urser_text_path, "w") as f:
                f.write(exception_text)
                f.close()
            return exception_text


# if __name__ == "__main__":
#     speech_to_text()