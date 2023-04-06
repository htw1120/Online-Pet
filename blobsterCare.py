

from modules.blobster import Blobster


def main():
    name = input("Enter your Blobster's name: ")
    color = input("Enter your Blobster's color: ")
    radius = eval(input("Enter your Blobster's radius: "))
    height = eval(input("Enter your Blobster's height: "))

    myBlobster = Blobster(name, color, radius, height)

    done = False

    while not done:
        print()
        print("Main Menu")
        print("\t(1) Display Name")
        print("\t(2) Change Name")
        print("\t(3) Display Color")
        print("\t(4) Change Color")
        print("\t(5) Feed Blobster")
        print("\t(6) Blobster Speak")
        print("\t(7) Exit")

        # Display current vitals and check to see if it has turned to dust
        # This will catch cases where the Blobster was fed too much as well
        vitals, blobster_ok = myBlobster.vitalsOK()
        print("Your Blobster is at " + format(vitals, ".2%") + " happiness")
        if not blobster_ok:
            print("Your Blobster turned to dust")
            break

        choice = eval(input("Make a selection: "))
        print()

        # Check to see if the Blobster turned to dust while waiting for the user to make a selection
        vitals, blobster_ok = myBlobster.vitalsOK()
        if not blobster_ok:
            print("Your Blobster is at " + format(vitals, ".2%") + " happiness")
            print("Your Blobster turned to dust")
            break

        if choice == 1:
            displayName(myBlobster)
        elif choice == 2:
            changeName(myBlobster)
        elif choice == 3:
            displayColor(myBlobster)
        elif choice == 4:
            changeColor(myBlobster)
        elif choice == 5:
            feedBlobster(myBlobster)
        elif choice == 6:
            blobsterSpeak(myBlobster)
        elif choice == 7:
            done = True

    print("Thanks for taking care of a Blobster")


def displayName(blobster):
    print("Your Blobster's name is " + blobster.getName().capitalize())


def changeName(blobster):
    name = input("Enter Blobster's new name: ")
    blobster.setName(name)
    displayName(blobster)


def displayColor(blobster):
    print("Your Blobster's color is " + blobster.getColor().lower())


def changeColor(blobster):
    color = input("Enter Blobster's new color: ")
    blobster.setColor(color)
    displayColor(blobster)


def feedBlobster(blobster):
    food = eval(input("Enter amount to you feed your Blobster: "))
    blobster.feedBlobster(food)


def blobsterSpeak(blobster):
    print(blobster.blobsterSpeak())
    

main()
