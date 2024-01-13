from ecapture import ecapture as ec
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import psutil
import sys
from word2number import w2n
from googletrans import Translator
import pyperclip 
import pyautogui
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
import uuid
import keyboard 
from englisttohindi.englisttohindi import EngtoHindi
from Brain.Bard import MainExecution 
import tkinter as tk
from test import main
main()
r = sr.Recognizer()
#pyperclip.copy('text to be copied')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
# OpenWeatherMap API key and base URL
weather_api_key = "002baa6bc2e00eef9696096ab42efe0c"
weather_base_url = "http://api.openweathermap.org/data/2.5/weather"

# News API key and base URL
news_api_key = "83392a25c2734e4e977f35da025786ab"
news_base_url = "https://newsapi.org/v2/top-headlines"

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


speak("Initiating Jarvis Sir")
speak("Starting all System Applications")
speak("Installing and Checking all drivers")
speak("Checking internet connection")
speak("Wait a moment Sir")
def check_internet_connection():    
    try:
        r = requests.get("https://google.com")
        return True
    except:
        return False    

if check_internet_connection():
    speak("Internet connection is available")

intents = {
  
    "open_chrome": ["open chrome", "launch chrome", "start chrome", "chrome kholo", "chrome launch karo", "chrome shuru karo"],
    "close_chrome": ["close chrome", "exit chrome", "chrome band karo", "chrome exit karo"],
    "close_youtube": ["close youtube", "exit youtube", "youtube band karo", "youtube exit karo"],
    "close_firefox": ["close firefox", "exit firefox", "firefox band karo", "firefox exit karo"],
    "battery_percentage": ["battery percentage", "how much charge is left", "charging status", "battery kitni hai", "battery bacha hua hai", "charging status kya hai","how much charging","what is the percentage of charging left in my laptop"],
    "change_tab": ["change tab", "switch tab", "change window", "tab badlo", "window badlo", "switch tab karo"], 
    "search_windows": ["search on windows", "search files", "windows mein search karo", "files dhoondo"],
    "home_screen": ["home screen", "show home screen", "home screen dikhao", "home screen kholo"],
    "close_command_prompt": ["close command prompt", "exit cmd", "command prompt band karo", "cmd band karo"],
    "shutdown_system": ["shut down the system", "turn off the computer", "system band karo", "computer band karo"],
    "restart_system": ["restart the system", "reboot the computer", "system restart karo", "computer restart karo"],
    "lock_system": ["lock the system", "lock computer", "system lock karo", "computer lock karo"],
    "take_screenshot": ["take screenshot", "capture screen", "screenshot lo", "screen capture karo"],
    "volume_up": ["volume up", "increase volume", "volume badhao", "volume badao"],
    "volume_down": ["volume down", "decrease volume", "volume kam karo", "volume ghatao"],
    "mute_volume": ["mute", "mute volume", "volume mute karo", "volume band karo"],
    "scroll_down": ["scroll down", "scroll down page", "nicha scroll karo", "page niche karo"],
    "scroll_up": ["scroll up", "scroll up page", "upar scroll karo", "page upar karo"],
    "type_text": ["type", "type something", "write text", "kuch likho", "likho", "text likho"],
    "close_window": ["close the window", "close current window", "window band karo", "current window band karo"],
    "open_notepad_write": ["open notepad and write", "notepad kholo aur likho", "write in notepad", "notepad mein likho","mujhe kuch likhna hai", "kuch likho notepad mein"],
    "save_note": ["save note", "save this", "note save karo", "ye save karo", "save karo"],
    "delete_last_word": ["delete last word", "last word delete karo", "delete last word in notepad", "notepad mein last word delete karo"],
    "save_with_name": ["save with name", "save note with name", "note ko naam se save karo", "is note ka naam se save karo"],
    "open_adobe_reader_read": ["open adobe reader", "Adobe reader kholo", "Kholo Adobe reader", "Mereko kuch padhna hai", "kuch padhna hai", "I want to read pdf "],
    "open_command_prompt": ["open command prompt", "open cmd"],
    "open_camera": ["open camera", "camera kholo"],
    "play_music": ["play music", "play a song", "start music", "music please", "song please"],
    "get_ip_address": ["ip address", "what's my IP", "IP pata karo"],
    "search_wikipedia": ["wikipedia", "search on wikipedia", "look up on wikipedia", "tell me about", "wikipedia par search karo", "wikipedia mein dekho"],
    "open_facebook": ["open facebook", "visit facebook", "go to facebook", "facebook kholo", "facebook par jao"],
    "open_whatsapp": ["open whatsapp", "visit whatsapp", "go to whatsapp", "whatsapp kholo", "whatsapp par jao"],
    "open_stackoverflow": ["open stackoverflow", "visit stackoverflow", "go to stackoverflow", "stackoverflow kholo", "stackoverflow par jao"],
    "send_whatsapp_message": ["send whatsapp message", "whatsapp message", "send a message on whatsapp", "whatsapp par message bhejo", "whatsapp mein message"],
    "send_email": ["email to me", "send an email", "send me an email", "email bhejo", "mereko email karo"],
    "exit_assistant": ["no thanks", "exit", "close", "shut down", "no thanks", "bahut hua", "band karo", "band hoja"],
    "create_image": ["create image", "generate image", "make an image", "image creation", "image banao", "photo banao"],
    "open_youtube": ["open youtube", "launch youtube  and search", "play on youtube","Search on youtube","gaana bajao youtube par", "youtube kholo", "youtube launch karo", "youtube shuru karo"],
    "search_google": [ "search on google", "google par search karo","open firefox", "firefox kholo", "firefox shuru karo"],
    "current_time": ["current time", "what's the time now", "tell me the time", "abhi kitni baje hai", "current samay"],
    "current_date": ["current date", "what's the date today", "tell me the date", "aaj ka date", "today's date"],
    "current_day": ["current day", "what day is it today", "tell me the day", "aaj ka din", "today's day"],
    "get_current_location": ["current location", "where am I", "location batao", "my current place", "find my location", "where am I right now"],
    "get_weather": ["current weather", "weather update", "tell me the weather", "mausam kaisa hai", "get weather forecast", "weather conditions"],
    "get_top_news": ["latest news", "top headlines", "news updates", "current affairs", "headline news", "breaking news", "news batao"],
    "suggest_movie": ["movie suggestion", "recommend a film", "suggest me a movie", "best movies to watch", "good films", "film suggestion", "which movie to watch"],
    "get_joke": ["tell me a joke", "joke sunao", "make me laugh", "funny joke", "hasi ka injection", "joke batao", "kuch hasi wala"],
    "all_in_one": ["who is","tell me about","define","explain","describe","what is","iske baare mein batao","content","information","details","know more about","give me the scoop on","enlighten me about"]
    

}


