
import json
from bardapi import Bard
# import requests
from bardapi import BardCookies
import re
path = 'jarvis\\database\\googlebard.json'
# from jarvis.config.configuration import bardtoken
# from jarvis.config.configuration import cookies_dis
import pyperclip
import pyautogui
from time import sleep
import keyboard
import webbrowser
def cookies():
    webbrowser.open('https://bard.google.com/')
    sleep(2)
    pyautogui.click(x=1743, y=71)
    sleep(1)
    pyautogui.click(x=1460, y=258)
    sleep(1)
    pyautogui.click(x=1458, y=103)
    sleep(1)
    keyboard.press_and_release('ctrl + w')
    data = pyperclip.paste()
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError as e:
        print(f'Error parsing JSON data: {e}')
    
    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"
    SIDv = next((item for item in json_data if item["name"]== SID),None)
    TSv = next((item for item in json_data if item["name"]== TS),None)
    CCv = next((item for item in json_data if item["name"]== CC),None)
    if SIDv is not None and TSv is not None and CCv is not None:
        SIDv = SIDv['value']
        TSv = TSv['value']
        CCv = CCv['value']
    else:
        print(f'values are none check it manually SIDv={SIDv}, TSv={TSv} and CCv={CCv}')
        
    cookies_dict = {
        "__Secure-1PSID" : SIDv,
    "__Secure-1PSIDTS" : TSv,
    "__Secure-1PSIDCC":CCv    }
    
    return cookies_dict

def writedata(dict_data,prompt):
    # data = {
    #     "prompt": prompt,
    #     "result" : dict_data
    # }
    # images_set = data['result']['images']
    # print(data)
    # print(type(data))
    # data['result']['images'] = f"the images are stored in other file, which id is {data['result']['response_id']} "
    # print(images_set)
    # print(type(images_set))
    # code = data['result']['code']
    
    # print(code)
    # print(f'the type of code is {type(code)}')
    # dict_data['result']['code'] = 'no value'
        

    # try:
    #     if os.path.exists('jarvis/database/googlebard.json'):
    #         # Load existing data from the JSON file (if any)
    #         with open('jarvis/database/googlebard.json', 'r') as json_file:
    #             existing_data = json.load(json_file)
    #             print(existing_data)
    # except FileNotFoundError:
    #     existing_data = {}

    # data1 = {
    #     data['result']['response_id'] : data,
    #     f"code of {data['result']['response_id'] }" : code
    # }
    # existing_data.update(data1)
    # print(existing_data)
    # # with open(path, 'w') as json_file:
    # #     json.dump(existing_data, json_file)
    words = re.split(r"\b\w{4}\b", prompt)
    file_name = words[0].replace(' ','').replace('?','')
    print(words[0])
    dict_data = str(dict_data)
    with open(f"jarvis//database//bard_response//{file_name}.txt", "w") as file:
        file.write(dict_data)
    
    
    

def bard_res(prompt):
    cookies_value=cookies()
    bard = BardCookies(cookie_dict=cookies_value)
    # results = Bard(token=bardtoken).get_answer(prompt)
    """Gets a response from Bard."""
    api_url = "https://bard.google.com/v1/query"
    headers = {
        # "Authorization": "Bearer {}".format(bardtoken),
    }
    # data = {"query": prompt}

    # results = requests.post(api_url, headers=headers, data=json.dumps(data))
    results = bard.get_answer(prompt)
    # data = json.dumps(results)
    
    
    writedata(results,prompt)    
    # print(data)

    return results

# bard_res(prompt='how can i become seurity tester? give me suggestion to achieve my dream i want high paying job i am currently working as qa')
