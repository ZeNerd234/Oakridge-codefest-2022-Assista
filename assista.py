import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import requests
import wolframalpha
import time
import subprocess
import smtplib
import random
from email.message import EmailMessage
import html
from translate import Translator
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image      


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  

    else:
        speak("Good Evening!")  

    speak("I am Assista! Your Educational and Therapist Bot!. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query




    

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()





        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'translator' in query:
            speak("Opening a seperate translator window")
            #Tkinter root Window with title
            root = Tk()
            root.title("Translator")

            #Creating a Frame and Grid to hold the Content
            mainframe = Frame(root)
            mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
            mainframe.columnconfigure(0, weight = 1)
            mainframe.rowconfigure(0, weight = 1)
            mainframe.pack(pady = 100, padx = 100)


            #variables for dropdown list
            lan1 = StringVar(root)
            lan2 = StringVar(root)

            #Translator function
            def translate():
                translator= Translator(from_lang=lan1.get(),to_lang=lan2.get())
                translation = translator.translate(var.get())
                var1.set(translation)


                

                #choices to show in dropdown menu
                choices = { 'English','Hindi','Spanish','German','Italian','Russian','French','Arabic','Chinese','Japenese','Korean','Persian','Latin','Greek','Swedish'}
                #default selection for dropdownlists
                lan1.set('English')
                lan2.set('Hindi')

                #creating dropdown and arranging in the grid
                lan1menu = OptionMenu( mainframe, lan1, *choices)
                Label(mainframe,text="Select a language").grid(row = 0, column = 1)
                lan1menu.grid(row = 1, column =1)

                lan2menu = OptionMenu( mainframe, lan2, *choices)
                Label(mainframe,text="Select a language").grid(row = 0, column = 2)
                lan2menu.grid(row = 1, column =2)

                #Text Box to take user input
                Label(mainframe, text = "Enter text").grid(row=2,column=0)
                var = StringVar()
                textbox = Entry(mainframe, textvariable=var).grid(row=2,column=1)

                #textbox to show output
                #label can also be used
                Label(mainframe, text = "Output").grid(row=2,column=2)
                var1 = StringVar()
                textbox = Entry(mainframe, textvariable=var1).grid(row=2,column=3)

                #creating a button to call Translator function
                b=Button(mainframe,text='Translate',command=translate).grid(row=3,column=1,columnspan=3)






                



            

