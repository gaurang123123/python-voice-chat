import datetime
import pyttsx3
import requests
import speech_recognition as sr
# import pyaudio 
import wikipedia
import webbrowser
import os
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your virtual voice assistant of Cmr Green Technology how may i help you??")


r = sr.Recognizer()
def takeCommand():

    try:
        with sr.Microphone() as mic:
            print("Listening...")
            r.adjust_for_ambient_noise(mic,duration=0.3)
            r.pause_threshold=1
            audio = r.listen(mic)
            speak("recognizing..")
            print("Recognizing...")
            # print("lis")
            text = r.recognize_google(audio,language='en-in')
            print("list2")
            text = text.lower()
            print("list3")
            # print("Listening...")

 
           
            # query = r.reco
            print("user said: \n",text)
    except Exception as e:
        print(e)
        print("Say that again please...")

        return "None"
    return text
# def sendEmail(to,content):

trigger = True
if __name__ == "__main__":

    wishMe()
    while trigger:
    # if 1:
        query = takeCommand()
    # logic for executing task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print("Searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=5)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'play song on youtube' in query:
            speak('which song do you want to play...')
            print('which song do you want to play...')
            query = takeCommand()
            print("playing on youtube...")
            speak("playing on youtube")
            pywhatkit.playonyt(query)
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather 
            api_key = "3d2952bc127d295815be912397a1a85d"
            # https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            print(city_name)
            complete_url = base_url + "q=" + city_name + "&appid =" + api_key

            # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=3d2952bc127d295815be912397a1a85d")
            print(response.json()['weather'][0]['main'])
            val = int(response.json()['main']['temp'])
            val = val - 273
            speak(str(val)+"degree celcius")
            # print((response.json()['main']['temp']-273)+)
            print(str(val)+"°C")
            x = response.json() 
             
            # if x["code"] != "404": 
            #     print("hello")
            #     y = x["main"] 
            #     current_temperature = y["temp"] 
            #     current_pressure = y["pressure"] 
            #     current_humidiy = y["humidity"] 
            #     z = x["weather"] 
            #     weather_description = z[0]["description"] 
            #     print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            # else: 
            #     speak(" City Not Found ")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[6]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time is {strtime}")

            speak(f"The Time is {strtime}")
        elif 'close' in query:
            trigger=False
        
          
            # query = query.replace("chatgpt","")
            # response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=3d2952bc127d295815be912397a1a85d")

            # response = 
            
            # result = wikipedia.summary(query,sentences=5)
            # print("According to wikipedia")
            # speak("According to wikipedia")
            # print(result)
            # speak(result)
        elif 'email to gaurang' in query:
            try:
                speak("what you want to say?")
                content = takeCommand()
                to = "gaurangag06@gmail.com"
                # sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry unable to send")


    # speak("Good morning gaurang how are you")



    