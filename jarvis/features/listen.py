import speech_recognition as sr


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")

        r.pause_threshold = 0.8

        audio = r.listen(source, 0, 4)

    try:
        print("recognising... ")
        Query = r.recognize_google(audio, language='en-in')
        print(f"User said: {Query} \n")
        # create_db_conversation("Speaker: " +Query + '\n\n\n')
        # create_db_conversation("-------\n\n\n")

    except Exception as e:
        # print(e)
        print("say that again please")

        return 'none'

    return Query
# takecommand()