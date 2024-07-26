from playsound import playsound
import eel
import pyttsx3 as pt
import speech_recognition as sr
import pywhatkit as pw
import os
import pyautogui as pti
import time
import pvporcupine
import pyaudio
import struct
import hugchat
import google.generativeai as genai
import psutil
import requests
# import speedtest


genai.configure(api_key="AIzaSyDjzfkOA0P0kVmCHJ_GsNVnWqVR1hTwF6o")

def ans(hh):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }


    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[]
    )
    response = chat_session.send_message(f"{hh}")
    print(response.text)
    engine.say(response.text)
    engine.runAndWait()


input=sr.Recognizer()
def playassistantsound():
    music_dir='C:\\Users\\hEART rIDER\\Desktop\project\\audio\\y2mate.com - Glitch Sound Effect Digital.mp3'
    playsound(music_dir)
    
engine=pt.init('sapi5')
voices = engine.getProperty('voices')         
engine.setProperty('voice', voices[1].id) 
@eel.expose
def palsy():
    engine.say("hello Sir")
    engine.runAndWait()
    engine.say("i'm palsy")
    engine.runAndWait()

@eel.expose
def input_rec():
    with sr.Microphone() as suno:
        l=["palsi","palsy","pulsy","pulsi","alsi","alsy","pubg","policy","police","hey","hi","he","hh","hye","hy"]
        print("listing....")
        eel.DisplayMessage('listing...')
        input.pause_threshold = 1
        input.adjust_for_ambient_noise(suno)
        aud=input.listen(suno,10,6)
        def saaf(r):
            i=0
            rp=r.split(" ")
            for j in l:
                if l[i] in rp:
                    rp.remove(l[i])
                i=i+1
            rp1=" ".join(rp)
            return rp1
        try:
            eel.DisplayMessage('recoginze...')
            query1=input.recognize_google(aud, language='en-in').lower()
            query=query1.lower()
            u=0
            j=""

                    
            if "play" in query.lower():
                engine.say("playing")
                engine.runAndWait()
                print(saaf(query))
                pw.playonyt(saaf(query))
            elif "on google" in query.lower():
                
                engine.say("opening")
                engine.runAndWait()
                print(saaf(query))
                pw.search(saaf(query))
                # print(re)
            elif "open" in query.lower():
                t1=saaf(query)
                t=t1.replace("open","").lower()
                print(t)
                os.system('start '+t)
            elif "time" in query:
                times=time.strftime("%H :""%M :"" %p")
                print(times)
                engine.say("it's"+times)
                engine.runAndWait()
            elif "take screenshot" in query:
                print(query)
                pti.hotkey("cmd",'shift','s')
            elif "shutdown" in query:
                os.system('Shutdown /s /t 1')
            elif "restart" in query:
                os.system('Shutdown /r /t 1')
            
            elif "how much power we have" in query or "battery" in query:
                battery=psutil.sensors_battery()
                percentage=battery.percent
                s=f'the battery is {percentage} percent'
                engine.say(s)
                engine.runAndWait()
            elif "weather" in query:
                engine.say("the weather is")
                engine.runAndWait()
                pw.search("what is the weather of faisalabad right now")
            
            elif "WhatsApp" in query:
                co={"home":"+92","writer":"+928","Shabir":"+92"} #create your own contactlist in dictionary name as key and number as a value of key
            ren=sr.Recognizer()
            try:
                with sr.Microphone() as ma:
                    print("on which you would send your msg : ",end="")
                    ren.adjust_for_ambient_noise(ma,duration=0.3)
                    sun=ren.listen(ma)
                    cont=ren.recognize_google(sun)
                    print(cont)
                    
                    print("What msg would you wants to send ",end=": ")
                    
                    zi=ren.listen(ma)
                    msg=ren.recognize_google(zi)
                    
                    pw.sendwhatmsg_instantly(co[cont],msg,19,25)
            except sr.UnknownValueError:
                print("i can't hear your voice ")
            
            else:
                t=saaf(query)
                ans(t)
        except sr.UnknownValueError:
            engine.say("the voice is not clear")
            engine.runAndWait()
            
            
