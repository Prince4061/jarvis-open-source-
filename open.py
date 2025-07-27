import os
import pyttsx3
import webbrowser


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("mai sun raha hu ......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        print("sorry mai sun nahi paya, phir se bolo")
        return "None"
    return query 


def OpenExe(query):
   
    speak("Okay sir, opening...")
    
    if "notepad" in query:
        path = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(path)

    elif "ppt" in query or "powerpoint" in query:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(path)
    
    elif "open youtube" in query:
        webbrowser.open("www.youtube.com")
        
    else:
        speak("Sorry,dont know how to open it.")
