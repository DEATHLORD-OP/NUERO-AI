# NOTE: PLEASE READ THE EXTRA NOTES CAREFULLY AS IT WILL HELP YOU IN THIS PROGRAM

# IMPORT STATEMENTS

import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib   # IMPORTED FOR OTHER PURPOSES (ALTHOUGH NOT IN USE BUT IMPORT IT AS YOU MAY GET AN ERROR)
import pyaudio   # IMPORTED FOR OTHER PURPOSES (ALTHOUGH NOT IN USE BUT IMPORT IT AS YOU MAY GET AN ERROR)
import turtle
import tkinter as tk

# SOME STATEMENTS ARE NOT BUILT IN. IT NEED TO BE IN THE INTREPRETER OR DOWNLOADED IN SYSTEM.

try:  # 'TRY' USED SO THAT NO ERROR IS SHOWN

    # SPEECH THROWER

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    # FUNCTIONS

    def speak(audio):  # LETS THE COMPUTER SPEAK
        engine.say(audio)
        engine.runAndWait()


    def wishMe():  # WISHES THE USER
        hour = int(datetime.datetime.now().hour)

        if (hour >= 0 and hour < 12):
            speak("GOOD MORNING BOSS.")

        elif (hour >= 12 and hour < 16):
            speak("GOOD AFTERNOON BOSS.")

        else:
            speak("GOOD EVENING BOSS")

        speak("HOW MAY I HELP YOU?")


    def close():  # TERMINATES THE PROGRAM
        sys.exit()


    def takeCommand():  # TAKES VOICE COMMAND OF THE USER

        r = sr.Recognizer()

        with sr.Microphone() as source:
            speak("LISTENING...")
            r.pause_threshold = 0.7
            r.energy_threshold = 300
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            my_lovely_turtle.clear()
            my_lovely_turtle.write(f"USER SAID: {query}\n", align='center', font='Arial')

        except Exception as exc:
            my_lovely_turtle.clear()
            my_lovely_turtle.write("SORRY COULD NOT RECOGNIZE THAT", align='center', font='Arial')
            return "None"

        query = query.lower()

        # TASKS FOR NEURO

        # SEARCH WIKIPEDIA TASK
        if "wikipedia" in query:
            speak("OK BOSS! SEARCHING.")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2, auto_suggest=True, redirect=True)
                speak("ACCORDING TO WIKIPEDIA")
                my_lovely_turtle.clear()
                my_lovely_turtle.write(query.upper(), align='center', font='Arial')
                speak(result)

            except Exception as e:
                speak("SORRY NOTHING WAS FOUND")

        # HOW ARE YOU TASK
        elif "how are you" in query:
            speak("I AM FINE BOSS")

        # OPENING YOUTUBE TASK
        elif "open youtube" in query:
            speak("OK BOSS ! OPENING YOUTUBE")
            webbrowser.open("youtube.com")

        # OPENING SPOTIFY TASK
        elif "open spotify" in query:
            speak("OK BOSS ! OPENING SPOTIFY")
            webbrowser.open("open.spotify.com")

        # HAI TASK (THE COMPUTER RECOGNIZES HI AS HAI)
        elif "hai" in query:
            speak("HI BOSS!")

        # TIME TELLING TASK
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H :%M")
            speak(f"THE TIME IS {time}\n")

        # TO CLOSE NEURO TASK
        elif "exit" in query:
            speak("BYE BOSS")
            sys.exit()

        # OPENING VISUAL CODE TASK
        elif "open visual code" in query:
            vs_code = "C:\\Users\\91993\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("OK BOSS OPENING VISUAL CODE EDITOR")
            os.startfile(vs_code)

        # OPENING VALORANT (GAME) TASK
        elif "open valorant" in query:
            speak("OPENING VALORANT")
            valorant = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(valorant)

        # SEARCHING THE WEB TASK
        elif "search" in query:
            speak("SEARCHING")
            webbrowser.open(query)

        # OPENING MS WORD TASK
        elif "open ms word" in query:
            speak("OPENING M S WORD")
            ms_word = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(ms_word)

        # OPENING MS EXCEL TASK
        elif "open ms excel" in query:
            speak("OPENING M S EXCEL")
            ms_excel = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(ms_excel)

        # WISHING BYE TASK
        elif "bye" in query:
            speak("BYE BOSS")

        # OPENING MS OFFICE TASK
        elif "open ms office" in query:
            speak("OPENING M S OFFICE")
            ms_office = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge_proxy.exe"
            os.startfile(ms_office)

        # OPENING MS POWERPOINT TASK
        elif "open ms powerpoint" in query:
            speak("OPENING M S POWERPOINT")
            ms_pwr = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ms_pwr)

        # OPENING PYCHARM TASK (WON'T WORK IF YOU RUN THIS IN PYCHARM)
        elif "open pycharm" in query:
            speak("OPENING PY CHARM")
            py_charm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
            os.startfile(py_charm)

        # OPENING OPERA WEB BROWSER TASK
        elif "open opera" in query:
            speak("OPENING OPERA GX WEB BROWSER")
            opera = "C:\\Users\\91993\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(opera)

        # ASKING BIRTH DATE TASK
        elif "when were you born" in query:
            speak("I WAS BORN ON JANUARY 1, 2022")

        # AGE TASK
        elif "what is your age" in query:
            speak("I AM A FEW MONTHS OLD.")

        # ABUSING (IDIOT) TASK
        elif "you are an idiot" in query:
            speak("NO! NOT A IDIOT LIKE YOU")

        # ABUSING (IDIOT) TASK
        elif "are you an idiot" in query:
            speak("NO! NOT A IDIOT LIKE YOU")

        # WISHING GOOD EVENING TASK
        elif "good evening" in query:
            speak("GOOD EVENING BOSS")

        # WISHING GOOD MORNING TASK
        elif "good morning" in query:
            speak("GOOD MORNING BOSS")

        # WISHING GOOD AFTERNOON TASK
        elif "good afternoon" in query:
            speak("GOOD AFTERNOON BOSS")

        # ASKING NAME TASK
        elif "what is your name" in query:
            speak("MY NAME IS NEURO")

        # WISHING THANK YOU TASK
        elif "thank you" in query:
            speak("YOUR WELCOME BOSS")

        # HATING TASK
        elif "i hate you" in query:
            speak("PLEASE DON'T HATE ME")

        # SAYING BEST TASK
        elif "you are the best" in query:
            speak("THANKS BOSS")

        # OPENING SNIPPING TOOL TASK
        elif "open snipping tool" in query:
            speak("OK BOSS. OPENING SNIPPING TOOL")
            snip_tool = "%windir%\system32\SnippingTool.exe"
            os.startfile(snip_tool)

        # HELP TASK
        elif "help me" in query:
            speak("YES BOSS. HOW CAN I HELP YOU?")

        # OPENING FILE EXPLORER TASK
        elif "open file explorer" in query:
            speak("OK BOSS. OPENING FILE EXPLORER")
            file = "C:\\Users\\91993\\Downloads"
            os.startfile(file)

        # OPENING MINECRAFT TASK
        elif "open minecraft" in query:
            speak("OK BOSS. OPENING MINECRAFT")
            minecraft = "C:\\Users\\91993\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(minecraft)

        # WISHED IF NO TASK IS MATCHED
        else:
            speak("SORRY BOSS CANNOT HELP YOU WITH THAT.")

        # QUERY IS THE SPEECH SAID BY THE USER
        return query

    # RUNS COMMANDS

    if __name__ == '__main__':

        # CANVAS

        root = tk.Tk()
        root.title("NEURO")
        root.iconbitmap('neuro_icon.bmp')
        canvas = tk.Canvas(root)
        canvas.config(width=700, height=500)
        canvas.pack(side=tk.LEFT)

        # SCREEN

        screen = turtle.TurtleScreen(canvas)
        screen.bgcolor("black")
        screen.bgpic("neuro.gif")

        # JARVIS BUTTONS

        # CALLING BUTTON
        button1 = tk.Button(root, text="CALL   NEURO", command=takeCommand)
        button1.pack()

        # CLOSING BUTTON
        button2 = tk.Button(root, text="CLOSE NEURO", command=close)
        button2.pack()

        # TURTLE

        my_lovely_turtle = turtle.RawTurtle(screen, shape="square")
        my_lovely_turtle.color('white')
        my_lovely_turtle.hideturtle()
        my_lovely_turtle.left(90)

        # COMMANDS

        wishMe()

        # SCREEN LOOPER

        root.mainloop()

