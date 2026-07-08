import random
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.speak(text)


target = random.randint(1,100)
prompt="Note: Number must be between 1 to 100 !!!"
print(prompt)
speaker.speak(prompt)

while True:
    prompt1="Guess the target number or enter 'Quit' to exit and end the game: "
    print(prompt1)
    speaker.speak(prompt1)
    userGuess = input()
    
    if(userGuess == "Quit"):
        break
    elif userGuess.isdigit():
        userGuess = int(userGuess)
        if (userGuess > 100 or userGuess < 1):
            prompt2="Invalid Number, Entered number is out of range. "
            print(prompt2)
            speaker.speak(prompt2)
            break
        elif(userGuess == target):
            prompt3="Congratulations!!! You have guessed the target number."
            print(prompt3)
            speaker.speak(prompt3)
            break
        elif(userGuess < target):
            prompt4="Your number is smaller than the targer number. Try Again"
            print(prompt4)
            speaker.speak(prompt4)
        else:
            prompt5="Your number is bigger than the target number. Try Again."
            print(prompt5)
            speaker.speak(prompt5)
    else:
        prompt6="Invalid Input !!!"
        print(prompt6)
        speaker.speak(prompt6)
        break
prompt7="-----GAME OVER-----"
print(prompt7)
speaker.speak(prompt7)
