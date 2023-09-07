import json
import re
import datetime

# Sample text containing the response
response_text = """
...  # Your response text here
"""

# Assume you have the query stored in a variable called user_query
user_query = "Give me code to create jarvis like voice assistant"

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
response_text_cleaned = response_text.replace(user_query, "").strip()

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

# Load existing data from the JSON file (if any)
with open('jarvis/database/chatGPT_res.json', 'r') as json_file:
    existing_data = json.load(json_file)

# Append the current response data to the main object
if 'responses' not in existing_data:
    existing_data['responses'] = []

existing_data['responses'].append(response_data)

# Save the updated data as JSON
with open('jarvis/database/chatGPT_res.json', 'w') as json_file:
    json.dump(existing_data, json_file, indent=4)
