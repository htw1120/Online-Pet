import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    # Draw the head    
    def drawHead(self):
        turtle.reset()
        turtle.penup()
        turtle.goto(0, -100)
        turtle.pendown()
        if self.__happy:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()

    # Draws the eyes    
    def drawEyes(self):
        # left eye
        turtle.goto(-30, 30)
        turtle.pendown()
        turtle.begin_fill()
        if self.__darkEyes:
            turtle.fillcolor("black")
        if not self.__darkEyes:
            turtle.fillcolor("blue")
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()

        # right eye
        turtle.goto(30, 30)
        turtle.pendown()
        turtle.begin_fill()
        if self.__darkEyes:
            turtle.fillcolor("black")
        if not self.__darkEyes:
            turtle.fillcolor("blue")
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()

    # Draws the mouth   
    def drawMouth(self):
        turtle.goto(-40, -30)
        turtle.pendown()
        turtle.pensize(5)
        if self.__smile:
            turtle.setheading(315)
            turtle.circle(60, 90)
        else:
            turtle.setheading(210)
            turtle.circle(60, -70)
        turtle.pensize(1)

    # Draws the entire face 
    def draw_face(self):
        turtle.clear()
        self.drawHead()
        self.drawEyes()
        self.drawMouth()

    # Makes the mouth smile
    def isSmile(self):
        return self.__smile

    # Makes the circle yellow
    def isHappy(self):
        return self.__happy

    # Makes the eyes dark
    def isDarkEyes(self):
        return self.__darkEyes

    # Changes the mouth from one to another
    def changeMouth(self):
        if not self.__smile:
            self.__smile = True
        if self.__smile:
            self.__smile = False
        self.draw_face()

    # Changes the circle from color to color
    def changeEmotion(self):
        if not self.__happy:
            self.__happy = True
        if self.__happy:
            self.__happy = False
        self.draw_face()

    # Changes the eyes from color to color
    def changeEyes(self):
        if not self.__darkEyes:
            self.__darkEyes = True
        if self.__darkEyes:
            self.__darkEyes = False
        self.draw_face()


def main():
    face = Face()
    face.draw_face()
    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
