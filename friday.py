import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12: 
        speak("Good Morning Sir")
    elif hour >= 0 and hour < 12:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Friday. Tony Stark's Advanced AI assistant that is now programmed to work with you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_in')
        print(f"User said: {query}\n")
   
    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
   wishMe()
   
   while True:
       query = takeCommand().lower()
       if 'wikipedia' in query: 
           speak("Searching on wikipedia...")
           query = query.replace('wikipedia','')
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           webbrowser.open('youtube.com')

       elif 'open google' in query:
           webbrowser.open('google.com')    
       
       elif 'play music' in query:
           music_dir = "D:\\Songs"
           songs = os.listdir(music_dir)
           rand_num = random.randint(0,len(songs)-1)
           os.startfile(os.path.join(music_dir, songs[rand_num]))    
       
        # elif 'what is time' in query:
        #    strtime = datetime.datetime.now().strftime("%H:%M:%S")
        #    speak(f"Sir, the time is {strtime}")
        
        # elif 'send email' in query:
        #     try:
        #         speak("What should I say Sir?")
        #         content = takeCommand()
        #         to = "hardy.lko@gmail.com"
        #         sendEmail(to,content)
        #         speak("I have sent the email Sir.")
        #     except Exception as e:
        #         speak("Sorry Sir.")
        #         speak("I couldn't send the email.")