training_query = []
labels = []
for label, phrases in intents.items():
    for phrase in phrases:
        training_query.append(phrase)
        labels.append(label)

model = make_pipeline(CountVectorizer(), RandomForestClassifier(n_estimators=100, random_state=42))

model.fit(training_query, labels)


joblib.dump(model, 'intent_recognition_model.joblib')

def recognize_intent(query):

    loaded_model = joblib.load('intent_recognition_model.joblib')

 
    predicted_intent = loaded_model.predict([query])

    return predicted_intent[0]

def save_notepad(text):

    speak("Sir, please provide a name for the file.")
    file_name = takecommand().lower()

    pyautogui.hotkey('ctrl', 's')
    pyautogui.write(file_name)
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 'w')

    speak(f"Notepad content saved as {file_name} and closed.")

def close_window():
    pyautogui.hotkey('alt', 'f4')

def open_notepad_write():
    npath = "C:\\Windows\\notepad.exe"
    os.startfile(npath)

    text = ""

    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")

        if "save it" in text or "save note" in text or "save this" in text or "note save karo" in text or "ye save karo" in text or "save karo" in text:
        
            save_notepad(text)
            break
        elif "delete last word" in text or "last word delete karo" in text or "delete last word in notepad" in text or "notepad mein last word delete karo" in text:
       
            pyautogui.hotkey('ctrl', 'z')
        else:
            pyautogui.write(text)
def save_notepad(text):
  
    speak("Sir, please provide a name for the file.")
    file_name = takecommand().lower()

    pyautogui.hotkey('ctrl', 's')
    pyautogui.write(file_name)
    pyautogui.press('enter')

    close_window()

    speak(f"Notepad content saved as {file_name} and closed.")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('2021kucp1110@iiitkota.ac.in','Yug@28012003')
    server.sendmail('2021kucp1110@iiitkota.ac.in',to,content)
    server.close()
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am jarvis sir, how can I help you")

