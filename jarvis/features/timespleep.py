from jarvis.features.speech import speak
from jarvis.features.listen import takecommand
import json
replacew = ['jarvis','service','sleep time is','set','time is',  "o'clock",'sleep','time','at','as','a','hour','hours']

personal = 'jarvis\database\personaldetails.json'
class sleeptime:

    def setsleeptime():
        
        speak('Sir, please tell me time to set up for wind up everything.')
        while True:
            sleeptime = takecommand().lower()
            for item in replacew:
                sleeptime = sleeptime.replace(item,"")
            try:
                sleeptime = int(sleeptime)
                break
            except Exception as e:
                print(e)
                speak('Sir, can not convert time into intger it means there it is something problem ')
        
        data = {
            "The sleeping time is " : sleeptime
        }
        print(sleeptime)
        return data
        
    def readdatabase():
        with open(personal,'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}
        return existing_data   
    def writeindatabase(data):
        existing_data = sleeptime.readdatabase()                 
        if 'personaldetails' not in existing_data:
            existing_data['personaldetails'] = []      
        
        existing_data['personaldetails'].append(data)
        with open(personal,'w') as file :
            json.dump(existing_data, file, indent=4)

            
