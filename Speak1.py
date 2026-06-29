# This works for Windows, macOS, Linux
import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("First statement")
speak("Second statement")
speak("Third statement")
