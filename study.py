# STUDY.PY - practicing Python while studying Network+

import random
import time

# to create blank lines, for easier reading
# wherever more space is needed between quesions, etc. 
def lines(x):
    print('\n  ' * x)

def spaces(x):
    print(' ' * x)

lines(5)
print('     NETWORK+ PRACTICE QUESTIONS       ')
time.sleep(1)
lines(2)
print('     Press Ctrl + c when finished       ')
time.sleep(1.)
input('     Press enter to continue            ')

i = 1  #for the while loops (for each question)
a = 1  #increments to give the option to quit every 5 questions

def Q1():
    global a
    while i > 0:
        lines(5)
        print('How fast of speed would you expect from cable internet? ')
        print('Enter a number, in Mb:  \n')
        ans = input('   ')
        if ans == '15':
            print('\nYEP')
            break
            # can also use i = 0
        else:
            print('\nNOPE')
    a += 1  #keep this variable outside of the while loop

def Q2():
    global a
    while i > 0:
        lines(5)
        print('\n\nHow many wire pairs does 1000BASE-T use?\n')
        ans = input('Enter a number:    ')
        if ans =='4':
            print('\nYEP')
            break
        else:
            print('\nNOPE')
    a += 1  #keep this variable outside of the while loop

def Q3():
    global a
    while i > 0:
        lines(5)
        print('What is the maximum cable length of 10GBASE-T on Cat6? ')
        ans = input('Enter a number, in meters:  ')
        if ans == '55':
            print('\nYEP')
            break
        else: 
            print('\nNOPE')
    a += 1  #keep this variable outside of the while loop

def Q4():
    global a
    while i > 0:
        lines(5)
        print('''
        Any encryption that uses the same key for 
        encryption ad decryption is called _________ . ''')
        print('''
                A.  Encoded key
                B.  Symmetric key
                C.  Single key
                D.  Sythetic key ''')
        ans = input('Enter a lower case letter only:    ')
        if ans == 'a':
            print('\nYEP')
            break
        elif ans == 'b':
            print('\nnope')
        elif ans == 'c':
            print('\nnope')
        elif ans == 'd':
            print('\nnope')
    a += 1  #keep this variable outside of the while loop

def Q5():
    global a
    while i > 0:
        lines(5)
        print('''
        When should you use a cable tester to troubleshoot
        a network cable? ''')
        print('''
                A.  When you have a host experiencing 
                    a very slow connection
                B.  When you have an intermittent 
                    connection problem
                C.  When you have a dead connection 
                    and you suspect a broken cable
                D.  When you are trying to find the 
                    correct cable up in the plenum''')
        ans = input('\nEnter a lower case letter only:    ')
        if ans == 'c':
            print('''\n\n
            CORRECT!  Cable testers can only show that you have a 
            broken or poorly wired cable, not if the cable is up 
            to proper specifications. ''')
            time.sleep(5)
            break
        elif ans == 'b':
            print('\n nope \n')
        elif ans == 'c':
            print('\n nope \n')
        elif ans == 'd':
            print('\n nope \n')
    a += 1  #keep this variable outside of the while loop

def Q6():
    global a
    while i > 0:
        lines(5)
        print('''
        What two devices together enable you to pick a 
        single cable out of a stack of cables? (Pick two, one at a time)''')
        print('''
                A.  Tone aggregator
                B.  Tone binder
                C.  Tone generator
                D.  Tone probe ''')
        print('\nPick two, enter one at a time')
        ans1 = input('First choice:    ')
        ans2 = input('Second choice:   ')
        if ans1 == 'c' or 'd':
            if ans2 == 'c' or 'd':
                print('\nYEP')
                time.sleep(2)
                break
            else:
                print('\nNOPE')
        else:
            print('\nnope')
    a += 1  #keep this variable outside of the while loop

