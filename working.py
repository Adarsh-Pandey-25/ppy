import pyttsx3
import pyjokes
import speech_recognition as sr
import random
import os
import wikipedia
import pywhatkit 
import requests 

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id )
def speak ( audio):
    engine.say(audio) # this basically process the audio 
    engine.runAndWait() # we will come to here this when this command run

def takeCommand2() :
    r = sr.Recognizer()
    with sr.Microphone() as source :

        print("i'm listning... ")
        r.pause_threshold = 0.8
        # r.energy_threshold = 300
        # r.phrase_threshold = 0.1
        audio = r.listen(source)

        try :
            # print("Recogniging...")
            query = r.recognize_google(audio,language= 'en-in')
            print(f'user said : { query } \n')
        except Exception as e :
            # print(e)     error messege 
            # print('sorry ! could you please say that again')
            takeCommand2()
            return "None"

        return query

# def downloadYoutube():
#     from pytube import YouTube
#     from pyautogui import click
#     from pyautogui import hotkey
#     import pyperclip   
#     from time import sleep
#     sleep(3)

#     click(x=1089, y=72)
#     hotkey("ctrl","c")
#     value = pyperclip.paste()
#     Link = str(value) 

#     def Download(link):
#         url = YouTube(link)
#         video = url.streams.first()
#         video.download("C:\\Users\\sagar\\OneDrive\\Desktop\\david\\Database\\YouTube")

#     Download(Link)
#     speak("Done sir i have downloaded the video")

def sayingJokes():
    joke = pyjokes.get_joke(language="en", category="all")
    speak("here it is ")
    print(joke)
    speak(joke)

def meetFunc(query):
    val = query.split()
    name = val[-1]
    speak("hii "+name+" "+"how are you  ?")
    print("hii "+name+" "+"how are you  ?")

def note():
    l = ["What do you want me to open sir M S word or notepad","sir where woukd you like to use, Notepad or M S word "]
    speak(random.choice(l))
    command = takeCommand2()
    if "notepad" in command :
        path = "C:\\Users\\visha\\Desktop\\notepad.txt"
        speak("On the way sir")
        os.startfile(path)
    elif "MS Word" in command or "word" in command :
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
        speak("On the way sir")
        os.startfile(path)

def search_wikipedia(query):
    speak('ok sir searching on wikipedia  ')
    query = query.replace('wikipedia','')
    query = query.replace('search','')
    query = query.replace('on','')
    result = ""
    try :
        result = wikipedia.summary(query, sentences = 1)
    except Exception as e :
        print("please say SEARCH < INFORMATION > ON WIKIPEIDEA " )

    speak('accordung to wikipedia')
    print(result)
    speak(result)  

def NotePade():
    path = "C:\\Users\\visha\\Desktop\\notepad.txt"
    speak("On the way sir")
    os.startfile(path)

def close_NotePade():
    speak ("okay sir, closing Notepad ")
    os.system("TASKKILL /F /IM C:\\Users\\visha\\Desktop\\notepad.txt")

def open_code():
    path = "C:\\Users\\visha\\AppData\\Local\\Programs\\MicrosoftVSCode\\Code.exe"
    speak("On the way sir")
    os.startfile(path)

def music():
    speak("which song you want me to play sir")
    import david2
    command =  david2.takeCommand()
    if 'anything' in command :
        speak("hope you would like it, ")
        l = ["khamoshiyan", 'main rang sharbaton ka', 'chhokra jawan re', 'galti se mistake']
        pywhatkit.playonyt(random.choice(l)) 
    else :
        speak("sure sir")
        pywhatkit.playonyt(command)

def google_search():

    speak("what you want me to search sir")
    command = takeCommand2()
    l = command.split()
    if "what" in l :
        c = l.index("what")
        l = l[c:]
    elif "how" in l :
        c = l.index("how")
        l = l[c:]
    else :
        for i in range(len(l)):
            if l[i] == "the":
                l[i] = ""
                break 
            else :
                l[i] = ""
        
    query = " ".join(l).strip()
    speak("sure sir")
    pywhatkit.search(query)
    result = wikipedia.summary(query, sentences = 1)
    speak(result)
    print(result)


