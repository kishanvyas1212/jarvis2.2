import spacy
import re
import random

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

GREETINGS = ["hello", "hi", "hey"]
GREETINGS_RES = ["Hello!", "Hi there!", "Hey!"]

# Define patterns for different commands and their corresponding actions
COMMANDS = {
    r"go to sleep": "sleep",
    r"what is date today": "date",
    r"what is time now": "time",
    r"google( about)?": "google",
    r"(search on )?youtube": "youtube"
}

def process_sentence(sentence):
    doc = nlp(sentence)
    print(doc)
    for w in doc.ents:
        print(w.text,w.label_)
    return doc

def perform_tasks(command):
    if command == "sleep":
        
        print("Ok, Sir, Going to sleep mode. Call me anytime for service.")
    elif command == "date":
        # date = tell_me_date()
        print('date is matched')
        # obj.Speak(date)
    elif command == "time":
        # time_c = tell_time()
        # print(time_c)
        print('time')
        # obj.Speak(f"Sir the time is {time_c}")
    elif command in GREETINGS:
        # obj.Speak(random.choice(GREETINGS_RES))
        print(random.choice(GREETINGS_RES))
    elif command == "google":
        search_google()
    elif command == "youtube":
        search_youtube()

def tell_me_date():
    # Implement the function to return the current date
    # ...
    print('tell me date function called')

def tell_time():
    # Implement the function to return the current time
    # ...
    print('tell time function called')
def search_google():
    # Implement the function to search on Google
    # ...
    print('Search google function is called')
def search_youtube():
    # Implement the function to search on YouTube
    # ...
    print("Search youtube func is called ")

def main():
    # obj = SomeClass()  # Replace 'SomeClass' with the appropriate class that has the 'Speak' method.

    while True:
        user_input = input("Enter a command: ").lower()
        doc = process_sentence(user_input)

        for pattern, command in COMMANDS.items():
            if re.search(pattern, user_input):
                perform_tasks(command)
                break
        else:
            print("Command not recognized. Please try again.")

if __name__ == "__main__":
    main()
