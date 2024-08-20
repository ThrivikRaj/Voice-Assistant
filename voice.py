import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
            return ""
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}")
    print(current_time)

def tell_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    speak(f"Today's date is {current_date}")
    print(current_date)

def search_web(query):
    speak(f"Searching the web for {query}")
    print("opening {}".format(query));
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    print("Hello!.... how can i assist you today?")
    speak("Hello!")
    
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hello! How can I assist you?")
            print("Hello! How can I assist you?")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search" in command:
            speak("What do you want to search for?")
            search_query = listen()
            if search_query:
                search_web(search_query)
            else:
                speak("Sorry, I didn't catch that.")
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I can help with telling the time, date, or searching the web. Please ask me.")
if __name__ == "__main__":
    main()