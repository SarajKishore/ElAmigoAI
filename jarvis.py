import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5') #voice api by MS
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Bat Computer, How may I help you Batman?")

def takeCommand():
    #microphone input returns string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("Recognizing")
        query= r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    
    except Exception as e:
        print(e)

        print("User voice unrecognizable. Try again...")
        return "None"
    return query
    

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()
    
         #logic
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")
        
        elif 'play music' in query:
            music_dir='F:\\Python El amigo\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The Time right now is {strTime}")
