from jarvis.features import emails
from jarvis.features import launch_app, searchnow,listen,takenotes, tell_time
from jarvis.features import speech, weather,loc,system_states, news, chatGPT,timespleep, googlebard
import speech_recognition as sr
import json

positive_res = 'jarvis\\database\\postiveres.json'
negative_res ='jarvis\\database\\intents.json'
class otherfun:
    def prompt():
        prompt = otherfun.takecommand().lower() 
        with open(negative_res,'r') as file:
                    neg_res = json.load(file)
        if prompt != "none":
                response = googlebard.bard_res(prompt)
                
        elif prompt in neg_res:
            speech.speak('Ok sir, skipping it')
        else:
            speech.speak('Sir please say again')
            prompt = otherfun.takecommand().lower()
            
        return prompt




    def takecommand():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listning...")

                    r.pause_threshold = 1

                    audio = r.listen(source,0,10)

                try:
                    print("recognising... ")
                    Query = r.recognize_google(audio, language='en-in')
                    print(f"User said: {Query} \n")
                    # create_db_conversation("Speaker: " +Query + '\n\n\n')
                    # create_db_conversation("-------\n\n\n")

                except Exception as e:
                    # print(e)
                    print("say that again please")

                    return 'none'

                return Query
class VoiceAssistant:
    def __init__(self):
        pass

    def mic_input(self):
        '''
        this is for taking voice input from the user
        :return:
        '''
        return listen.takecommand().lower()
    takecommand = otherfun.takecommand
    def Speak(self,text):
        import pyttsx3
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)

        engine.say(text)
        engine.runAndWait()
        return
    def searchgoogle(self,query):
        return searchnow.searchGoogle(query)
    def searchyoutube(self,query):
        return searchnow.searchYoutube(query)
    def searchwikipidia(self,query):
        return searchnow.searchWikipidea(query)
    def takenotes(self):
        return takenotes.write_content_with_voice()
    def read_emails(self):
        return emails.search_in_mail()
    def send_email(self,sender):
        
        
        sender = sender.replace(' ', '')
      
        
        print(sender)
        speech.speak("sir, finding sender in data base")
        email_sender = emails.search_key(sender)
        print(email_sender)
        
        speech.speak('Sir, please tell me the subject')
        subject = otherfun.takecommand().lower()
        while subject == 'none':
            speech.speak('Sir, Please say that again')
            subject = otherfun.takecommand().lower()
        speech.speak('Sir, Please tell me what to write in body') # will update and link with chatgpt for write down the email body
        body = otherfun.takecommand().lower()
        while body == 'none':
            speech.speak('Sir, Please say that again!')
            body = otherfun.takecommand().lower()
        speech.speak(f'Sir, The subject of mail is {subject} and want to send mail to {sender} whose email address is {email_sender}')
        speech.speak('Sir do you want to change subject or body or sender name or anything ? ')
        res = listen.takecommand().lower()
        with open(positive_res,'r') as file:
                    pos_res = json.load(file)
        with open(negative_res,'r') as file:
                    neg_res = json.load(file)
                    
        if any(command in res for command in pos_res):
            pass
            # Please change code later so user can change any inpute field 
        elif any(command in res for command in neg_res):
            speech.speak('Ok Sir, Then this is final email. Sending email')
            emails.send_email(subject, body, email_sender)
        elif "please send now" in res or 'send it now' in res:
            emails.send_email(subject, body, email_sender)
        
    def tell_time(self):
        return tell_time.time()
    def find_apps(self,path,data):
        return launch_app.find_application_path(path,data)
    def close_app(self,name):
        return launch_app.close_application(name)
    def launch_app(self,path):
        return launch_app.launch_application(path)
    def tell_me_date(self):

        return tell_time.date()

    def weather_show(self, command='rajkot'):
        return weather.get_weather(command)
    def my_location(self):
        city, state, country = loc.my_location()
        return city, state, country
    def find_dis(self,place):
        
        current_loc, target_loc, distance = loc.loc(place)
        return current_loc, target_loc, distance
    def system_info(self):
        return system_states.system_stats()
    def news(self):
        """
        Fetch top news of the day from google news
        :return: news list of string if True, False if fail
        """
        return news.get_news()
    def searchgpt(self):
        q = otherfun.takecommand().lower()
        while q  == 'none':
            q = otherfun.takecommand().lower()
        print(q)
        speech.speak(f'sir the given query is {q}')
        res = chatGPT.search_gpt(q)
    
        return res
    def sleeptime(self):
        
        existinhdata = timespleep.sleeptime.readdatabase()
        print(existinhdata['personaldetails'])
        if existinhdata['personaldetails'] == []:
           settime= timespleep.sleeptime.setsleeptime()
           timespleep.sleeptime.writeindatabase(settime)
        else:
            print(f'the time is already set down, {existinhdata["personaldetails"]}')
    def bard(self):
        response = otherfun.prompt()
            
        
        return response
            