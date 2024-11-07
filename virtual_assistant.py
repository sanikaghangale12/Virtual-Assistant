import speech_recognition as sr
import pyttsx3  # text-to-speech conversion library
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from tkinter import messagebox

# Initialize speech recognition, text-to-speech, and other necessary libraries
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Female voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

def alexa_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                talk(command)
    except:
        pass
    return command

def run_alexa():
    command = alexa_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time is: " + time)
    elif "person" in command:
        command = command.replace("person", "")
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
# run_alexa()  till this it is code without 

# GUI Setup
def start_assistant():
    status_label.config(text="Assistant is listening...")
    run_alexa()
    status_label.config(text="Assistant is idle")

# Initialize the main window
root = tk.Tk()
root.title("Virtual Assistant")

# Create a simple UI with a button to activate the assistant
status_label = tk.Label(root, text="Click 'Start' to begin", font=("Arial", 14))
status_label.pack(pady=20)

start_button = tk.Button(root, text="Start Assistant", command=start_assistant, font=("Arial", 12))
start_button.pack(pady=10)

# Add an exit button to close the application
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
exit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
