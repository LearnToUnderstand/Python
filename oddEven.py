import multiProgram


def oddEven():
    usersNumber = int(input("Give me a number, and I'll determine if it's odd or even:  \n"))

    if usersNumber % 4 == 0:
        print("That's an even number, and a multiple of 4, also.")
    elif usersNumber % 2 == 0: 
        print("That's an even number")
    else: 
        print("That's an odd number")

    input("\nPress Enter to continue.\n")

    print("OK, now give me two numbers and I'll see if they are divisible by each other.\n")
    num1 = int(input("Give me a number.\n"))
    num2 = int(input("And another number.\n"))

    if num2 % num1 == 0: 
        print("The second number is divisible by the first.")
    elif num1 % num2 == 0:
        print("The first number is divislbe by the second.")
    else: 
        print("They are not divisible by each other.")

    input("\nPress Enter to complete the program.")
    final = input("press y to return to main menu, or 'n' to exit")
    if final == "y":
        multiProgram.welcome()
    if final == "n":
        exit()
    else:  
        print("Please press 'y' or 'n' \n")