def convert_phone_number_to_numeric(phone_words):
    words_list = phone_words.split()


    numeric_list = [str(w2n.word_to_num(word)) if word.isalpha() else word for word in words_list]
    numeric_phone_number = ' '.join(numeric_list)

    return numeric_phone_number



def get_current_location():
    location = geocoder.ip('me')
    return location.city

def get_weather(city):
    params = {
        'q': city,
        'appid': weather_api_key,
    }
    response = requests.get(weather_base_url, params=params)
    data = response.json()

    if data['cod'] == '404':
        return "City not found. Please check the city name."

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    return f"The weather in {city} is {weather_description}. The temperature is {temperature} degrees Celsius."

def get_top_news():
    params = {
        'apiKey': news_api_key,
        'country': 'in',
    }
    response = requests.get(news_base_url, params=params)
    data = response.json()

    if data['status'] != 'ok':
        return "Unable to fetch news at the moment."

    articles = data['articles'][:5]  # Take only the top 5 articles
    headlines = [article['title'] for article in articles]
    return "Here are the top headlines:\n" + "\n".join(headlines)
def suggest_movie():
    speak("Sure, I can suggest a movie. What genre are you in the mood for?")
    genre = takecommand().lower()
    while "none" in genre:
        genre = takecommand().lower()

    ia = imdb.IMDb()
    movies = ia.search_movie(genre)

    if not movies:
        speak(f"Sorry, I couldn't find any movies in the {genre} genre.")
    else:
        random_movie = random.choice(movies)
        speak(f"I suggest you watch {random_movie['title']}. Enjoy!")
def get_joke():
    joke = pyjokes.get_joke(language='en', category='all')
    res = EngtoHindi(joke)
    return res.convert
def translate_to_english(hindi_text):
    translator = Translator()
    english_text = translator.translate(hindi_text, src='hi', dest='en').text
    return english_text

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
            try:
                print("Recognizing....")
                lang = 'en-IN'  
                query = r.recognize_google(audio, language=lang)

               
                #query=translate_to_english(query)
            except Exception as e:
                speak("Say that again please...")
                return "none"
        except Exception as e:
            speak("Say something please...")
            return "none"
    print(f"User said: {query}")
    return query

