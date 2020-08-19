import pygame
import os
import subprocess
import requests
from bs4 import BeautifulSoup
import textwrap
import RPi.GPIO as GPIO
import time
import speech_recognition as sr
import sys
import Adafruit_DHT
import datetime
import random

#Program to play music
def playmusic():
folder=os.listdir(os.getcwd())
for files in folder:
if files.endswith(".mp3"):
print(files)
pygame.mixer.init()
pygame.mixer.music.load(files)
pygame.mixer.music.set_volume(100.0)
pygame.mixer.music.play()

#Program to stop music
Def Stopmusic():
Pygame.mixer.music.stop()


#Program to fetch,display and read news
def readnews():
url = "https://www.ndtv.com/top-stories"

r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

g_data = soup.find_all("div",{"class":"nstory_header"})

for item in g_data:
shorts = textwrap.wrap(item.text, 125)
for sentence in shorts:
print(sentence+"\n")
os.system("espeak -ven+m3 -s150 ' " + sentence + " '  2>/dev/null")
#Program to Turn On Lights
def TurnOnLights():
GPIO.setmode(GPIO.BCM)
RELAY=4
GPIO.setup(RELAY,GPIO.OUT)
GPIO.output(RELAY,GPIO.HIGH)

#Program to Turn Off Lights
def TurnOffLights():
GPIO.setmode(GPIO.BCM)
RELAY=4
#GPIO.setwarnings(False)
GPIO.setup(RELAY,GPIO.OUT)
GPIO.output(RELAY,GPIO.LOW)


#The Main Frame
sensor=Adafruit_DHT.DHT11
quote=random.randint(1,8)

while(1):
now=datetime.datetime.now()
Humidity,Temperature=Adafruit_DHT.read_retry(sensor,17)
tdy=(datetime.datetime.today().strftime("%A"))
print('Temp:{0:0.1f}C\n\nHumidity:{1:0.1f}%\t\t\t\t\t\t'.format(Temperature,Humidity)+tdy+'\n\n'+
now.strftime("\t\t\t\t\t\t\t%d-%m-%Y\n\n\t\t\t\t\t\t\t\t\t%H:%M:%S\r"))
c={1:"Have a great day",2:"We are all a mess,but its how we keep it together that makes us beautiful!",
3:"Beauty begins the moment you decide to beyou!",
4:"Smile in the mirror!It makes a great difference in life",5:"I myself entire am made entirely of flaws,stitched together with good intentions",
6:"Elegance is the only beauty that never fades",7:"Self love isn't selfish!",8:"The beauty you see in me is a reflection of you!"}
r = sr.Recognizer()
with sr.Microphone() as source:
os.system('clear')
print('Temp:{0:0.1f}C\n\nHumidity:{1:0.1f}%\t\t\t\t\t\t'.format(Temperature,Humidity)+tdy+'\n\n'+
now.strftime("\t\t\t\t\t\t\t%d-%m-%Y\n\n\t\t\t\t\t\t%H:%M:%S\r"))
if(now.hour>=0 and now.hour<12):
print("\n\n\n\n\n\n\t\t\t\tGood Morning\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
elif(now.hour>=12 and now.hour<17):
print("\n\n\n\n\n\n\t\t\t\tGood Afternoon\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n")
elif(now.hour>=17 and now.hour<21):
print("\n\n\n\n\n\n\t\t\t\tGood Evening\n\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n")
else:
print("\n\n\n\n\t\t\t\tGood Night\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
print("\n"+c[quote])

print("\n\n\n\t\t\t\tSay something!")

audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
ch=r.recognize_google(audio)
print("\n\t\t\t\tGoogle Speech Recognition thinks you said " + r.recognize_google(audio))
time.sleep(2)
if(ch=="read news"):
readnews()
elif(ch=="play music"):
playmusic()
elif(ch=="turn on light" or ch=="turn on lights"):
TurnOnLights()
elif(ch=="turn off light" or ch=="turn off lights"):
TurnOffLights()

except sr.UnknownValueError:
print("\n\n\t\t\t\tGoogle Speech Recognition could not understand audio ")
time.sleep(2)
except sr.RequestError as e:
print("Could not request results from Google Speech Recognition service; {0}".format(e))
