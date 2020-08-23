import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
newVoiceRate = 135
engine.setProperty('rate',newVoiceRate)
voices= engine.getProperty('voices') #getting details of current voice
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss.")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon Boss. ")
    else:
        speak("Good Evening Boss.")
    speak("I am Friday")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        speak("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        speak("Recognizing.....")
        query = r.recognize_google(audio, language="en-in") #Using google for voice recognition.
        print(f"User Said: {query}\n") #User query will be printed.
    except Exception as e:
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        speak("Say that again please...")
        return "None"  # None string will be returned
    return query
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    speak("Enter your email.")
    email = input("Enter your email: ")
    speak("Enter your password.")
    passwrd = input("Enter your password: ")
    server.login(email, passwrd)
    server.sendmail("prashantbhandari2007@gmail.com", to, content)
    server.close()
if __name__=="__main__":
    wishMe()
    speak("How may i help you Boss?")
    while True:
        query = take_command().lower()
        if "close" in query:
            print("Ok, Quiting.....")
            speak("Ok, Quiting.....")
            break
        elif "what is time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=5)
                print("According to Wikipedia")
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                print("Sorry no Information found.")
                speak("Sorry no Information found.")
        elif "open google" in query:
            print("opening google...")
            speak("opening google...")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            print("youtube.com")
            webbrowser.open("youtube.com")
        elif "play song" in query:
            while True:
                try:
                    print("Which song you want to hear?")
                    speak("Which song you want to hear?")
                    query2 = take_command().lower()
                    music_dir = 'D:\prashant\songs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, query2+".mp3"))
                except:
                    print("Sorry no song found.")
                    speak("Sorry no song found.")
                finally:
                    break
        elif "play video" in query:
            while True:
                try:
                    print("Which video you want to see?")
                    speak("Which video you want to see?")
                    query2 = take_command().lower()
                    music_dir = 'D:\prashant\\videos'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, query2+".mp4"))
                except:
                    print("Sorry no video found.")
                    speak("Sorry no video found.")
                finally:
                    break
        elif "send email" in query:
            try:
                print("To whom, you want to send mail?")
                speak("To whom, you want to send mail?")
                to = input("To: ")
                print("What should i say boss?")
                speak("What should i say boss?")
                content = input("Content: ")
                sendEmail(to, content)
                speak("sending.......")
                print("sending.......")
                print("Email send sucessfully")
                speak("Email send sucessfully")
            except:
                print("Email sending failed.")
                speak("Email sending failed.")