if __name__ == "__main__":
    speak("All drivers are available")
    speak("All systems vae been activated")
    wish()
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Currently it is {strTime}")
    while True:
    
        query_user=takecommand().lower()
        print(query_user)
        query=recognize_intent(query_user)
        print(query)
        if "none" in query_user:
            continue
        

        elif "open_notepad_write" in query:
            open_notepad_write()

        
        elif "open_adobe_reader_read" in query:
            apath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader 9.lnk"
            os.startfile(apath)
        elif "open_command_prompt" in query:
            os.system("start cmd")
        elif "open_command_prompt" in query:
            os.system("start cmd")
        elif "get_current_location":
            location = get_current_location()
            speak(location)
        elif "get_weather" in query:
            speak("Of where you want to get weather?")
            city = takecommand().lower()
            while "none" in city:
                city = takecommand().lower()
            weather = get_weather(query)
            speak(weather)
        elif "get_top_news" in query:
            top_news = get_top_news()
            speak(top_news)
        elif "suggest_movie" in query:
            suggest_movie()
        elif "get_joke" in query:
            joke = get_joke()
            speak(joke)
        elif "all_in_one" in query:
            result=MainExecution(query_user)
            speak(result)
        elif "open_camera" in query:
          
            speak("Capturing image. in 3 seconds...")
            ec.capture(0, "Jarvis Camera ", "img.jpg")
            speak("image captured")
            keyboard.press_and_release('alt + f4')


        elif "play_music" in query:
            music_dir="D:\\music"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,rd))
        
        elif "get_ip_address" in query:
            url = 'https://api64.ipify.org?format=json'
            response = requests.get(url)
            data = response.json()
            ip_address = data['ip']
            speak(f"your IP is {ip_address}")

        elif "search_wikipedia" in query:
            speak("what should I search on wikipedia...")

            quer=takecommand().lower()
            while "none" in quer:
                quer=takecommand().lower()
            results=wikipedia.summary(quer,sentences=2)
            speak("according to wikipedia,")
            speak(results)

        elif "open_facebook" in query:
            cm="facebook.com"
            webbrowser.get('firefox').open(f"https://{cm}")

            webbrowser.open("facebook.com")


        elif "open_whatsapp" in query:
            cm="web.whatsapp.com"
            webbrowser.get('firefox').open(f"https://{cm}")
            
        
        elif "open_stackoverflow" in query:
            cm="stackoverflow.com"
            webbrowser.get('firefox').open(f"https://{cm}")

            
        
        elif "search_google" in query:
            speak("sir, what should i search on google")
            cm=takecommand().lower()
            webbrowser.get('firefox').open(f"https://www.google.com/search?client=firefox-b-d&q={cm}")

        elif "send_whatsapp_message" in query:
            speak("sir, on what number I have to send message")
            num=takecommand()
            num = convert_phone_number_to_numeric(num)
            a=1
            while a:
                speak(f"sir, the number is {num} is it correct")
                mssg=takecommand()
                if "no" in mssg:
                    speak(f"sir, the number is")
                    num=takecommand()
                    a=1
                elif  "yes" in mssg:
                    speak("sir, what message I have to send message")
                    msg=takecommand().lower()
                    kit.sendwhatmsg(f"+91{num}", f"{msg}",2,25)
                    break
                    a=0

        elif "open_youtube" in query:
            speak("sir, what should i search on youtube")
            cn=takecommand().lower()
            kit.playonyt(f"{cn}")

        elif "send_email" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "yugmodi284@gmail.com"
                sendEmail(to,content)
                speak("email has been sent to avi")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to yug")


        elif "create_image" in query:
            speak("sir, what type of image you want to create")
            name=takecommand().lower()
            webbrowser.open(f"https://deepdreamgenerator.com/search?q={name}")
            sleep(10)
            speak("sir, do you want to save all these images")
            a=1
            while a:
                save=takecommand().lower()
                if "yes" in save:
                    speak("Ok Sir, wait a minute") 
                    pyautogui.click(x=1803, y=74)
                    sleep(2)
                    pyautogui.click(x=1273, y=988)

                    sleep(5)

                    keyboard.press_and_release('alt + f4')
                    a=0
                elif "No" in save:
                    speak("Ok Sir")
                    keyboard.press_and_release('alt + f4')
                    a=0

            
            
        elif 'battery_percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f"Your laptop is on: {percentage}%")
            speak(f"Your laptop is on: {percentage}%")


        elif 'change_tab'in query:
            speak("Ok..Changing The Tab")
            pyautogui.keyDown("alt")
            keyboard.press_and_release('alt + Tab')

        elif 'search_windows' in query:
            speak("Ok..Opening Windows")
            press('windows')


        elif 'home_screen' in query:
            speak("Ok..Redirecting You To Home Screen")
            keyboard.press_and_release('windows + d')

        elif 'open_chrome' in query:
            keyboard.press_and_release('winleft')


            time.sleep(2)


            for char in 'chrome':
               keyboard.press_and_release(char)


            keyboard.press_and_release('enter')




        elif 'close_chrome' in query: 
            os.system("taskkill /f /im chrome.exe")
            speak("Chrome has been closed")

        
        elif 'current_time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'current_date' in query:
            strDate = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Sir, today's date is {strDate}")

        elif 'current_day' in query:
            today = datetime.datetime.now().strftime("%A")
            speak(f"Sir, today is {today}")
        
        elif "close_command_prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "shutdown_system" in query:
            os.system("shutdown /s /t 5")

        elif "restart_system" in query:
            os.system("shutdown /r /t 5")

        elif "lock_system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "take_screenshot" in query:
            speak('tell me a name for the file')
            name = MicExecution().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "volume_up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume_down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute_volume" in query:
            pyautogui.press("volumemute")

        elif "scroll_down" in query:
            pyautogui.scroll(1000)
        elif "scroll_up" in query:
            pyautogui.scroll(-1000)

        elif 'type_text' in query: #10
            query = query.replace("type", "")
            pyautogui.write(f"{query}")

        elif 'close_window' in query:
            pyautogui.hotkey('alt', 'f4')

        elif "exit_assistant" in query:
            speak("Ok Sir, you can call me any time")
            speak("just say wake up jarvis")
            exit()
            break

            
            
        speak("Sir,do you have any other work")
