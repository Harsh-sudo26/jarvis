import speech_recognition as sr
import pyaudio
import time
import pyttsx3
import wikipedia
import os
import pywhatkit
import pyautogui
import datetime
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wishme():
    hour = int (datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour <=18:
        speak("Good Afternoon")
    else:
        speak("good evening")
    speak("i am jarvis how can i help you sir")
    def takeCmd():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print (" user said : {query}\n")
        except Exception as e:
            print(e)
            print("say that again please...")
            return "none"
        return query
  
    while True:
        query = takeCmd().lower()
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)

            # open youtube 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube sir")

            # what open song 
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            speak("opening whatsapp sir")
            # open goggle 
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google sir")


            # yt song play cmd 
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            # yt control cmd m
        elif 'stop' in query:
                speak('Stopping the video')
                pyautogui.press('m')
        elif 'mute' in query:
                speak('Muting the video')
                pyautogui.press('m')
        elif 'unmute' in query:
                speak('Unmuting the video')
                pyautogui.press('m')
        elif 'volume up' in query:
                speak('Increasing volume')
                pyautogui.press('up')
        elif 'volume down' in query:
                speak('Decreasing volume')
                pyautogui.press('down')
        elif 'full screen' in query:
                speak('Going full screen')
                pyautogui.press('f')
        elif 'exit full screen' in query:
                speak('Exiting full screen')
                pyautogui.press('esc')
        elif 'exit' in query:
                speak('Goodbye!')
                break


    # vs code open
        #elif 'open vscode' in query:


def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    return current_time

        
if __name__== "__main__":
    speak("hello Sir")
    wishme()
    get_current_time()
   


