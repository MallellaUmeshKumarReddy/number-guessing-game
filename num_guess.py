# number guessing game
import random
import time
#using time to maintain gap between every action
print('number guessing game')
x=0
y=1
j=input('\nPlease enter your name : ')
while (True):    #continues loop
    p=int(input("\npress 0 to quit game and 1 to start : "))
    time.sleep(0.5)
    if p==y:     #to proceed into the game
        print('kids chose less tahn 10')
        print('men and women chose bellow 99')
        print('legends choose above 100')
        print('i will leave to you to decide what you are') 
        n=int(input("choose range : "))
        time.sleep(0.5)
        m=random.randint(1,n)
        o=int(input("enter your number : "))
        time.sleep(0.5)
        if m==o:    #comparing cpu and players input
            print("((o|o) congrats your guess is right")
            time.sleep(1.0)
        else:
            print(" :( better luck next time cpu selected " ,(m))
            time.sleep(1.0)
        continue
    elif p==x:
        print('quitting...')
        time.sleep(2.0)
    else:
        print('pressed wrong option game terminating')
    break #breaking if 0 is selected


    






    
