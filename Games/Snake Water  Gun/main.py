# We all have played Snake, Water, Gun game in out childhood. If you haven't, google the rules of this game and write a python program capable of playing this game with the user.
'''
-1 for Snake
0 for Water
1 for Gun
'''

import random
Computer=random.choice([-1,0,1])

info=[f"s for Snake", "w for water", "g for Gun"]
print(info)
yourChoice=input("Enter your choice: ")
if (yourChoice!="s" and yourChoice!="w" and yourChoice!="g"):
    print("Invalid Choice!!!")
else:
    Dict={
        "s":-1,
        "w":0,
        "g":1
    }
    reverseDict={
        -1:"Snake",
        0:"Water",
        1:"Gun"
    }

    you=Dict[yourChoice]

    print(f"Computer chose {reverseDict[Computer]} and You chose {reverseDict[you]}.")

    if (Computer==you):
        print("Its a Draw!!!")
    else:
        if (Computer == -1 and you == 1):       #(Computer-you) = -2
            print("You Won!!!")
        elif (Computer == -1 and you == 0):     #(Computer-you) = -1
            print("You Loose!!!")
        elif (Computer == 1 and you == -1):     #(Computer-you) = 2
            print("You Loose!!!")
        elif (Computer == 1 and you == 0):      #(Computer-you) = 1
            print("You Won!!!")
        elif (Computer == 0 and you == -1):     #(Computer-you) = 1
            print("You Won!!!")
        elif (Computer == 0 and you == 1):      #(Computer-you) = -1
            print("You Loose!!!")
        else:
            print("Something went Wrong!!!")

'''
Advance logic to solve above problem in few lines:
if ((Computer-you) ==-1 or (Computer-you) == 2):
    print("You Loose!!!")
else:
    print("You Won!!!)
'''