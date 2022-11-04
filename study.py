# STUDY.PY - practicing Python while studying Network+
# i can have a fill in the blank, remember to strip 
# away the caps / add caps where needed, no matter how the input
# is typed 

import random
import time

# creates blank lines, for easier reading
def lines(x):
    a = print('\n  ' * x)
    return a

def spaces(x):
    b = print(' ' * x)
    return b

lines(5)
print('     NETWORK+ PRACTICE QUESTIONS       ')
time.sleep(2)
lines(2)
print('     Press Ctrl + c when finished       ')
input('     Press enter to continue            ')

# the questions, labeled as "Qx"
i = 1  #for the while loops

def Q1():
    while i > 0:
        print('\n\nHow fast of speed would you expect from cable internet? ')
        print('Enter a number, in Mb:  \n')
        ans = input('   ')
        if ans == '15':
            print('\nEP')
            break
            # can also use i = 0
        else:
            print('\nNOPE')

def Q2():
    while i > 0:
        print('\n\nHow many wire pairs does 1000BASE-T use?\n')
        ans = input('Enter a number:    \n')
        if ans =='4':
            print('\nYEP')
            break
        else:
            print('\nNOPE')

def Q3():
    while i > 0:
        print('\n\nWhat is the maximum cable length of 10GBASE-T on Cat6? ')
        ans = input('Enter a number, in meters:  \n')
        if ans == '55':
            print('\nYEP')
            break
        else: 
            print('\nNOPE')

def Q4():
    while i > 0:
        print('''\n\n
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

def Q5():
    while i > 0:
        print('''\n\n
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

def Q6():
    while i > 0:
        print('''\n\n
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

def Q7():
    while i > 0:
        print('''\n\n
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

def Q8():
    while i > 0:
        print('''\n\n
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

def Q9():
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

def Q10():
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

def Q11():
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

def Q12():
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


while i > 0:
    questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12]
    random.choice(questions)()
    

# add a list, use a function for as much as possible, to reuse
# use a separate file, with the questions? 
#   if so, include spaces before and after, between questions.
# include a choice to exit, about every 5 questions or so.





