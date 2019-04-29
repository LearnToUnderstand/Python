# combining multiple test programs and allowing user to choose which one to execute
# while also allowing user to return to the 'main menu' to start over again.
# all test programs taken from PracticePython.org


import datetime, time, sys, yearAt100, oddEven, madLib 



def welcome():
    print("Hello. What would you like to do?\n")
    print("Choose a number, below, to start that program: \n")
    print("1 :  Calculates what year you will turn age 100, then asks you for a number and prints a line that many times.\n")
    print("2 :  Determines if your number is odd or even, then checks for divisibility of numbers you provide.   \n")
    print("3 :  Play a MadLib-style game called 'How to Deal With Difficult People' \n")
    print("4 :  asdfasdfasdfasdf...  \n")
    print("0 :  Exit this program.")


welcome()




choice = ""

while choice == "":
    choice = input("Please choose a selection:  ")
    if choice == "1":
        yearAt100.yearAt100()
    elif choice == "2":
        oddEven.oddEven()
    elif choice == "3":
        madLib.madLib()
    elif choice == "Quit":
        choice == str(choice).lower
        print("Thanks for stopping by!")
        time.sleep(2)
        exit()
#    else:
#        print("Invalid selection.")
         








