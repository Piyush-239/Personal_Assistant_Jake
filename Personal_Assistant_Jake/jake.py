import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import pyaudio
import webbrowser
import os
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning! sir")

    elif hour>=12 and hour<18:
        speak("good afternoon! sir")

    else:
        speak("good evening! sir")
    
    speak("Its me Jake, How can i help you")
    print("Try:  hello")

def takeCommand():
    #need microphone input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You say:  {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry to listen you...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #make sure string is in lowecase

        if 'wikipedia' in query:
            speak("Let me search in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 3)#you can adjust sentences i set it to 3.
            speak("According to our knowledge")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackOverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = '' #your folder location with drive inside ''.
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))# 0 here means to start from 1st song

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strTime}")

        elif 'open visual studio' in query:
            codePath = "" #your folder location with drive inside "".
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("Im always great")

        elif 'hello' in query:
            speak("Hello sir.")

        elif 'hello jake' in query:
            speak("Hello sir.")

        elif 'who are you' in query:
            speak("Im an A I, Im here to help you")

        elif 'who is' in query:
            try:
                speak("Take a minute ")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences= 3)
                speak("sir")
                speak(results)
            except Exception as e:
                speak(e)
                speak("Im not able to search that")
        elif 'what is' in query:
            try:
                speak("Let me search")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences= 3)
                speak("Sir")
                speak(results)
            except Exception as e:
                speak(e)
                speak("Im not able to search that")
        elif 'what do' in query:
            try:
                speak("Let me search")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences= 3)
                speak("Sir")
                speak(results)
            except Exception as e:
                speak(e)
                speak("Im not able to search that")
        elif 'quit' in query:
            speak("Thanks for your time! Sir.")
            break
#Thankyou for choosing this , develops by "PIYUSH SHARMA"
        