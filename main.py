from sre_constants import IN
import pyttsx3                                                           #installs text to speech (speaks out your result as jarvis)module with pip as pip install pyttsx3
import speech_recognition as sr                                          #install speech rec module and names as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyautogui
import pygeoip
import phonenumbers
import opencage
import geocoder
import folium




GOD = " Sir..."                                                       # GOD (in caps as const) with changable  value Desired to be read out  
BOT = "Jarvis..."

print("initialising " + BOT)

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
        r.pause_threshold = 1                                 # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 300                              # minimum audio energy to consider for recording  def val=300
        audio = r.listen(source)

    try :
        print("Recognising...")
        query = r.recognize_google(audio)
        print(f"I heard: {query}\n")    

    except Exception as e:
        print("Say that again please")    
        speak("Say that again please")  
        query = None    
    return query

def wishme():                                              # Function to wish according to current time
    hour = int(datetime.datetime.now().hour)               ### here current(now) howr is pulled out from datetime module and converted to intiger for comparision
  
    
    if hour>=4 and hour <12:
        speak("Good Morning" + GOD)

    elif hour>=12 and hour<17:    
         speak("Good Afternoon" + GOD)

    
    elif hour>=17 and hour<22:    
         speak("Good Evening" + GOD)     

    else:
         speak("Good Night" + GOD)

def iptrack():                                                   #for info abt ip add
    speak("Executing trackdown protocol")
    gip = pygeoip.GeoIP("C:\\Users\\91702\\Desktop\\Jarvis\\BOT\\GeoLiteCity.dat")
    res = gip.record_by_addr(IP)
    speak("deep search mechanism completed. IP tracked dow succesfully. Results on your screen! Let me read for you")
    
    for key, val in res.items():
        print('%s : %s' % (key,val) )
        speak('%s : %s' % (key,val) )   
        
    speak("Do you want me to show it on map ?")
    reply = takeCommand()
    if 'yes' in reply.lower():
        ipmap = "https://earth.google.com/web/search/40.730890336425404,+-73.98785954084427/@21.86160242,98.21483344,-16555.87785054a,48804308.25455189d,35y,353.40374679h,0t,0r/data=CmoaQBI6GVi7N9CNXURAIb9iDRc5f1LAKiY0MC43MzA4OTAzMzY0MjU0MDQsIC03My45ODc4NTk1NDA4NDQyNxgCIAEiJgokCYjd_dCfXkRAETn9-gAGXURAGUlvLxnmflLAIRxsC7flf1LA"
        #ipmap1 = "https://www.google.com/maps/place/40%C2%B043'51.3%22N+73%C2%B059'16.3%22W/@40.7309143,-73.9884051,176m/data=!3m2!1e3!4b1!4m5!3m4!1s0x0:0x0!8m2!3d40.7309143!4d-73.9878579"

        webbrowser.get('firefox').open(ipmap, new=1)    
        speak("Ok!... Fetching the realtime data from satellite and Rendering it in 3 dimensions for you... ")
        speak("")
        speak("Servelances... now Flying in circular manoeuvres over IP user's coordinates")


def phtrack():
    speak("sure please Enter the number")
    key = "1a5ad34105e74c59b8d924658a5531a2"
    numb = input("Enter Number :_")
    speak("ok! searching the data base ")

    from phonenumbers import geocoder  

    sannumber = phonenumbers.parse(numb)

    #for country
    Location = geocoder.description_for_number(sannumber, 'en')
    speak("search succesfull")
    print("Country:_" + Location)
    speak("the user  is located near Pune..., Maharashtra" + Location)

    # for service provider
    from phonenumbers import carrier

    serprov = phonenumbers.parse(numb)
    carname = carrier.name_for_number(serprov, 'en')
    print("Service Provided by:_" + carname )
    speak("And is aviling services from" + str(carname))

    from opencage.geocoder import OpenCageGeocode

    geocoder = OpenCageGeocode(key)

    query = str(Location)

    results = geocoder.geocode(query)
    #print(results)

    lat =results[0]['geometry']['lat']
    lng =results[0]['geometry']['lng']
    speak("Here are his coordinates!")

    print(lat,lng)

    speak("Do you want me to show it on map?")
    reply = takeCommand()
    if 'yes' in reply.lower():
        mymap = folium.Map(Location=[lat,lng], zoom_start=9)
        folium.Marker([lat, lng],popup=Location).add_to((mymap))
        mymap.save("mylocation.html")
        os.startfile('mylocation.html')
