
import datetime, multiProgram


def yearAt100():

    '''
        while True:
            try:
                userName = input("Hello.  What is your name?  ")
            except ValueError:
                print("Please enter a valid entry")
    '''
    userName = ""  
    while userName == "":
        userName = input("enter name:  ")
    userAge = ""
    while userAge == "":
        userAge = input("And what is your age?  ")
    userAge = int(userAge)
    thisYear = datetime.datetime.now()
    yearOfHundred = thisYear.year + (100 - userAge)
    print("You, ",userName,", will be 100 years old in the year ", yearOfHundred, ".")
    input("press enter to continue.")

    #asks for a number, then prints a response that many times.  
    userNumber = ""
    while userNumber == "":
        userNumber = input("Now, give me a number between 1 and 5. \n")
    userNumber = int(userNumber)
    i = 1
    while i <= userNumber:
        print("You entered ", userNumber,".\n")
        i += 1
    final = input("press y to return to main menu, or 'n' to exit")
    if final == "y":
        multiProgram.welcome()
    if final == "n":
        exit()
    else:  
        print("Please press 'y' or 'n' \n")















