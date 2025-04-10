def introScene():
    directions = ["left", "right", "forward", "backward"]
    print("There are four hallways. Where would you like to go?")

    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input().lower()

        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            YouGetSpitOutInTheBerklee130PracticeRooms()
        elif userInput == "forward":
            YouWalkIntoAnET4Exam()
        elif userInput == "backward":
            print("You find that this door opens into a wall.")
            input("")
            print("a bricks falls out and onto your head")
            input("")
            print("you die :(")
            input("")
            Youdie()
        else:
            print("Please enter a valid option for the adventure game.")

def Youdie():
    directions = ["yes", "no"]
    print("Would you like to try again?")

    userInput = ""
    while userInput not in directions:
        print("Options: yes/no")
        userInput = input().lower()
        if userInput == "no":
            print("Thank you for playing.")
            exit()
        elif userInput == "yes":
            introScene()

def showShadowFigure():
    directions = ["forward", "backward"]
    print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
    
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input().lower()
        
        if userInput == "forward":
            oujiboard()
        elif userInput == "backward":
            print("You run away in fear, back to the previous location.")
            input("")
            introScene()
        else:
            print("Invalid choice. Try again.")

def oujiboard():
    directions = ["yes", "no"]
    print("You come across a Ouija board, do you use it?")

    userInput = ""
    while userInput not in directions:
        print("Options: yes/no")
        userInput = input().lower()

        if userInput == "yes":
            usingtheboard()
        elif userInput == "no":
            print("You keep walking.")
            input("")
            print("you wonder about boston")
            input("")
            print("it's so old")
            input("")
            print("and mysterious")
            input("")
            print("a ghost would be pretty cool to meet")
            

def usingtheboard()
    print("You approach and put your hands on the triangle.")
    input("")
    print("okay but ghosts aren't real...")
    input("")
    print("...right?")
    input("")
    print("-RIGHT?")
    input("")
    print("before you can think twice...")
    input("")
    print("the triangle starts moving")
    input("")
    print("....C")
    input("")
    print("..H..")
    input("")
    print("....A...")
    input("")
    print(".....R....")
    input("")
    print("...")
    input("")
    print("..L")
    input("")
    print("it pauses")
    input("")

    Youdie()

def YouGetSpitOutInTheBerklee130PracticeRooms():
    print("You end up in the Berklee 130 practice rooms, where someone is playing guitar at full volume.")
    Youdie()

def YouWalkIntoAnET4Exam():
    print("You walk into an ET4 (Ear Training 4) exam. The proctor stares at you, expecting an answer.")
    input("")
    print("the teacher stares at you")
    input("")
    print("and stares")
    input("")
    print("still staring")
    input("")
    print("and MORE")
    input("")
    print("AND MORE")
    input("")
    print("sudenly you feel your skin start to heat")
    input("")
    print("and burn")
    input("")
    print("your teacher's eyes turn red")
    input("")
    print("as you melt into tHE GROUND AND YOU....")
    input("")
    print("DIEEEEEEEEEEEE!!!")
    input("")
    Youdie()

def restartGame():
    print("No more options left. Restarting game...")
    introScene()

if __name__ == "__main__":
    
    print("Welcome to the Spades Game!")
    input("Press Enter to continue...")  # Wait for player input before printing next line
    print("As an avid traveler, you have decided to visit the Catacombs of Boston.")
    input("")
    print("However, during your exploration, you find yourself lost.")
    input("")
    name = input("Let's start with your name: ")
    print("Good luck, " + name + ".")
    input("")
    print("Anyway, back to it")
    input("")
    print("You are at a crossroads and can choose to walk in multiple directions to find a way out.")
    input("")
    introScene()

