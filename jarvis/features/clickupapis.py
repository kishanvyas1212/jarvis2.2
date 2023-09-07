import requests
# from jarvis.config.configuration import clickupapitoken
API_KEY =''
list_id = ""
# url = "https://api.clickup.com/api/v2/list/" + list_id + "/task"

# query = {
#   "archived": "false",
#   "page": "0",
#   "order_by": "string",
#   "reverse": "true",
#   "subtasks": "true",
#   "statuses": "string",
#   "include_closed": "true",
#   "assignees": "string",
#   "tags": "string",
#   "due_date_gt": "0",
#   "due_date_lt": "0",
#   "date_created_gt": "0",
#   "date_created_lt": "0",
#   "date_updated_gt": "0",
#   "date_updated_lt": "0",
#   "date_done_gt": "0",
#   "date_done_lt": "0",
#   "custom_fields": "string"
# }

# headers = {"Authorization": API_KEY}

# response = requests.get(url, headers=headers, params=query)

# data = response.json()
# print(data)
# import requests

# folder_id = "YOUR_folder_id_PARAMETER"
# url = "https://api.clickup.com/api/v2/folder/" + folder_id + "/list"

# query = {
#   "archived": "false"
# }

# headers = {"Authorization": "YOUR_API_KEY_HERE"}

# response = requests.get(url, headers=headers, params=query)

# data = response.json()
# print(data)
import requests

team_id = ""
url = "https://api.clickup.com/api/v2/team/" + team_id + "/space"

query = {
  "archived": "false"
}

headers = {"Authorization": API_KEY}

response = requests.get(url, headers=headers, params=query)

data = response.json()
print(data)