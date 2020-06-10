import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishTime():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('Shubham plz tell me how may i help you : ')


def takecmd():
    r = sr.Recognizer()
    print("Listning.....")
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said : {query}\n')

    except Exception as e:
        print('say that again')
        return "None"
    return query


if __name__ == '__main__':
    wishTime()
    while True:
        query = takecmd().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", '')
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ")
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'play music' in query:
            music_fol = 'D:\\Audio song\\New song'
            songs = os.listdir(music_fol)
            num = random.randint(1,100)
            os.startfile(os.path.join(music_fol,songs[num]))
        elif 'java by durgasir' in query:
            java_fol= 'E:\\Study content\\Java\\Durga Sir'
            os.fdopen(java_fol)

