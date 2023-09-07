import subprocess
import json
from jarvis.features.listen import takecommand
from jarvis.features.speech import speak

pos_file ='jarvis\\database\\postiveres.json'
neg_file = 'jarvis\\database\\intents.json'



def find_application_path(app_name, app_data):
    # Load application data from the JSON file
    with open(pos_file,'r') as file:
        pos_res= json.load(file)
    with open(neg_file,'r') as file:
        neg_res = json.load(file)
    with open(file_path, 'r') as f:
        app_data = json.load(f)
    for app in app_data:
        if app[0].lower() == app_name.lower():
            print(app_name)
            return app[1]
        elif app_name.lower() in app[0].lower():
            speak(f'Sir, similar app is found which is {app[0]}. Do you want to launch it ?')
            res = takecommand().lower()
            if res in pos_res:
                return app[1]
            elif res in neg_res:
                speak('Ok sir, skipping this task.')
                return False
            
    return None


def launch_application(application_path):
    try:
        subprocess.Popen(application_path)
        print(f"Application launched: {application_path}")
    except Exception as e:
        print(f"Error launching application: {e}")


def close_application(application_name):
    try:
        subprocess.call(["taskkill", "/F", "/IM", application_name])
        print(f"Application closed: {application_name}")
    except Exception as e:
        print(f"Error closing application: {e}")

    else:
        return print('work done')


# Specify the path to the JSON file containing application data
file_path = 'jarvis/database/all_applications.json'