def instagram():
    
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC 
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By 
    from selenium.common.exceptions import TimeoutException
    from bs4 import BeautifulSoup
    from IPython.display import Image  # fro displaying the image in ouput cell
    import time
        

    driver = webdriver.Chrome(executable_path= "C:\\Users\\sagar\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
    #seting the window size 
    driver.set_window_size(700, 920)
    driver.get("https://www.instagram.com/")
    driver.get("https://web.whatsapp.com/")


    #Initializing the wait object 
    wait = WebDriverWait(driver,8)
    try :
        # locating the textbox and waiting fro it to load 
        # driver.refresh()
        user_name = wait.until(EC.presence_of_element_located(("name","username")))
        user_name.send_keys(username)

        ### lovcating the password box and sending the password 
        pswd = driver.find_element("name","password")
        pswd.send_keys(password)

        #Locating the login button 
        button = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button/div')))
        button.submit()

        popup = wait.until(EC.presence_of_element_located(("xpath","//div[@class = '_ac8f']")))
        # val = popup.get_attribute("outerHTML")
        # print(val)
        popup.click()

        # Notification pop up 
        if driver.find_element('xpath',"//div[contains(@class, 'x7r02ix') and contains(@role, 'dialog')]/div/div/div[3]/button[2]").is_displayed():
            driver.find_element('xpath',"//div[contains(@class, 'x7r02ix') and contains(@role, 'dialog')]/div/div/div[3]/button[2]").click()

    except TimeoutException :
        print("Something went wrong! Try Again")

def sear_api(query):

    header = {
        "Authorization": "Bearer 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"
    }

    data = {
    "model": "text-davinci-003",
    "prompt": query,
    "max_tokens": 100,
    "temperature": 0.5,
    "top_p": 1,
    "n": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
    }

    response = requests.post("https://api.openai.com/v1/completions",json =data,headers=header,)
    # print(response.status_code)
    python_data = response.json()
    # print(python_data)
    try :
        data = python_data["choices"][0]["text"]
        # speak("here is what i found sir")
        print(data)
        speak(data)

    except :
        print("Could not fetch ! ")
    return
        

# def who_search(query):
#     l = query.split()
#     if "Who" in query or "who" in query :
#         c = l.index("who")
#         l = l[c:]
#     # else :
#     #     for i in range(len(l)):
#     #         if l[i] == "the":
#     #             l[i] = ""
#     #             break 
#     #         else :
#     #             l[i] = ""
        
#     query = " ".join(l).strip()
#     speak("sure sir")
#     pywhatkit.search(query)
#     try:
#       result = wikipedia.summary(query, sentences = 1)
#     except wikipedia.exceptions.DisambiguationError as e:
#       print ("result could not search")
#       print()
#     except wikipedia.exceptions.PageError as e:
#       print ("result could not search")
#       print()
#     speak(result)
#     print(result)

# def what_search(query):
#     l = query.split()
#     if "What" in query or "what" in query :
#         c = l.index("what")
#         l = l[c:]
#     query = " ".join(l)
#     speak("sure sir")
#     pywhatkit.search(query)
#     try:
#         result = wikipedia.summary(query, sentences = 1)
#         speak(result)
#         print(result)
#     except wikipedia.exceptions.DisambiguationError as e:
#       print ("i am sorry sir result could not search")
#       print()
#     except wikipedia.exceptions.PageError as e:
#       print ("i am sorry sir result could not search")
#       print()

# def how_search(query):
    l = query.split()
    if "how" in query :
        c = l.index("how")
        l = l[c:]
    
    query = " ".join(l)
    speak("sure sir")
    pywhatkit.search(query)
    try:
        result = wikipedia.summary(query, sentences = 1)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print ("i am sorry sir result could not search")
        print()
    except wikipedia.exceptions.PageError as e:
        print ("i am sorry sir result could not search")
        print()