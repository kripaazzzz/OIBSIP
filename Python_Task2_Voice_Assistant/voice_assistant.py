import speech_recognition as sp
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import subprocess

listener = sp.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()
     

def input_instruction ():
    try:
        with sp.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            print(instruction)
            if "nova" in instruction:
                instruction = instruction.replace("nova", "").strip()
                print(instruction)
                return instruction

            else:
                return ""
    except Exception as e:
        print(e)
        talk("Please repeat")
        return ""

def play_nova():

    instruction = input_instruction()
    print(instruction)

    if ('good morning' in instruction or
    'hello' in instruction or 
    'good evening' in instruction):
        talk("Hello Kripa, how can I help you today?")
    
    elif 'play' in instruction:
        song = instruction.replace('play', "").strip()
        talk("playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        print("TIME BLOCK ENTERED")
        current_time = datetime.datetime.now().strftime('%I:%M%p')
        print(current_time)
        talk("Current time is " + current_time)

    elif 'date' in instruction:
        print("DATE BLOCK ENTERED")
        current_date = datetime.datetime.now().strftime('%d /%m /%Y')
        print(current_date)
        talk("Today's date is " + current_date)

    elif 'open chrome' in instruction:
        talk("Opening Chrome")
        webbrowser.open('https://www.google.com')

    elif 'open notepad' in instruction:
        talk("Opening Notepad")
        subprocess.Popen('notepad.exe')

    elif 'open spotify' in instruction:
        talk("Opening Spotify")
        subprocess.Popen(
            r"C:\Users\KRIPA\AppData\Local\Microsoft\WindowsApps\Spotify.exe"
        )

    elif 'search' in instruction:
        search = instruction.replace('search','').strip()
        talk("Searching " + search)
        webbrowser.open(
            "https://www.google.com/search?q=" + search
        )

    elif 'stop' in instruction:
        talk("Goodbye")
        return False

    else:
        talk("Sorry, I didn't understand.")

    return True

while True:
    if play_nova() == False:
        break
