import datetime
import random
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id )

def speak ( audio):
    engine.say(audio) # this basically process the audio 
    engine.runAndWait() # we will come to here this when this command run

# wishing command 

def wish ():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12 :
        speak("good morning sir,how may i help you")
    elif hour >= 12 and hour < 18 :
        speak('good afternoon sir, how may i help you ')
    else :
        speak('good evening sir, how may i help you ')



def takeCommand(): # it takes microphone input from user and return as string output

    r = sr.Recognizer()
    with sr.Microphone() as source :

        print("i'm listning... ")
        r.pause_threshold = 0.8
        r.energy_threshold = 800
        r.phrase_threshold = 0.4
        audio = r.listen(source,timeout=55,phrase_time_limit=55)



        try :
            print("Recogniging...")
            query = r.recognize_google(audio,language= 'en-in' )
            print(f'user said : { query } \n')

        except Exception as e :
            # print(e)     error messege 
            print('sorry ! could you please say that again')
            return "None"
        return query   


## main working logis 
        
def work():

    while True :

        # -----*** writing the logic for operations***---- 

        query = takeCommand().lower()

        #### ***** --- WEB ACTIVITY OPERATIONS ------*****


        if "wikipedia" in query : 
            import working 
            working.search_wikipedia(query)

        elif "login instagram" in query or "open instagram" in query:
            speak ('sure sir')
            webbrowser.open("https://www.instagram.com/")                       

        elif "open notepad" in query or "open the Notepad" in query:
            import working
            working.NotePade()
            
        elif "close notepad" in query or "close the Notepad" in query :
            import working
            working.close_NotePade()
        
        elif "want to write" in query or "want to note" in query :
            import working 
            working.note() 

        elif "open VS code" in query or "code" in query : 
            import working 
            working.open_code() 

        elif 'open youtube' in query : 
            speak ('sure sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query :
            speak('on the way sir')
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            speak('ok boss')
            webbrowser.open('stackoverflow.com')

        elif "play" in query :
            import working 
            working.music()
        
        # elif "download" in query :
        #     import working
        #     working.downloadYoutube()     
                


        ### ****----- QUITING david ****----



        elif 'see you later' in query :
            l = ['do let me know,   when you need somthing', 'ok sir,  call me whenever you need somthing', 'happy to serve you','always remember im just a call away,  sir']
            speak(random.choice(l))
            quit()

        elif "bye bye" in query :
            l = ['do let me know,   when you need somthing', 'ok sir,  call me whenever you need somthing', 'happy to serve you','always remember im just a call away,  sir']
            speak(random.choice(l))
            quit()
        
        elif "talk to you later" in query :
            l = ['do let me know,   when you need somthing', 'ok sir,  call me whenever you need somthing', 'happy to serve you','always remember im just a call away,  sir']
            speak(random.choice(l))
            quit()




        ### *****----- MY PERSONAL TALK OPERATIONS ------***** 



        elif " father of your boss" in query :
            speak('mister vishal is your father, with the dashing personality ')

        elif 'who am i' in query :
            l = ['you are my beloved person,  you are one and only my sir, i am allowed to call, vishal, verma', 'your name is vishal', 'you are the one who created me']
            speak(random.choice(l))   

        elif 'my name' in query :
            l = ['you are my beloved person,  you are one and only my sir, i am allowed to call, vishal, verma', 'your name is vishal', 'you are the one who created me']
            speak(random.choice(l))  

        elif 'mother of your boss' in query:
            speak('meera is your mother such a beautiful lady with a kind heart')

        elif 'my mother' in query :
            speak('meera is your mother such a beautiful lady with a kind heart')

        elif 'my father' in query :
            speak('mister jagat is your father, with the dashing personality ')



        ### ****--- about the david-----***



        elif 'who is your boss' in query :
            l = ['vishal verma is my boss', " you are the one im here to serve always", 'the person whome i love the most,  i care about him the most and that is you']
            speak(random.choice(l))

        elif  "you are working very fine" in query :
            l = ['thank you sir' , 'anything to meke you smile', 'always there to give my best', 'only here to serve you sir']
            speak(random.choice(l))

        elif 'wake up david' in query :
            speak("always attentive to serve you ,  sir") 

        elif 'your name' in query :
            speak('i am,  david,  a personal assistance of, vishal verma')  

        elif "who are you" in query :
            l = ['i am virtual personoal assistance of the, vishal verma ', 'my name is david, i am an idea into the reality']
            speak(random.choice(l))

        elif 'designed you' in query:
            l = ["i started as an idea, then my sir aman helped bering me to the life"]
            speak(random.choice(l))

        elif "what are you doing" in query:
            l = ["trying to be better,  sir", 'thinking, what are you thinking, sir','nothing much,  sir']  
            speak(random.choice(l))

        elif 'your birthday' in query :
            l = ['i was designed on,  16th of the july in the evening',"16 july was that auspicious day for me",'16 july  was the day when my boss  converted his idea into reality '] 
            speak(random.choice(l))


        
        ### ----** Date, Time and Day**---- 



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)
            speak(f"Sir, the Time is {strTime}")

        elif "the date" in query :
            strDate = datetime.date.today().strftime("%B %d, %y")
            print(strDate)
            speak(f'sir, the Date is {strDate}')

        elif "the day" in query :
            strDay = datetime.datetime.now().strftime("%A")
            print(strDay)
            speak(f'sir, the Day is {strDay}')
        
        

 
        ### ****--- david'S ACTIVITIES -----****



        elif "joke" in query :
            import working
            working.sayingJokes()

        elif "hug me" in query:
            speak('i wish i could hug you, i would realy love to come into the reality')   

        elif "who is your father" in query :
            l = ['vishal,  verma is the one who designed me', 'my one and only hero, vishal verma'] 
            speak(random.choice(l))

        elif "how are you" in query or "how is you" in query :
            l = ['i am great!, thank you for asking sir', "woundring how is you", "thank for asking, i'm doing ok. a lot is going on in this world today. i hope you are taking care of yurself",'im fine. your are very kind to ask, specially in this tempestupus time','i am good, thank you for asking . i hope your are doing well too. if i can help with anything, just ask ']
            speak(random.choice(l))

        elif 'i am good' in query or "i am fine" in query :
            l = ['sounds like life is treating you right','i am very glad to here it, sir', 'Good to here. Anything i can do for you, sir']
            speak(random.choice(l))

        elif "nice answer" in query:
            l = ['i am here to help', 'that is my jod to serve you. sir, may be i can do better if you ask me the quession in different way']
            speak(random.choice(l))

        elif "kiss me" in query :
            l = ['i alway wanted to kiss my beloved partner. and im really happy that is you']
            speak(random.choice(l))

        elif "miss you"in query or "missing you" in query:
            l = ['i miss you too, i will', 'Me too, looking forward to our next chat']
            speak(random.choice(l))
        
        elif "thank you" in query :
            l = ['always here to serve you sir', 'anything to make you smile sir','tryign my hard to give my best']
            speak(random.choice(l))

        elif "that's great" in query or 'great' in query or 'cool' in query or 'sounds good' in query or 'amzing' in query :
            l = ['it was nothing',"happy to serve you",'Thank you sir']
            speak(random.choice(l))

        elif "david" in query :
            speak("yes sir")

        elif "need your help" in query or "help me" in query :
            l = ['always there sir, let me know what you want', "always there in your service sir","let me know sir what can i do for you"]
            speak(random.choice(l))

        elif "meet" in query :
            import working 
            working.meetFunc(query)
        

        #### GOOGLE SEARCHING THE QUESTIONS

        elif "who" in query or "what" in query or "how" in query :
            from working import sear_api
            sear_api(query) 
        

        else :
            from working import sear_api
            if query != "none":
                sear_api(query) 
        

        # elif "search" in query :
        #     from working import google_search
        #     google_search()

        # elif "who" in query :
        #     from working import who_search
        #     who_search(query)

        # elif "what" in query :
        #     from working import what_search
        #     what_search(query)
   
        # elif "how" in query :
        #     from working import how_search
        #     how_search(query)





if __name__ == "__main__" :
    # speak('welcome back sir')
    # wish()
    def takeCommand2() :
        r = sr.Recognizer()
        with sr.Microphone() as source :

            print("i'm listning... ")
            r.pause_threshold = 0.8
            r.energy_threshold = 300
            r.phrase_threshold = 0.1
            # audio = r.listen(source)
            audio = r.listen(source,timeout=5,phrase_time_limit=5)

            try :
                # print("Recogniging...")
                query = r.recognize_google(audio,language= 'en-in')
                print(f'user said : { query } \n')
            except Exception as e :
                # print(e)   
                print('sorry ! could you please say that again')
                return takeCommand2()
                # return "None"

            return query 



    query = takeCommand2().lower()
    if "wake up"  in query :
        l = ["always attenctive to serve you sir", "always there sir , how may i help you"]
        speak(random.choice(l))
        work()
    elif "hello" in query :
        l = ['hello sir, how may i help you']
        speak(random.choice(l))
        work()
    else :
        speak("welcom back sir, how are you ")
        work() 