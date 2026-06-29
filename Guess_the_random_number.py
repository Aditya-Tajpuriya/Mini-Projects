import random
import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

target = random.randint(1,100)
speak("Note: Number must be between 1 to 100 !!!")

while True:
    
    speak("Guess the target number or enter 'Quit' to exit and end the game: ")
    userGuess = input()

    if(userGuess == "Quit"):
        break
    elif userGuess.isdigit():
        userGuess = int(userGuess)
        if (userGuess > 100 or userGuess < 1):
            speak("Invalid Number, Entered number is out of range. ")
            break
        elif(userGuess == target):
            speak("Congratulations!!! You have guessed the target number.")
            break
        elif(userGuess < target):
            speak("Your number is smaller than the targer number. Try Again")
        else:
            speak("Your number is bigger than the target number. Try Again.")
    else:
        speak("Invalid Input !!!")
        break

speak("-----GAME OVER-----")
