from jarvis.features.speech import speak
import speech_recognition as sr
import subprocess
import pyautogui


def write_content_with_voice():
    speak('Sir, say quit to stop writing')
    speak('Notepad is launching')
    subprocess.Popen('notepad.exe')  # Open Notepad using subprocess

    # Initialize the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # print("Listening...")

        while True:
            print("Listening...")

            r.pause_threshold = 0.8

            audio = r.listen(source, 0, 4)
            try:
                text = r.recognize_google(audio)

                print("Recognized:", text)

                if text.lower() == "quit":
                    break
                if 'print in new line' == text.lower():
                    pyautogui.typewrite(text + "\n ")

                # Write the recognized text into Notepad using keyboard input
                pyautogui.typewrite(text + " ")

            except sr.UnknownValueError:
                print("Unable to recognize speech.")
                speak("Unable to recognize speech.")
            except sr.RequestError as e:
                print("Speech recognition request error:", str(e))

            else:
                print('new loop started')

    # Save and close the Notepad file
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f4')

