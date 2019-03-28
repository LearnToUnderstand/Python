

# combining multiple test programs and allowing user to choose which one to execute
# while also allowing user to return to the 'main menu' to start over again.
# all test programs taken from PracticePython.org


import datetime, time, sys; 



def welcome():
    print("Hello. What would you like to do?\n");
    print("Choose a number, below, to start that program: \n");
    print("1 :  Calculates what year you will turn age 100, then asks you for a number and prints a line that many times.\n");
    print("2 :  Determines if your number is odd or even...  \n");
    print("3 :  Play a MadLib-style game  \n");
    print("4 :  asdfasdfasdfasdf...  \n");

    q1 = int(input(" Please choose a selection:   "));


    if q1 == 1: 
 #   Determines what year user will turn age 100
        print("Hello.");
        userName = input("What is your name? ");
        userAge = int(input("And what is your age? "));
        thisYear = datetime.datetime.now();
        yearOfHundred = thisYear.year + (100 - userAge); 
        print("You, ",userName,", will be 100 years old in the year ", yearOfHundred, "."); 
        input("press enter to continue.");

        #asks for a number, then prints a response that many times.  
        userNumber = int(input("Now, give me a number between 1 and 5. \n"));
        i = 1;
        while i <= userNumber:
            print("You entered ", userNumber, ". \n");
            i += 1;
  #      yearTilHundred();
        final = input("press y to return to main menu, or 'n' to exit");
        if final == "y":
            welcome();
        if final == "n":
            exit();
        else:  
            print("Please press 'y' or 'n' \n");



#  Odd/Even program

    elif q1 == 2:

        usersNumber = int(input("Give me a number, and I'll determine if it's odd or even:  \n"));

        if usersNumber % 4 == 0:
            print("That's an even number, and a multiple of 4, also.");
        elif usersNumber % 2 == 0: 
            print("That's an even number");
        else: 
            print("That's an odd number");

        input("\nPress Enter to continue.\n");

        print("OK, now give me two numbers and I'll see if they are divisible by each other.\n");
        num1 = int(input("Give me a number.\n"));
        num2 = int(input("And another number.\n"));

        if num2 % num1 == 0: 
            print("The second number is divisible by the first.");
        elif num1 % num2 == 0:
            print("The first number is divislbe by the second.");
        else: 
            print("They are not divisible by each other.");

        input("\nPress Enter to complete the program.");

#        exit();

        final = input("press y to return to main menu, or 'n' to exit");
        if final == "y":
            welcome();
        if final == "n":
            exit();
        else:  
            print("Please press 'y' or 'n' \n");


