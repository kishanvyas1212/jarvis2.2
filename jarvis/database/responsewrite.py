import json
path = 'jarvis\\database\\googlebard.json'
import os

dict_data = {'prompt': '7',
             'result': {'content':'', 
                         'conversation_id': '', 
                         'response_id': '3', 
                         'factualityQueries': None, 
                         'textQuery': ['python modules to write, read and updatte the csv, json, text and exel files',
                                        1
                                        ], 'choices': [
                                            {'id': '', 'content': [
                                                    ""  ]
                                            },
                                            {'id': '', 'content': [
                                            ""        
                                            ]
                                            },
                                            {'id': '2', 'content': [
                                            ""       
                                            ]
                                            }
                                        ], 'links': [], 'images': set(), 'code': None
                     }
             }


print(dict_data['result']['images'])

# Update the `images` key with a string
dict_data['result']['images'] = f"the images are stored in other file, which id is {dict_data['result']['response_id']} "

code = dict_data['result']['code']
print(code)
dict_data['result']['code'] = 'no value'
    
# Convert the dictionary to JSON
json_data = json.dumps(dict_data)

# print(json_data)
# print(type(json_data))

# Check if the JSON file exists

try:
    if os.path.exists('jarvis/database/googlebard.json'):
        # Load existing data from the JSON file (if any)
        with open('jarvis/database/googlebard.json', 'r') as json_file:
            existing_data = json.load(json_file)
            print(existing_data)
except FileNotFoundError:
    existing_data = {}

# Update the existing data with the new data
# print('=============================================================================================')
data = {
    dict_data['result']['response_id'] : dict_data
}
existing_data.update(data)
print(existing_data)
with open(path, 'w') as json_file:
    json.dump(existing_data, json_file)




