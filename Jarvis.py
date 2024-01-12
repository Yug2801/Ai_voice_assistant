import pyttsx3
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
import sys
from word2number import w2n
from googletrans import Translator
import pyperclip 
import pyautogui
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)



intents = {
  
    "open_chrome": ["open chrome", "launch chrome", "start chrome", "chrome kholo", "chrome launch karo", "chrome shuru karo"],
    "close_chrome": ["close chrome", "exit chrome", "chrome band karo", "chrome exit karo"],
    "open_youtube": ["open youtube and search", "launch  and search", "play on youtube","Search on youtube","gaana bajao youtube par", "youtube kholo", "youtube launch karo", "youtube shuru karo"],
    "close_youtube": ["close youtube", "exit youtube", "youtube band karo", "youtube exit karo"],
    "open_firefox": ["open firefox", "launch firefox", "start firefox", "firefox kholo", "firefox launch karo", "firefox shuru karo"],
    "close_firefox": ["close firefox", "exit firefox", "firefox band karo", "firefox exit karo"],
    "battery_percentage": ["battery percentage", "how much charge is left", "charging status", "battery kitni hai", "battery bacha hua hai", "charging status kya hai","how much charging","what is the percentage of charging left in my laptop"],
    "change_tab": ["change tab", "switch tab", "change window", "tab badlo", "window badlo", "switch tab karo"], 
    "open_windows": ["open windows", "show desktop", "windows kholo", "desktop dikhao"],
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
    "open_notepad_write": ["open notepad and write", "notepad kholo aur likho", "write in notepad", "notepad mein likho", "kuch likho notepad mein"],
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
    "search_google": ["open google", "search on google", "look up on google", "google search", "google par search karo", "google mein dekho"],
    "send_whatsapp_message": ["send whatsapp message", "whatsapp message", "send a message on whatsapp", "whatsapp par message bhejo", "whatsapp mein message"],
    "search_youtube": ["youtube", "search on youtube", "look up on youtube", "youtube search", "youtube par search karo", "youtube mein dekho"],
    "send_email": ["email to me", "send an email", "send me an email", "email bhejo", "mereko email karo"],
    "exit_assistant": ["no thanks", "exit", "close", "shut down", "no thanks", "bahut hua", "band karo", "band hoja"],
    "create_image": ["create image", "generate image", "make an image", "image creation", "image banao", "photo banao"],
    "current_time": ["current time", "what's the time now", "tell me the time", "abhi kitni baje hai", "current samay"],
    "current_date": ["current date", "what's the date today", "tell me the date", "aaj ka date", "today's date"],
    "current_day": ["current day", "what day is it today", "tell me the day", "aaj ka din", "today's day"],


}


training_query = []
labels = []
for label, phrases in intents.items():
    for phrase in phrases:
        training_query.append(phrase)
        labels.append(label)

model = make_pipeline(CountVectorizer(), MultinomialNB())

model.fit(training_query, labels)


joblib.dump(model, 'intent_recognition_model.joblib')
def recognize_intent(query):

    loaded_model = joblib.load('intent_recognition_model.joblib')

 
    predicted_intent = loaded_model.predict([query])

    return predicted_intent[0]


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

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


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

               
                query=translate_to_english(query)
            except Exception as e:
                speak("Say that again please...")
                return "none"
        except Exception as e:
            speak("Say something please...")
            return "none"
    print(f"User said: {query}")
    return query

if __name__ == "__main__":
    wish()
    while True:
    
        query_user=takecommand().lower()
        print(query)
        query=recognize_intent(query_user)

        if "open_notepad_write" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

            speak("Sir, What should I write in it")
            text = ""
            
            while "save it" or "jsave note" or "save this" or  "note save karo"or  "ye save karo"or "save karo" not in text:
                if  "delete last word" or  "last word delete karo" or "delete last word in notepad"or "notepad mein last word delete karo" in text:
             
                    pyautogui.hotkey('ctrl', 'z')  
                else:
                    text = takecommand().lower()
                    pyautogui.write(text)

            speak("Sir, please provide a name for the file.")
            file_name = takecommand().lower()

            pyautogui.hotkey('ctrl', 's') 
            pyautogui.write(file_name)    
            pyautogui.press('enter')       
            pyautogui.hotkey('ctrl', 'w')  
            speak(f"Notepad content saved as {file_name} and closed.")

        
        elif "open_adobe_reader_read" in query:
            apath="C:\\Programquery\\Microsoft\\Windows\\Start Menu\\Programs\\AcroRd32.exe"
            os.startfile(apath)
        elif "open_command_prompt" in query:
            os.system("start cmd")
        elif "open_command_prompt" in query:
            os.system("start cmd")

        elif "open_camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play_music" in query:
            music_dir="D:\\music"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,rd))
        
        elif "get_ip_address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP is {ip}")

        elif "search_wikipedia" in query:
            speak("searching on wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia,")
            speak(results)

        elif "open_facebook" in query:
            webbrowser.open("facebook.com")

        elif "open_whatsapp" in query:
            webbrowser.open("web.whatsapp.com")
        
        elif "open_stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        
        elif "open_firefox" or "search_google" in query:
            speak("sir, what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send_whatsapp_message" in query:
            speak("sir, on what number I have to send message")
            num=takecommand()
            num = convert_phone_number_to_numeric(num)
            a=1
            while a:
                speak(f"sir, the number is {num} is it correct")
                mssg=takecommand()
                if "no" in mssg:
                    num=takecommand()
                    a=1
                elif  "yes" in mssg:
                    speak("sir, what message I have to send message")
                    msg=takecommand().lower()
                    kit.sendwhatmsg(f"+91{num}", f"{msg}",2,25)
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
            speak("sir, do you want to save all these images")
            save=takecommand().lower()
            if "yes" in save:
                
                pyautogui.click(x=1848, y=79)
                sleep(5)
                pyautogui.click(x=1273, y=988)
            elif "No" in save:
                speak("Ok Sir")
            
        elif 'battery_percentage' in query:
            battery = psutil.sensors_battery()
            print(f"Your laptop is on: {battery.percent}%")
            speak("Your laptop is on: {battery.percent}%".format(battery=battery))

        elif 'change_tab'in query:
            speak("Ok..Changing The Tab")
            pyautogui.keyDown("alt")
            press_and_release('alt + Tab')

        elif 'search_windows' in query:
            speak("Ok..Opening Windows")
            press('windows')


        elif 'open_windows' or 'home_screen' in query:
            speak("Ok..Redirecting You To Home Screen")
            press_and_release('windows + d')

        elif 'open_chrome' in query:
             press_and_release('windows')
             sleep(2)
            press_and_release('c')
            press_and_release('h')
            press_and_release('r')
            press_and_release('o')
            press_and_release('m')
            press_and_release('e')
            press_and_release('Enter')




        elif 'close_chrome' in query: 
            os.system("taskkill /f /im chrome.exe")
            speak("Chrome has been closed")

        elif 'close_youtube' or"close_firefox" in query:
            os.system("taskkill /f /im firefox.exe")

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

        elif "volume_down" in query or "decrease the volume" in query:
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

        elif "good bye jarvis" in query or"goodbye jarvis" in query or "you need a break" in query:
            speak("Ok Sir, you can call me any time")
            speak("just say wake up jarvis")
            playsound("C:\\Users\\user\\Music\\sleep.mp3")
            break

            
            
        speak("Sir,do you have any other work")
