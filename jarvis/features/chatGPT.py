import webbrowser
import pyautogui
import datetime
import json
import pyperclip
import os
import time

# def get_current_timestamp():
#     return time.strftime('%Y-%m-%d %H:%M:%S')

# def save_to_json(data):
#     file_path = 'jarvis\\database\\chatGPT_res.json'
#     all_data = []

#     try:
#         with open(file_path, 'r') as json_file:
#             all_data = json.load(json_file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         pass

#     all_data.append(data)

#     with open(file_path, 'w') as json_file:
#         json.dump(all_data, json_file, indent=4)
def search_gpt(query):
    webbrowser.open('https://chat.openai.com/')
    time.sleep(5)
    x = 963
    y = 915
    # Assume you have the query stored in a variable called user_query
    user_query = query
    # print(pyautogui.position())
    pyautogui.click(x=x, y=y)
    time.sleep(1)
    pyautogui.typewrite(user_query)
    time.sleep(2)
    print(pyautogui.position())
    x = 1568
    y = 929
    pyautogui.click(x=x, y=y)
    time.sleep(30)
    pyautogui.moveRel(0, -300)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')
    copy_text = pyperclip.paste()
    time.sleep(2)

    # timestamp = get_current_timestamp()
    # data = {
    #     'timestamp': timestamp,
    #     'text': copy_text
    # }

    # save_to_json(data)

    time.sleep(2)


    # Sample text containing the response
    # response_text = """
    # ...  # Your response text here
    # """



    # Define the markers to locate code and text
    code_markers = ["import", "def main():", "python\nCopy code"]

    # Function to find the marker closest to the beginning of the response
    def find_marker(response_text, markers):
        closest_index = len(response_text)
        closest_marker = None

        for marker in markers:
            index = response_text.find(marker)
            if index != -1 and index < closest_index:
                closest_index = index
                closest_marker = marker

        return closest_marker, closest_index

    # Find the user query in the response and remove any occurrences of it
    query_index = copy_text.find(user_query)

    if query_index != -1:
        response_text_cleaned = copy_text[query_index + len(user_query):].strip()
    else:
        response_text_cleaned = copy_text.strip()
        response_text_cleaned = copy_text.replace(user_query, "").strip()

    # Find the closest marker to separate the text and code parts
    closest_marker, closest_index = find_marker(response_text_cleaned, code_markers)

    if closest_marker:
        response = response_text_cleaned[:closest_index].strip()
        code = response_text_cleaned[closest_index + len(closest_marker):].strip()
    else:
        # If no marker is found, consider the whole response as text (no code)
        response = response_text_cleaned
        code = ""

    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a dictionary to store the data for this response
    response_data = {
        'query': user_query,
        'response': response,
        'code': code,
        'timestamp': current_time
    }

    # Check if the JSON file exists
    if os.path.exists('jarvis/database/chatGPT_res.json'):
        # Load existing data from the JSON file (if any)
        with open('jarvis/database/chatGPT_res.json', 'r') as json_file:
            try:
                existing_data = json.load(json_file)
            except json.JSONDecodeError:
                # If the JSON file is empty or invalid, start with an empty dictionary
                existing_data = {}
    else:
        existing_data = {}

    # Append the current response data to the main object
    if 'responses' not in existing_data:
        existing_data['responses'] = []

    existing_data['responses'].append(response_data)  

    # Save the updated data as JSON
    with open('jarvis/database/chatGPT_res.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)
    
    return response_data
 
