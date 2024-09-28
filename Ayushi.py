import Speech_Recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_query():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            print("recognize.....")
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower()
            if 'Alex' in query: 
             query = query.replace('Alex', '')
             talk(query)
    except Exception as e:
            print(f"Error: {e}")
            return ""
    return query


def run_Alex():
    query = take_query()


    if query:      
        print(query)
    if 'play' in query:
        song = query.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)


    if 'video' in query:
        talk('seaching to YouTube')
        video = query.replace('video', '')
        talk('playing' + video)
        pywhatkit.playonyt(video)
        
         
    elif 'time' in query:    

        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'who' in query or 'what is' in query:
        talk('searching to wikipedia')
        person = query.replace('who is', '').replace('what is', '')
        info = wikipedia.summary(person,2)
        talk('according to wikipedia')
        print(info)
        talk(info)
   
    elif'open youtube' in query:
        webbrowser.open('https://youtube.com')
      
    elif 'can i date you' in query or 'can you date with me' in query:
        talk('sorry,I have a headache')
    elif 'are you single' in query:
        talk('No, I am in love with my Developer')
    elif 'how are you' in query:
        talk('I am fine, and you?')
    elif 'i am also fine' in query or 'i am ok' in query:
        talk("it's sounds good ")
    elif 'i am not fine' in query or 'i am not ok' in query:
        talk("Ohh!! If there's any thing troubling you, you can share with me")
    elif "what's your name"  in query:
        talk('my name is Alex')
    elif 'who are you' in query:
        talk('I am an assistant of Ayushi')
    else:
        talk('please say the command again.')
while True:
    run_Alex()     
