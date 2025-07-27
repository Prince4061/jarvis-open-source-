
import pyttsx3
import speech_recognition as sr 
import os 
# from open import OpenExe 
import webbrowser
import joblib 
import datetime 


try:
    model = joblib.load('voice_assistant_model.pkl')
except FileNotFoundError:
    print("Model file 'voice_assistant_model.pkl' not found. Please run 'train_model.py' first.")
    exit()


engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id) 

engine.setProperty('rate', 180) 



def speak(audio):
    """Function to speak the given text"""
    print(f"Assistant: {audio}") 
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    """Function to listen to the user's command"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower().strip()
    except Exception as e:
        # speak("Sorry, I didn't catch that. Could you please say it again?") 
        return ""

def get_intent(query):
    """Function to predict the intent of the command using the model"""
    intent = model.predict([query])[0]
    return intent

# --- MAIN LOGIC ---

if __name__ == "__main__":
    speak("Hello Boss.")
    
    while True:
       
        query = takecommand()
        
        if not query:
            continue

      
        intent = get_intent(query)
        print(f"Predicted Intent: {intent}") 

      
        if intent == "GREETING":
            speak("Hello boss, how are you?")

        elif intent == "WHO_IS_BOSS":
            speak("Prince Sir. He is the brilliant mind who created me.")

        elif intent == "COMPLIMENT":
            speak("Thank you, Boss. I appreciate that.")
        
        elif intent == "OPEN_APP":
            app_name = query.replace('open', '').replace('start', '').replace('launch', '').strip()
            speak(f"Opening {app_name}.")
            try:
               
                os.startfile(app_name)
            except Exception as e:
                speak(f"Sorry, I couldn't open {app_name}.")

        elif intent == "PLAY_SONG":
            speak("Okay boss, playing a song for you.")
            folder_dir = "C:\\Users\\prince\\Desktop\\songs" 
            try:
                songs_list = os.listdir(folder_dir)
                if songs_list:
                    os.startfile(os.path.join(folder_dir, songs_list[0]))
                else:
                    speak("Sorry, the songs folder is empty.")
            except FileNotFoundError:
                speak("Sorry, I could not find the songs folder.")

        elif intent == "GET_TIME":
            strTime = datetime.datetime.now().strftime("%I:%M %p") # e.g., "08:30 PM"
            speak(f"Boss, the current time is {strTime}.")

        elif intent == "SEARCH_WEB":
            search_query = query.replace('search for', '').replace('who is', '').replace('what is', '').strip()
            speak(f"Searching Google for {search_query}.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif intent == "GOODBYE":
            speak("Goodbye, Boss! Have a great day.")
            break
        
        else:
            speak("Sorry, I don't understand that command yet.")