


import random

# creates blank lines, for easier reading
def lines(x):
    a = print('\n  ' * x)
    return a

def spaces(x):
    b = print(' ' * x)
    return b

lines(10)
print('     NETWORK+ PRACTICE QUESTIONS ')
lines(5)
print('     Press Ctrl + c when finished')
input('     Press enter to continue ')

# the questions, labeled as "Qx"
i = 1  #for the while loops

def Q1():
    lines(5)
    while i > 0:
        print('How fast of speed would you expect from cable internet? ')
        print('Enter a number, in Mb:  ')
        ans = input('   ')
        if ans == '15':
            lines(1)
            print('YEP')
            break
            # can also use i = 0
        else:
            lines(1)
            print('NOPE')
            lines(1)

def Q2():
    while i > 0:
        print('How many wire pairs does 1000BASE-T use?')
        ans = input('Enter a number:    ')
        if ans =='4':
            print('YEP')
            lines(5)
            break
        else:
            print('NOPE')
            lines(5)

def Q3():
    while i > 0:
        lines(5)
        print('What is the maximum cable length of 10GBASE-T on Cat6? ')
        ans = input('Enter a number, in meters:  ')
        lines(5)
        if ans == '55':
            print('YEP')
            lines(5)
            break
        else: 
            print('NOPE')
            lines(5)

def Q4():
    lines(5)
    while i > 0:
        print('''
        Any encryption that uses the same key for 
        encryption and decryption is called _________ . ''')
        print('''
                A.  Encoded key
                B.  Symmetric key
                C.  Single key
                D.  Sythetic key ''')
        lines(5)
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

while i > 0:
    questions = [Q1, Q2, Q3, Q4]
    random.choice(questions)()
    
# use a separate file, with the questions? 
#   if so, include spaces before and after, between questions.
# include a choice to exit, about every 5 questions or so.




