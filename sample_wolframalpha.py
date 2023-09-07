import wolframalpha
from jarvis.config.configuration import wolframalphaid
import json
file_path = 'wolframalpha_responses.json'

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(wolframalphaid)
        answer = client.query(question)
        print(type(answer))
        print(answer)
        # answer1 = next(answer.results).text
        # print(answer1)
        data = {
        "query": question,
        "response": answer
            }
        print(answer)
        # Check if the JSON file already exists
        try:
            with open(file_path, "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        # Append the new data to the existing data
        existing_data.append(data)
        print(existing_data)

        # Save the data to the JSON file
        with open(file_path, "w") as file:
            json.dump(existing_data, file)
        
        
        return answer
    except Exception as e:
        print('error found which is shown below ')
        print(e)
        # print("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
    
question = 'Three Mile Island'
answer = computational_intelligence(question)
# save_response_to_json(question, answer)