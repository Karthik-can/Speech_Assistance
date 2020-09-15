import speech_recognition as sr # Recognise Speech
import playsound # To play an audio file
from gtts import gTTS # Google text to speech
import random
from time import ctime # Get time details
import webbrowser # Open browser
import ssl
import certifi
import time
import os # To remove created audio files
from PIL import Image
import subprocess
import pyautogui # Screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests
#import pyaudio


class person:
    name = ""
    def setName(self,name):
        self.name = name

class asis:
    nema = ""
    def serName(self,name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speek(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # Initialise a recogniser
#Listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # Microphone as source
        if ask:
            engine_speek(ask)

        audio = r.listen(source,5,5) # Listen for the audio via source
        print("Done Listening")
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio) # Convert audio to text
        except sr.UnknownValueError: # Error:Recognizer does not understand
            engine_speek("I did not understand!")
        except sr.RequestError:
            engine_speek("Sorry,The Service is Down") # Error:Recognizer is not connected
        print(">>",voice_data.lower()) # Print the user said
        return voice_data.lower()

#Get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string,lang='en') # Text to speech(Voice)
    r = random.randint(1,20000000)
    audio_file = 'audio'+str(r)+'.mp3'
    tts.save(audio_file) # Save as mp3
    playsound.playsound(audio_file) # Play the audio file
    print(asis_obj.name + ":",audio_string) # Print the user said
    os.remove(audio_file) # Remove audio file

def respond(voice_data):
    # Greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["Hey,how can I help you"+ person_obj.name,"hey,what's up?"+person_obj.name,"I'm listening"+person_obj.name,"how can I help you?"+person_obj.name,"hello"+person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # Name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name},{person_obj.name}") # Gets user name from voice input
        else:
            engine_speak(f"My name is {asis_obj.name}.what's your name?") # Incase you didnt mention your name

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay,i will remember that"+person_name)
        person_obj.setName(person_name) # Remember name in person object

    if there_exists(["what is my name"]):
        engine_speak("Your name must be"+person_obj.name)

    if there_exists(["Your name should be"]):
        asis_name = voice_data.split('be')[-1].strip()
        engine_speak("okay,i will remember that my name is "+asis_name)
        asis_obj.serName(asis_name) # Remeber name in asis object
#   # Greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("Im very well,thanks for asking"+person_obj.name)

    # Time
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] =="00":
            hours='12'
        else:
            hours =time[0]
        minutes = time[1]
        time = hours+'Hours and'+minutes+'minutes'
        engine_speak(time)

    # Search Google
    if there_exists(["search for"])  and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speek("Here is what I found for" + search_term +"on google")

    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.replace("search","")
        url = "https://google.com/search?q=" +search_term
        webbrowser.get().open(url)
        engine_speek("Here is what I found for" + search_term + "on google")

    # Search Youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query="+search_term
        webbrowser.get().open(url)
        engine_speek("Here is what I found for " + search_term + "on youtube")

     # get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()

    #  weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    # stone paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]

        cmove=random.choice(moves)
        pmove = voice_data

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        # engine_speak("hi")
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")

        # 11 toss a coin
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose " + cmove)

        # 12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply' or 'x':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

        # 13 screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')

        # 14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition = record_audio("what do you need the definition of")
        url = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + definition)
        soup = bs.BeautifulSoup(url, 'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found ' + definitions[1])
            else:
                engine_speak('Here is what i found ' + definitions[2])
        else:
            engine_speak("im sorry i could not find the definition for " + definition)

    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("bye")
        exit()

        # Current city or region
    if there_exists(["where am i"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        engine_speak(f"You must be somewhere in {loc}")

        # Current location as per Google maps
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")

    if there_exists("stop"):
        exit()

time.sleep(1)
person_obj = person()
asis_obj = asis()
asis_obj.name = "Jack Sparrow"
person_obj.name = ""
engine = pyttsx3.init()

while(1):
    voice_data = record_audio("Recording") # Get the voice input
    print("Done")
    print("Q:",voice_data)
    respond(voice_data) # Respond