speak("Initialising " + BOT)

###############################################    Bot is initialised here . Main code starts hereafter     ##########################################                  


wishme() 
#speak("This is "+ BOT + " at your service online and ready ! How may I Help You ?" ) 
query = takeCommand()


webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
#wiki = ["who is", "what is", "wikipedia"]


                                                ############       online commands  ########### 

if 'get me info on' in query:
    speak('Hacking into the secure servers of archive database')
    query = query.replace("get me info on", "")
    results = wikipedia.summary(query, sentences =2)
    
    print(results)
    speak("Servers breached ! Here's what i found !" + results)
 
elif 'open YouTube' in query:
     youtube = "youtube.com"
     speak("Starting youtube")
     webbrowser.get('firefox').open(youtube, new=1)
    
elif 'on YouTube' in query:
    query1 = query.replace("search for", "")
    query2 = query1.replace("on YouTube", "")
    youtube = "https://www.youtube.com/results?search_query=" + query2
    speak("Starting youtube")
    webbrowser.get('firefox').open(youtube, new=1)      

elif 'on Google' in query:
    query1 = query.replace("search for", "")
    query2 = query1.replace("on Google", "")
    google = "https://www.google.com/search?q=" + query2
    speak("Launching Google")
    webbrowser.get('firefox').open(google, new=1) 

elif 'launch' in query.lower():
    speak("ok," + GOD)
    query = query.replace("launch", "")
    web = "https://www." + query 
    web1 = web + ".com"
    webbrowser.get('firefox').open(web1, new=1)

elif 'stream' in query.lower():
    music = query.replace("stream", "")
    pywhatkit.playonyt(music)
    speak("playing the video on Youtube for you")

elif 'address' in query.lower():
    speak("ok, Initializing Trackdown protocol... in 3... 2... 1... ")
    speak("systems are ready! now... , Enter the IP Address ")
    IP = input("Enter IP Adress :_")

    iptrack()
    


elif 'phone number' in query.lower():
    phtrack()
    
    #google = str('https://www.google.com/maps/@') 
    #gog1 = google + str(lat) +","+ str(lng)
    #webbrowser.get('firefox').open(gog1, new=1)
    
                                                            ######   Local commands     #####

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"{GOD} the time is {strTime}")

elif 'play music' in query.lower():
    os.startfile('C:\\Users\\91702\\Desktop\\-\\Songs\\ALONE_AW.mp3')

elif 'screenshot' in query.lower():

    ss = pyautogui.screenshot()
    
    ss.save('C:\\Users\\91702\\Desktop\\Jarvis\\BOT\\Screenshots\\ss.png')    
    speak("Screenshot taken! do you want me to open it?")
    reply = takeCommand()
    if 'yes' in reply.lower():
        os.startfile('C:\\Users\\91702\\Desktop\\Jarvis\\BOT\\Screenshots\\ss.png')

elif 'open pycharm' in query.lower(): 
    os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe")
    speak("Running pycharm if foreground")
elif 'close pycharm' in query.lower(): 
    os.system('TASKKILL /F /IM pycharm64.exe')
    speak("programme terminated successfully")    

elif 'break' in query.lower():
        speak("Ok" + GOD +"you can call me Anytime")
        os.system('TASKKILL /F /IM main.py')

elif 'terminate' in query.lower():
        speak("Ok!... terminating all services. Glad to serve you!" + GOD )
        os.system('TASKKILL /F /IM main.py')
        os.system('TASKKILL /F /IM call.py')

elif 'say' in query.lower():
    say = query.replace("say", "")
    speak(say)   
