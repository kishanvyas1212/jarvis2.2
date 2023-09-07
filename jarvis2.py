from jarvis import VoiceAssistant
import json
import datetime
import re
import random
import wolframalpha
import pyautogui
import time
from jarvis.config.configuration import wolframalphaid 
import pprint
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import threading
import time
import imaplib
from email.message import EmailMessage
from jarvis.features.gui import Ui_MainWindow

import sys
obj = VoiceAssistant()
file_path_wolframalph = 'jarvis\database\wolframalpha_responses.json'
file_pathgreet = 'jarvis\database\greet.json'
file_pathgreetres = 'jarvis\database\greetres.json'
file_negative = 'jarvis\database\intents.json'
all_app_json = 'jarvis\\database\\all_applications.json'
positive_res = 'jarvis\\database\\postiveres.json'
def searchpath(path):
    with open(path, 'r') as file:
        return json.load(file)

Negative = searchpath(file_negative)
pos_res = searchpath(positive_res)
GREETINGS = searchpath(file_pathgreet)
GREETINGS_RES = searchpath(file_pathgreetres)
calltobard = ['goole bard','open bard','search on bard','search on google bard','seach on google bird','search on bird']


class otherfun:
    def sendername():
            obj.Speak('Sir, whom you want to send email ?')
            sender = obj.mic_input()
            if sender != "none":
                obj.send_email(sender)
                
            elif any(command in sender for command in Negative):
                obj.Speak('Ok sir, skipping it')
            else:
                obj.Speak('Sir please say again')
                otherfun.sendername()


    def computational_intelligence(question):
        try:
            client = wolframalpha.Client(wolframalphaid)
            answer = client.query(question)
            
            print(answer)
            answer1 = next(answer.results).text
            # print(answer1)
            data = {
            "query": question,
            "response": answer
                }
            print(answer)
            # Check if the JSON file already exists
            try:
                with open(file_path_wolframalph, "r") as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = []

            # Append the new data to the existing data
            existing_data.append(data)
            print(existing_data)

            # Save the data to the JSON file
            with open(file_path_wolframalph, "w") as file:
                json.dump(existing_data, file)
            
            
            return answer1
        except Exception as e:
            print('error found which is shown below ')
            print(e)
            # print("Sorry sir I couldn't fetch your question's answer. Please try again ")
            return None

    def find_app(app_name):
        with open(all_app_json, 'r') as f:
            app_data = json.load(f)
            # print(app_data)
        obj.Speak('Sir, Finding the application path. Please wait...')
        path_launch_app = obj.find_apps(app_name,app_data)
        
        print(path_launch_app)
        if path_launch_app:
            obj.Speak('Sir, application is launching. Please wait..')

            obj.launch_app(path_launch_app)
        else:
            obj.Speak('sir, application is not found.')




    def wish():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            obj.Speak("Good morning, Sir")
        elif hour >= 12 and hour < 18:
            obj.Speak("Good Afternoon, Sir")
        else:
            obj.Speak("Good evening, sir")
        c_time = obj.tell_time()
        obj.Speak(f"Currently it is {c_time}")
        obj.Speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")


    def startup():
        # obj.Speak("Initializing Jarvis")
        # obj.Speak("Starting all systems applications")
        # obj.Speak("Installing and checking all drivers")
        # obj.Speak("Caliberating and examining all the core processors")
        # obj.Speak("Checking the internet connection")
        # obj.Speak("Wait a moment sir")
        # obj.Speak("All drivers are up and running")
        # obj.Speak("All systems have been activated")
        obj.Speak("Now I am online")
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            obj.Speak("Good Morning")
        elif hour > 12 and hour < 18:
            obj.Speak("Good afternoon")
        else:
            obj.Speak("Good evening")
        c_time = obj.tell_time()
        obj.Speak(f"Currently it is {c_time}")
        obj.Speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")


