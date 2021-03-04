from tkinter import *


#Project purpose: detect strong or weak passwords. With a Graphical User Interface implementation
#Ryan Herman


#Listen for button press
def actionEvent():
    password = str(entryBox.get())
    #Pass password to checkPassword()
    result = checkPassword(password)
    issueMessage = ""

    # ErrorArray [0-SixChar, 1-ContainUpperCase, 2-ContainLowerCase, 3-ContainDigit, 4-ContainSpecial]
    if result[0] == 1:
        issueMessage = issueMessage + " \n - Password is too short"
    if result[1] == 1:
        issueMessage = issueMessage + " \n - Password must contain an uppercase letter"
    if result[2] == 1:
        issueMessage = issueMessage + " \n - Password must contain a lowercase letter"
    if result[3] == 1:
        issueMessage = issueMessage + " \n - Password must contain a number"
    if result[4] == 1:
        issueMessage = issueMessage + " \n - Password must contain a special character"

    if 1 not in result:
        issueMessage = "Password is good"
        resultLabel.config(fg = 'Green', text= "Password is strong")
    else:
        resultLabel.config(fg = 'Red',text=issueMessage)


def checkPassword(password):

    #ErrorArray [0-SixChar, 1-ContainUpperCase, 2-ContainLowerCase, 3-ContainDigit, 4-ContainSpecial]
    #Return 1 if no issue with password
    resultArray = [1] * 5
    if len(password) >= 6:
        resultArray[0] = 0

    for i in range(len(password)):
        if password[i].isnumeric():
            resultArray[3] = 0
        elif password[i].isupper():
            resultArray[1] = 0
        elif password[i].islower():
            resultArray[2] = 0
        elif (password[i] >= 'a' and password[i] <= "z") or (password[i] >= 'A' and password[i] <="Z"):
            containChar = True
        else:
            resultArray[4] = 0

    return resultArray


#Build the GUI
password = ""
mainFrame = Tk()
mainFrame.geometry("275x300")

outerFrame = Frame(mainFrame)
outerFrame.pack()

topHalfFrame = Frame(outerFrame)
topHalfFrame.pack(side=TOP)

bottomHalfFrame = Frame(outerFrame)
bottomHalfFrame.pack(side=BOTTOM)

q1Frame = Frame(topHalfFrame)
q1Frame.pack(side=TOP)

q2Frame = Frame(topHalfFrame)
q2Frame.pack(side=BOTTOM)

q3Frame = Frame(bottomHalfFrame)
q3Frame.pack(side=TOP)

q4Frame = Frame(bottomHalfFrame)
q4Frame.pack(side=BOTTOM)

infoLabel = Label(q1Frame, text="Password Strength Check \n\n Password should contain:\n"
                                    " - At least 6 characters \n - An uppercase/ lowercase letter \n"
                                    " - A number \n - A special character \n")
infoLabel.pack(side=TOP)

checkLabel = Label(q2Frame, text="Check Password:")
checkLabel.pack(side=LEFT)

entryBox = Entry(q2Frame)
entryBox.pack(side=RIGHT)

goButton = Button(q3Frame, text="Check", fg='Blue', command = actionEvent)
goButton.pack(side=TOP)

resultLabel = Label(q4Frame)
resultLabel.pack(side= BOTTOM)


mainFrame.mainloop()