# madlib game

    elif q1 == 3:
    
        def newline():
            print("\n");

        vowels = ('a','e','i','o','u','A','E','I','O','U')

        # function to determine first letter of the input is a vowel or consonant, 
        #to choose "a" or "an"
        # that comes before the user's word
        def aan1():  # for word1 only
            if word1.startswith(vowels): 
                print("an", end=" ");
            else:
                print("a", end=" ");

        def countdown():
            countdown = 3;
            while (countdown > 0):
                print("...", sep = " ");
                time.sleep(0.5)
                countdown -= 1;

        newline(); newline();

        initial_agreement = input("Hello!  would you like to create a story together? \n Type y for yes, or n for no.\n ")

        if (initial_agreement == "y"):
            print("Great!  Let's get started!")
            countdown();
        else:
            print("OK, bye!.");
            newline();
            KeyboardInterrupt();
            

        #begin user input section
        print("\n I'm going to ask you for a word, then you type your word and press enter.");
        print("After we do that several times, I'll randomly put those words into a story."); 
        word1 = input("\n First word:  Name verb (something you do):  \n");
        word2 = input("\n Great.  Now give me an adjective (a word that describes something):  \n"); 
        word3 = input("\n How about a another adjective (description word):   \n");
        word4 = input("\n Now, name a thing:  \n");
        word5 = input("\n Another verb, please (something you do):  \n");
        word6 = input("\n And another verb:  \n");
        word7 = input("\n Name an emotion, or feeling, that you express to someone (good or bad):  \n");
        word8 = input("\n Another noun, please (a thing):  \n");
        word9 = input("\n A verb (something you do: \n");
        word10 = input("\n And another verb: \n");
        word11 = input("\n A tool, or something useful in a tricky situation: \n");
        word12 = input("\n A thing, but in plural form (more than one): \n");
        word13 = input("\n Another thing, in plural form (more than one): \n");
        word14 = input("\n Adjective (a word that describes something), but something bad: \n");
        word15 = input("\n A verb (something you do): \n");
        word16 = input("\n Something you say to someone you're arguing with (1-5 words): \n");
        word17 = input("\n A verb ending in 'ing' (like running, instead of run): \n");
        word18 = input("\n Another verb, ending in 'ing': \n");
        word19 = input("\n A verb (something you do): \n");
        word20 = input("\n An adjective, ending in 'ly' (like beautifully, stupidly, quickly, etc.): \n");
        word21 = input("\n And, lastly... another verb (something you do): \n");





        # story time. 
        newline();
        print("Please wait while I put our story together"); 
        time.sleep(1);
        newline(); countdown();


        '''
        print("\n Once upon ", end="") 
        aan1();
        print(word1, end="");
        print(" there was a dog that would always " + word2 + ".");
        print("This dog was from " + word3 + ".");

        '''

        newline();

        print("HOW TO DEAL WITH DIFFICULT PEOPLE");
        print("By you and me");

        newline();

        print("1. You have to remember to ", word1, ".");
        print("It's the number one step in dealing with 'unreasonable' people. ");
        print("Everyone wants to feel ", word2, ".");
        print("No progress can take place until the other person feels acknowledged.");
        print("While you're listening, really focus on what the other person is saying, not what you want to say next.");

        newline();

        print("2.  Stay ", word3, ".");
        print("When a situation is emotionally charged, it's easy to get caught up in the ", end = "");
        print(word4, end = "");
        print(" of the moment.  \nMonitor your breathing. Try to take some slow, deep breaths.");

        newline();
        input("Press enter to continue");
        newline();

        print("3.  Don’t ", word5, ".");
        print("You don't know what the other person is going through.  ");

        newline();

        print("4.  ", word6, " respect and dignity toward the other person. ");
        print("No matter how a person is treating you, showing ", word7, end = "");
        print(" will not help productively resolve the situation. ");

        newline();

        print("5.  Look for the hidden ", word8, "." );
        print("What is this person really trying to gain? What is this person trying to ", word9, "?");
        print("Look for others around you who might be able to help. ");
        print("If you’re at work and there’s an irate customer, quickly ", word10, end = "");
        print(" to see if a ", word11, " is close by. ");

        newline();
        input("Press enter to continue the story.");
        newline();

        print("6.  Don't demand ", word12, " or ", word13, ".");
        print("For example, telling someone who's upset to be quiet and calm down ", end = "");
        print("will just make him or her ", word14, ".");
        print("  Instead, ask the person what they are upset about, and allow them to ", word15, ".");

        newline();

        print("7.  Saying, 'I understand,' usually makes things worse. Instead, say '", word16, "'."); 

        newline();

        print("8.  Avoid ", word17, ", as this may look like you are ", word18, "the person.");
        print("Similarly, humor can sometimes lighten the mood, but more often than not,");
        print("it’s risky and it may ", word19, ".");

        newline();

        print("9.  Don’t act ", word20, ". This might be tough.");
        print("You’re naturally not enjoying the other person saying nasty things or things that you know aren’t true.");
        print("You’re going to want to ", word21, " yourself.");
        print("But the other person is so emotionally revved up, it’s probably not going to help. ");
        print("Remember, this is not about you. Don’t take it personally, and remind yourself: ");
        print("Hurt people hurt people.  You can help by showing that you care."); 

        newline();
        input("Press enter to continue...");
        newline();

        print("Thank you for playing!  Watch for more stories coming in the future!");

        time.sleep(2);

#        exit();

        final = input("press y to return to main menu, or 'n' to exit");
        if final == "y":
            welcome();
        if final == "n":
            exit();
        else:  
            print("Please press 'y' or 'n' \n");



    else: 
        print("bye");
        exit();



welcome();