except Exception as e:   # SYSTEM THROWS THIS IF ANY ERROR OCCURRED
    speak("SORRY BOSS. SOMETHING WENT WRONG.")

'''
EXTRA NOTES :-

ABOUT: 

THIS AI IS NAMED NEURO. NEURO IS NOT ONE OF THE AI WHO PERFORMS PRETTY WELL. IT IS MADE USING PYTHON.
IT IS NOT PROPERLY AN AI. IT IS AN AI OR NOT, IS NOT CLARIFIED, BECAUSE AI IS INTELLIGENCE DONE BY
MACHINES, AS OPPOSED TO NATURAL INTELLIGENCE BY HUMANS (ANIMALS). THIS AI DOES NOT LEARN ON IT'S OWN, BUT
PERFORMS TASKS WHICH ARE COMMONLY PERFORMED BY THE USER ON A COMPUTER. IT IS TECHNICALLY AN AI.

DRAWBACKS:

* DOES NOT ALWAYS RECOGNIZES THE SPEECH OF THE USER. (DUE TO QUALITY OF MIC)
* DOES NOT PERFORMS ALL TASKS
* OLD LOOK

ADVANTAGES: 

* PERFORMS COMMON TASKS
* USER FRIENDLY
* YOU CAN COMMUNICATE WITH IT JUST LIKE A HUMAN

CREDITS: 

NAME: SANIDHYA JAIN
WORK: STUDENT
QUALIFICATIONS: 10 TH STANDARD STUDENT

NOTE : SOME APPLICATIONS MIGHT NOT BE INSTALLED ON YOUR DEVICE OR MAY BE NOT ON THE DESIRED FILE LOCATION. IN THIS CASE YOU MIGHT GET AN ERROR. IN ORDER TO
SOLVE THIS FOLLOW THE STEPS BELOW.

STEP 1: OPEN THE FILE LOCATION OF THE APPLICATION(s)
STEP 2: RIGHT - CLICK THE FILE
STEP 3: CLICK ON PROPERTIES
STEP 4: THERE YOU WILL FIND THE TARGET OF THE FILE. COPY THAT
STEP 5: PASTE IT IN THE STRING VARIABLE.

EXAMPLE :-
elif "open minecraft" in query:
            speak("OK BOSS. OPENING MINECRAFT")
            minecraft = "C:\\Users\\91993\\AppData\\Roaming\\.minecraft\\TLauncher.exe" (THIS THE TARGET OF MY FILE - MINECRAFT)
            os.startfile(minecraft)

 minecraft = "C:\\Users\\91993\\AppData\\Roaming\\.minecraft\\TLauncher.exe" (REPLACE THE CONTENT IN THE VARIABLE WITH THE TARGET OF YOUR FILE - MINECRAFT)
 
 NOTE: PLEASE PUT A BACKSLASH(\) BEFORE OR AFTER EVERY BACKSLASH(\) OR REPLACE THE SLASH(/) WITH A DOUBLE BACKSLASH(\\) (THIS FOR THE FILE TARGET ONLY)
 
'''
