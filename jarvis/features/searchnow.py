import pywhatkit
import wikipedia as googleScrap
import webbrowser
import subprocess
from jarvis.features.listen import takecommand
from jarvis.features.speech import speak


def searchGoogle(query):
    if 'google' in query or 'search on google' in query or 'google about' in query:
        query = query.replace('jarvis', '').replace('search on google', '').replace('google about', '').replace(
            'google', '')
        speak('Sir, this is what i found on google')
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except Exception as e:

            speak('Sir, found an error. would do like to know it ?')
            com = takecommand().lower()
            if 'yes' in com:
                print(e)
                speak(
                    'Sir, do you want to google it ?')  # currently google it later replace google with chatgpt to solve issue.
                com = takecommand().lower()
                if 'yes' in com:
                    webbrowser.open('https://chat.openai.com/')
                else:
                    return

            else:
                return


def searchYoutube(query):
    if 'open youtube' in query or 'search on youtube' in query or 'on youtube' in query:
        query = query.replace('jarvis', '').replace('open youtube', '').replace('search on youtube', '').replace(
            'youtube', '').replace('seach', '')
        speak('Launchin youtube... Please wait')
        web = 'https://www.youtube.com/results?search_query=' + query
        try:
            # subprocess.run(['chrome', '--new-tab', 'https://www.youtube.com/results?search_query=' + query])

            webbrowser.open(web)
            # pywhatkit.playonyt(web)
            speak('done sir')

        except Exception as e:
            print(e)


def searchWikipidea(query):
    if 'wikipedia' in query or 'search on wikipedia' in query:
        query = query.replace('jarvis', '').replace('search on wikepidia', '').replace('wikipedia', '')
        speak('Sir, searching on wikipedia')
        web = 'https://www.google.com/results?search_query=' + query
        try:
            result = googleScrap.summary(query, sentences=2)
            speak('Accoording to wikipedia')
            print(result)
            speak(result)
        except Exception as e:
            print(e)
# searchGoogle(query)
# searchYoutube(query)


