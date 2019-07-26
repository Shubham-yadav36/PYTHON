import pyttsx3
import datetime
import  speech_recognition as sr

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1],id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour <12:
                speak("Good Morning sir ")
        elif hour >=12 and hour<18:
                speak("Good afternoon Sir")
        else:
                speak("good evening sir")

        speak("I am assistance sir how can help you plz tell me !")

def take_commond():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listning........")
                r.pause_threshold = 1
                audio = r.listen(source)

        try:
                print("Recognizing.....")
                query = r.recognize_google(audio, Language='en-in')
                print(f"User said : (query)\n")

        except Exception as e:
                print(e)

                print("Say that again please...")
                return "none "
        return query

if __name__ == "__main__":
        wishMe()
        take_commond()

