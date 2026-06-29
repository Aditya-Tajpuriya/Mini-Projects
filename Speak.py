# This works for only Windows
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("First statement")
speaker.Speak("Second statement")
speaker.Speak("Third statement")
speaker.Speak("fourth statement")
a=input("Enter the statement you want to hear: ")
speaker.Speak(a)