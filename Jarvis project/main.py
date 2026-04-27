 # first install 'pip install speechrecognition pyaudio'
# second install 'pip install setuptools'
# third install ' pip install pyttsx3'
# fourth install 'pip install pocketsphinx'

import speech_recognition as sr
import webbrowser 
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    if "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    if "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
   

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake word "Jarvis"
        
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        # recognize speech using Sphinx
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=2)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Lusten for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.RequestError as e:
            print("Error; {0}".format(e))