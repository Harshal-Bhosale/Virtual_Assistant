import pyttsx3    
import os
import speech_recognition as sr


#from main import GOD
#from main import BOT

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):                                           #The speak function speaks the string which is passed to it
    engine.say(text)
    engine.runAndWait()

def takeCommand():                                           # Function to take input as speech and return a string
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8                                 # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 300                              # minimum audio energy to consider for recording  deaf val=300
        audio = r.listen(source)

    try :
        print("Recognising...")
        query = r.recognize_google(audio)
        print(f"I heard: {query}\n")    

    except Exception as e:
        #print("Say that again please")    
        query = None    
    
    return query  
    
    


while True:
    wakeup = takeCommand()
    if 'Jarvis' in str(wakeup):
        speak("Initialising Jarvis")
        print("Initialising Jarvis")
        #speak("This is Jarvis at your service! online and ready ! How may I Help You ?" ) 
        os.startfile('C:\\Users\\91702\\Desktop\\Jarvis\\BOT\\main.py')

    else:
        print("Nothingg")


