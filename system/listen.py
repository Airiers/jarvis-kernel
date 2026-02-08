import speech_recognition as sr
from system.voice import speak
from datetime import datetime
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

with_micro = False # ! CHANGE TO TRUE

def take_user_input():
    if with_micro:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='fr-fr')
        except Exception:
            speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
    else:
        query = input("Command: ")
    if not 'exit' in query or 'stop' in query:
        speak(query)
    else:
        hour = datetime.now().hour
        if hour >= 21 and hour < 6:
            speak(f'Bonne nuit {USERNAME}, reposez-vous bien !')
        else:
            speak(f'Bonne journée {USERNAME}')
        exit()