class Mainthread(QThread):
    def __init__(self):
        super(Mainthread, self).__init__()

    def run(self):
        self.Taskexecution()

    def Taskexecution(self):
        otherfun.startup()
        while True:
            query = obj.mic_input()
            print(query)
            if "let's start" in query or 'start work' in query:
                # wish()
                obj.Speak('Sir, execution is started')
                
                loop = True
                while loop:
                    command = obj.mic_input()
                    if 'go to sleep' in command:
                        obj.Speak("Ok, Sir, Going to sleep mode. Call me anytime for service.")
                        loop = False
                        break

                    elif re.search('what is day today', command):
                        date = obj.tell_me_date()
                        print(date)
                        obj.Speak(date)

                    elif "what is time now" in command:
                        time_c = obj.tell_time()
                        print(time_c)
                        obj.Speak(f"Sir the time is {time_c}")
                    elif command in GREETINGS:
                        obj.Speak(random.choice(GREETINGS_RES))
                    elif 'google about' in command or 'google' in command:

                        obj.searchgoogle(command)
                    elif 'youtube' in command or 'search on youtube' in command:

                        obj.searchyoutube(command)

                        # elif 'show me weather' in command or "today's weather" in command:

                    #     get_weather(command)
                    elif 'want to launch app' in command or 'launch application' in command or 'launch app' in command:

                        obj.Speak('Sir, Which application do you want to launch ?')
                        app_name = obj.mic_input()
                        # print(app_name)
                        if app_name != 'none':
                                
                            otherfun.find_app(app_name)

                        else:
                            obj.Speak('Sir, can not recognised the application name, do you want search again, Sir? ')
                            des = obj.mic_input()
                            if 'yes' in des or 'definitely' in des:
                                otherfun.find_app(app_name, obj.find_apps)
                            else:
                                obj.Speak('Ok sir, moving forward.')
                    elif 'close app' in command or 'close the application' in command or 'Close application' in command:

                        obj.Speak('Sir, which application do you want to kill?')
                        application_name = obj.mic_input() + '.exe'
                        print(application_name)
                        obj.close_app(application_name)


                    elif 'want to send email' in command or 'send email' in command:                    
                        otherfun.sendername()

                    elif 'read mails' in command or 'read emails' in command or 'show emails' in command:
                        obj.read_emails()

                    elif 'turn off' in command:
                        obj.Speak("Sir, do you want to turn off program ? ")
                        last_command = obj.mic_input()
                        
                        if any(command in last_command for command in pos_res):
                            obj.Speak('Ok sir. Turning off the program')
                            exit(app.exec_())
                        else:
                            obj.Speak('Ok, sir. Program is running')
                    elif "calculate" in command:
                        question = command
                        answer = otherfun.computational_intelligence(question)
                        obj.Speak(answer)
                    
                    elif "what is" in command or "who is" in command:
                        question = command
                        answer = otherfun.computational_intelligence(question)
                        obj.Speak(answer)
                    elif 'show me weather' in command or 'display weather' in command:
                        obj.weather_show(command)
                    elif "where i am" in command or "current location" in command or "where am i" in command:
                        try:
                            city, state, country = obj.my_location()
                            print(city, state, country)
                            
                        except Exception as e:
                            obj.Speak("Sorry sir, I coundn't fetch your current location. Please try again")
                    elif command in calltobard:
                         obj.Speak('sir what do you want to ask google bard?')
                         response = obj.bard() 
                         print(response)  
                         if response['content'] !='' or response['content'] !='None': 
                            obj.Speak(response['content']) 
                         else:
                             obj.Speak('Sir, plese check the terminal to see the answer because there is not speakable content')   
                    elif "switch the window" in command or "switch window" in command:
                        obj.Speak("Okay sir, Switching the window")
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.keyUp("alt")   
                    elif "show me headlines" in command or "news" in command or "headlines" in command:
                        
                        news_res = obj.news()
                        # print(news_res)
                        obj.Speak('Todays Headlines are..')
                        for index, articles in enumerate(news_res):
                            pprint.pprint(articles['title'])
                            obj.Speak(articles['title'])
                            if index == len(news_res)-2:
                                break
                        obj.Speak('These were the top 10 headlines, Have a nice day Sir!!..')     
                    elif "find distance between" in command or 'how i far from' in command:
                        obj.Speak('Sir please tell me the target place')
                        target = obj.mic_input()
                        def distance(target):
                            target = target.replace('location is', '').replace('target is','')
                            try:
                                current_loc, target_loc, distance =obj.find_dis(target)
                                pass
                            except Exception as e:
                                print(e)
                                obj.Speak("Sorry sir, I coundn't fetch your current location. Please try again")
                                
                            else:
                                obj.Speak(f'Sir, the distance between your location {current_loc} to the target location {target_loc} is {distance} km.')
                        if target !='':
                            distance(target)
                        else:
                            obj.Speak('Sir, can not recognise the city, Please say again city name.')
                            target = obj.mic_input()
                            if target !='' or target != None:
                                distance(target)
                            elif target in Negative:
                                return 
                            else:
                                return
                    elif "show me system" in command or "system details" in command:
                        sys_info = obj.system_info()
                        print(sys_info)
                        obj.Speak(sys_info)
                    elif 'search on chat gpt' in command or 'get answer from chat gpt' in command or 'open chat gpt' in command:
                        obj.Speak('Ok Sir, please tell me query you want to search on chatgpt ')
                        res = obj.searchgpt()
                        obj.Speak('Sir get the response from chatgpt ')
                        obj.Speak(f'sir found response is {res["response"]}')
                    elif "where is" in command:
                        place = command.split('where is ', 1)[1]
                        current_loc, target_loc, distance = obj.location(place)
                        city = target_loc.get('city', '')
                        state = target_loc.get('state', '')
                        country = target_loc.get('country', '')
                        time.sleep(1)
                        try:

                            if city:
                                res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                                print(res)
                                obj.Speak(res)

                            else:
                                res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                                print(res)
                                obj.Speak(res)

                        except:
                            res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                            obj.Speak(res)
                        
                            
startjarvis = Mainthread()
# startjarvis.Taskexecution()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startjarvis.start()
        # startjarvis.Taskexecution()
       
        

    def showTime(self): 
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