def Q7():
    global a
    while i > 0:
        lines(5)
        print('''
        A newly installed host uses what NDP control message 
        type to find available routers on the network? ''')
        print('''
                A.  Network advertisement
                B.  Network solicitation
                C.  Router advertisement
                D.  Router solicitation''')
        ans = input('Enter a lower case letter only:    ')
        if ans == 'd':
            print('YEP')
            break
        elif ans == 'b':
            print('nope')
        elif ans == 'c':
            print('nope')
        elif ans == 'a':
            print('nope')
    a += 1  #keep this variable outside of the while loop

def Q8():
    global a
    while i > 0:
        print('''
        What is the progressive loss of radio signal passing 
        through different media called? ''')
        print('''
                A.  Attenuation 
                B.  EAP
                C.  RFI
                D.  SNR ''')
        ans = input('Enter a lower case letter only:    ')
        if ans == 'a':
            print('YEP')
            break
        elif ans == 'b':
            print('nope')
        elif ans == 'c':
            print('nope')
        elif ans == 'd':
            print('nope')
    a += 1  #keep this variable outside of the while loop

def Q9():
    global a
    while i > 0:
        print('''\n\n
        Which technology enables use of a WAP without directly connecting the 
        WAP to an AC power outlet?  ''')
        print('''
                A.  AES
                B.  PoE
                C.  Powered Wi-Fi
                D.  TKIP  ''')
        ans = input('Enter a lower case letter only:    ')
        if ans == 'b':
            print('''YEP!  
                    Power over Ethernet enables a wireless 
                    access point to use electricity from a PoE switch
                    rather than connect to an AC power outlet direcctly.  ''')
            break
        elif ans == 'a':
            print('nope')
        elif ans == 'c':
            print('nope')
        elif ans == 'a':
            print('nope')
    a += 1  #keep this variable outside of the while loop

def Q10():
    global a
    while i > 0:
        print('''\n\n
        To achieve maximum Wi-Fi coverage in a room, 
        where should you place the WAP? ''')
        print('''
                A.  On the north side of the room
                B.  In the center of the room
                C.  Near a convenient electrical outlet
                D.  It doesn't matter  ''')
        ans = input('Enter a lower case letter only:    ')
        if ans == 'b':
            print('YEP')
            break
        elif ans == 'd':
            print('nope')
        elif ans == 'c':
            print('nope')
        elif ans == 'a':
            print('nope')
    a += 1  #keep this variable outside of the while loop

def Q11():
    global a
    while i > 0:
        print('''\n\n
        Which of the following is the most secure method of 
        wireless encryption?  ''')
        print('''
                A.  WEP
                B.  WPA
                C.  WPA2
                D.  WPA3 ''')
        ans = input('Enter a lower case letter only:    ')
        if ans == 'd':
            print('YEP')
            break
        elif ans == 'b':
            print('nope')
        elif ans == 'c':
            print('nope')
        elif ans == 'a':
            print('nope')
    a += 1  #keep this variable outside of the while loop

def Q12():
    global a 
    while i > 0:
        print('''\n\n
        what do you call a wireless network in infrasctructure mode 
        with more than one access point?  ''')
        print('''
                A.  BSS
                B.  EBSS
                C.  WBSS
                D.  ExNet  ''')
        ans = input('Enter a lower case letter only:    ')
        if ans == 'b':
            print('YEP!  (Extended Basic Service Set)')
            break
        elif ans == 'd':
            print('nope')
        elif ans == 'c':
            print('nope')
        elif ans == 'a':
            print('nope')
    a += 1  #keep this variable outside of the while loop

def phrase():
    phrases = [
            'Good job deciding to study some more!',
            'Keep at it!',
            'Keep it up!',
            'More studying = easier exam!',
            'Nice work']
    phrase = random.choice(phrases)
    print(phrase)

while i > 0:
    questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12]
    random.choice(questions)()
    # THE OPTION TO QUIT EVERY 5 QUESTIONS IS NOT WORKING
    if a % 5 == 0:
        print('\nDo you want to keep going?')
        quit = input('\nPress y or n :     ')
        if quit == 'n':
            lines(2)
            phrase()
            time.sleep(2)
            exit()
        else: a = 1

